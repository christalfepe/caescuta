from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
class Usuario(ListView):
    model = Perfil
    template_name = "usuario.html"

class Criar_Perfil(CreateView):
    model = Perfil
    fields = ['matricula', 'nome', 'curso']
    template_name = 'form.html'
    success_url = reverse_lazy('usuario')
def editar(request):
    return render(request, 'editar.html')