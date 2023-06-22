from django.views.generic import TemplateView, CreateView, ListView
from .models import FeedbackDisciplina, FeedbackEspaco
from django.urls import reverse_lazy


class Feedback(TemplateView):
    template_name = 'feedback.html'


class CreateFeedbackDisciplina(CreateView):
    model = FeedbackDisciplina
    fields = ['disciplina','feedback_dis']
    template_name = 'feedback/form.html'
    success_url = reverse_lazy('feedback')

class CreateFeedbackEspaco(CreateView):
    model = FeedbackEspaco
    fields = ['espaco','feedback_esp']
    template_name = 'feedback/form.html'
    success_url = reverse_lazy('feedback')

class ListFeedbackEspaco(ListView):
    model = FeedbackEspaco
    template_name = 'feedback/lista_espaco.html'