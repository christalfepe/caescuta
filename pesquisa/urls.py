
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.landing, name="pesquisa"),
    path("lista/", views.survey_list, name="survey-list"),
    path("minhalista/", views.minha_lista, name="minha-lista"),
    path("<int:pk>/", views.detail, name="survey-detail"),
    path("create/", views.create, name="survey-create"),
    path("<int:pk>/deletar/", views.delete, name="survey-delete"),
    path("<int:pk>/editar/", views.edit, name="survey-edit"),
    path("<int:pk>/questao/", views.question_create, name="survey-question-create"),
    path(
        "<int:survey_pk>/questao/<int:question_pk>/opcao/",
        views.option_create,
        name="survey-option-create",
    ),
    path("<int:pk>/comecar/", views.start, name="survey-start"),
    path("<int:survey_pk>/submissao/<int:sub_pk>/", views.submit, name="survey-submit"),
    path("<int:pk>/obrigado/", views.thanks, name="survey-thanks"),
]