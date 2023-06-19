"""CAescuta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('cadastro/disciplina/', CreateDisciplina.as_view(), name='cadastrar-disciplina'),
    path('cadastro/espaco/', CreateEspaco.as_view(), name='cadastra-espaco'),
    path('cadastro/curso/', CreateCurso.as_view(), name='cadastra-curso'),
    path('editar/disciplina/<int:pk>/', UpdateDisciplina.as_view(), name='edita-disciplina'),
    path('editar/espaco/<int:pk>/', UpdateEspaco.as_view(), name='edita-espaco'),
    path('editar/curso/<int:pk>/', UpdateCurso.as_view(), name='edita-curso'),
    path('excluir/disciplina/<int:pk>/', DeleteDisciplina.as_view(), name='exclui-disciplina'),
    path('excluir/espaco/<int:pk>/', DeleteEspaco.as_view(), name='exclui-espaco'),
    path('excluir/curso/<int:pk>/', DeleteCurso.as_view(), name='exclui-curso'),
    path('listar/disciplina/', ListDisciplina.as_view(), name='lista-disciplina'),
    path('listar/espaco/', ListEspaco.as_view(), name='lista-espaco'),
    path('listar/curso/', ListCurso.as_view(), name='lista-curso'),
]
