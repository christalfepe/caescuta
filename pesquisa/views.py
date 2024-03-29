from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import transaction
from django.forms.formsets import formset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from .forms import SurveyForm, QuestionForm, OptionForm, AnswerForm, BaseAnswerFormSet
from .models import Survey, Question, Answer, Submission


class LandingView(TemplateView):
    template_name = "landing.html"

@login_required
def survey_list(request):
    """User can view all their survey"""
    pesquisas = Survey.objects.filter(is_active=True).order_by("-created_at").all()
    paginator = Paginator(pesquisas, 3)
    pages = request.GET.get('page')
    surveys = paginator.get_page(pages)
    return render(request, "survey/lista.html", {"surveys": surveys})

@login_required
def minha_lista(request):
    """User can view all their survey"""
    pesquisas = Survey.objects.filter(creator=request.user).order_by("-created_at").all()
    paginator = Paginator(pesquisas,3)
    pages = request.GET.get('page')
    surveys=paginator.get_page(pages)
    return render(request, "survey/minhalista.html", {"surveys": surveys})

@login_required
def detail(request, pk):
    """User can view an active survey"""
    try:
        survey = Survey.objects.prefetch_related("question_set__option_set").get(
            pk=pk, creator=request.user
        )
    except Survey.DoesNotExist:
        raise Http404()

    questions = survey.question_set.all()

    # Calculate the results.
    # This is a naive implementation and it could be optimised to hit the database less.
    # See here for more info on how you might improve this code: https://docs.djangoproject.com/en/3.1/topics/db/aggregation/
    for question in questions:
        option_pks = question.option_set.values_list("pk", flat=True)
        total_answers = Answer.objects.filter(option_id__in=option_pks).count()
        for option in question.option_set.all():
            num_answers = Answer.objects.filter(option=option).count()
            option.percent = 100.0 * num_answers / total_answers if total_answers else 0


    num_submissions = survey.submission_set.filter(is_complete=True).count()
    return render(
        request,
        "survey/detalhes.html",
        {
            "survey": survey,
            "questions": questions,
            "num_submissions": num_submissions,
        },
    )


@login_required
def create(request):
    """User can create a new survey"""
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.creator = request.user
            survey.save()
            return redirect("survey-edit", pk=survey.id)
    else:
        form = SurveyForm()

    return render(request, "survey/criar.html", {"form": form})


@login_required
def delete(request, pk):
    """User can delete an existing survey"""
    survey = get_object_or_404(Survey, pk=pk, creator=request.user)
    if request.method == "POST":
        survey.delete()

    return redirect("minha-lista")
@login_required
def desativar(request, pk):
    """User can delete an existing survey"""
    survey = get_object_or_404(Survey, pk=pk, creator=request.user)
    if request.method == "POST":
        survey.is_active = False
        survey.save()
    return redirect("minha-lista")
@login_required
def ativar(request, pk):
    """User can delete an existing survey"""
    survey = get_object_or_404(Survey, pk=pk, creator=request.user)
    if request.method == "POST":
        survey.is_active = True
        survey.save()
    return redirect("minha-lista")
@login_required
def edit(request, pk):
    """User can add questions to a draft survey, then acitvate the survey"""
    try:
        survey = Survey.objects.prefetch_related("question_set__option_set").get(
            pk=pk, creator=request.user
        )
    except Survey.DoesNotExist:
        raise Http404()

    if request.method == "POST":
        survey.is_active = True
        survey.save()
        return redirect("survey-detail", pk=pk)
    else:
        questions = survey.question_set.all()
        return render(request, "survey/editar.html", {"survey": survey, "questions": questions})


@login_required
def question_create(request, pk):
    """User can add a question to a draft survey"""
    survey = get_object_or_404(Survey, pk=pk, creator=request.user)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.survey = survey
            question.save()
            return redirect("survey-option-create", survey_pk=pk, question_pk=question.pk)
    else:
        form = QuestionForm()

    return render(request, "survey/questao.html", {"survey": survey, "form": form})


@login_required
def option_create(request, survey_pk, question_pk):
    """User can add options to a survey question"""
    survey = get_object_or_404(Survey, pk=survey_pk, creator=request.user)
    question = Question.objects.get(pk=question_pk)
    if request.method == "POST":
        form = OptionForm(request.POST)
        if form.is_valid():
            option = form.save(commit=False)
            option.question_id = question_pk
            option.save()
    else:
        form = OptionForm()

    options = question.option_set.all()
    return render(
        request,
        "survey/opcoes.html",
        {"survey": survey, "question": question, "options": options, "form": form},
    )


def start(request, pk):
    """Survey-taker can start a survey"""
    survey = get_object_or_404(Survey, pk=pk, is_active=True)
    if request.method == "POST":
        sub = Submission.objects.create(survey=survey)
        return redirect("survey-submit", survey_pk=pk, sub_pk=sub.pk)

    return render(request, "survey/comecar.html", {"survey": survey})


def submit(request, survey_pk, sub_pk):
    """Survey-taker submit their completed survey."""
    try:
        survey = Survey.objects.prefetch_related("question_set__option_set").get(
            pk=survey_pk, is_active=True
        )
    except Survey.DoesNotExist:
        raise Http404()

    try:
        sub = survey.submission_set.get(pk=sub_pk, is_complete=False)
    except Submission.DoesNotExist:
        raise Http404()

    questions = survey.question_set.all()
    options = [q.option_set.all() for q in questions]
    form_kwargs = {"empty_permitted": False, "options": options}
    AnswerFormSet = formset_factory(AnswerForm, extra=len(questions), formset=BaseAnswerFormSet)
    if request.method == "POST":
        formset = AnswerFormSet(request.POST, form_kwargs=form_kwargs)
        if formset.is_valid():
            with transaction.atomic():
                for form in formset:
                    Answer.objects.create(
                        option_id=form.cleaned_data["option"], submission_id=sub_pk,
                    )

                sub.is_complete = True
                sub.save()
            return redirect("survey-thanks", pk=survey_pk)

    else:
        formset = AnswerFormSet(form_kwargs=form_kwargs)

    question_forms = zip(questions, formset)
    return render(
        request,
        "survey/submissao.html",
        {"survey": survey, "question_forms": question_forms, "formset": formset},
    )


def thanks(request, pk):
    """Survey-taker receives a thank-you message."""
    survey = get_object_or_404(Survey, pk=pk, is_active=True)
    return render(request, "survey/obrigado.html", {"survey": survey})

landing = LandingView.as_view()