from django.db import models
from cadastro.models import Disciplina, Espaco
# Create your models here.

class FeedbackDisciplina(models.Model):
    feedback_dis = models.CharField(max_length=400,verbose_name="Feedback da Disciplina")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.feedback_dis,self.disciplina.nome)

class FeedbackEspaco(models.Model):
    feedback_esp = models.CharField(max_length=400,verbose_name="Feedback do Espaço")
    espaco = models.ForeignKey(Espaco, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.feedback_esp,self.espaco.nome)



