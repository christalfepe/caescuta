from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import *
from django.urls import reverse_lazy


class Home(TemplateView):
    template_name = "home.html"



class CreateDisciplina(CreateView):
    model = Disciplina
    fields = ['codigo', 'nome']
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class CreateEspaco(CreateView):
    model = Espaco
    fields = ['nome_espaco']
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class CreateCurso(CreateView):
    model = Curso
    fields = ['nome_curso']
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class UpdateDisciplina(UpdateView):
    model = Disciplina
    fields = ['nome']
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class UpdateEspaco(UpdateView):
    model = Espaco
    fields = ['nome_espaco']
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class UpdateCurso(UpdateView):
    model = Curso
    fields = ['nome_curso']
    template_name = 'form.html'
    success_url = reverse_lazy('home')


class DeleteDisciplina(DeleteView):
    model = Disciplina
    template_name = 'form_exclui.html'
    success_url = reverse_lazy('home')


class DeleteCurso(DeleteView):
    model = Curso
    template_name = 'form_exclui.html'
    success_url = reverse_lazy('home')


class DeleteEspaco(DeleteView):
    model = Espaco
    template_name = 'form_exclui.html'
    success_url = reverse_lazy('home')


class ListDisciplina(ListView):
    model = Disciplina
    template_name = 'lista/disciplina.html'


class ListCurso(ListView):
    model = Curso
    template_name = 'lista/curso.html'


class ListEspaco(ListView):
    model = Espaco
    template_name = 'lista/espaco.html'
