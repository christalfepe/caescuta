from django.views.generic import ListView
from .models import *
from django.views.generic import ListView, CreateView

from .models import *


# Create your views here.
class Usuario(ListView):
    model = ModelUsuario
    template_name = "usuario.html"

class Admin(CreateView):
    model = UsuarioManager
    template_name = "admin.html"
