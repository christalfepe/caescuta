from django.db import models
from cadastro.models import Disciplina, Espaco
# Create your models here.

class Feedback_Disciplina(models.Model):
    feedback_dis = models.CharField(max_length=400,verbose_name="Feedback da Disciplina")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.feedback_dis,self.disciplina.nome)

class Feedback_Espaco(models.Model):
    feedback_esp = models.CharField(max_length=400,verbose_name="Feedback do Espaço")
    espaco = models.ForeignKey(Espaco, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.feedback_esp,self.espaco.nome)



