from django.views.generic import TemplateView, CreateView, ListView
from .models import Feedback_Disciplina, Feedback_Espaco
from django.urls import reverse_lazy
# Create your views here.
class Feedback(TemplateView):
    template_name = 'feedback.html'


class CreateFeedback_Disciplina(CreateView):
    model = Feedback_Disciplina
    fields = ['disciplina','feedback_dis']
    template_name = 'feedback/form.html'
    success_url = reverse_lazy('feedback')

class CreateFeedback_Espaco(CreateView):
    model = Feedback_Espaco
    fields = ['espaco','feedback_esp']
    template_name = 'feedback/form.html'
    success_url = reverse_lazy('feedback')

class ListFeedback_Espaco(ListView):
    model = Feedback_Espaco
    template_name = 'feedback/lista.html'