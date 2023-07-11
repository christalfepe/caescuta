from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import Usuario, Admin

urlpatterns = [
    path('contas/', include('django.contrib.auth.urls')),# incluindo as rotas de autenticação do próprio Django
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('usuarios/lista',Usuario.as_view(),name='usuario'),
    path('admin/',Admin.as_view(),name='admin'),
]