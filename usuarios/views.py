from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
class Usuario(ListView):
    model = ModelUsuario
    template_name = "usuario.html"