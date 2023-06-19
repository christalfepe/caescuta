from django.db import models
from cadastro.models import Curso
# Create your models here.
class Perfil(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome",blank=False)
    matricula = models.IntegerField(primary_key=True, verbose_name="Matrícula")
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT,verbose_name="Código do curso")


    def __str__(self):
        return "{} ({}) - {}".format(self.nome,self.matricula, self.curso.nome_curso)
