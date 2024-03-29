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
from django.urls import path

from .views import *

urlpatterns = [
    path('',Feedback.as_view(),name='feedback'),
    path('disciplina/',CreateFeedbackDisciplina.as_view(),name='cadastrar-feedback-disciplina'),
    path('disciplina/lista/', ListFeedbackDisciplina.as_view(),name='lista-feedback-disciplina'),
    path('espaco/',CreateFeedbackEspaco.as_view(),name='cadastrar-feedback-espaco'),
    path('espaco/lista/', ListFeedbackEspaco.as_view(),name='lista-feedback-espaco'),
]