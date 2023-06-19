from django.db import models

# Create your models here.
class Disciplina(models.Model):
    codigo = models.IntegerField(verbose_name="Código")
    nome = models.CharField(max_length=150)

    def __str__(self):
        return "{} ({})".format(self.codigo, self.nome)


class Espaco(models.Model):
    nome_espaco = models.CharField(max_length=150, verbose_name="Espaço")

    def __str__(self):
        return "{}".format(self.nome_espaco)

class Curso(models.Model):
    codigo_curso = models.IntegerField(primary_key=True, verbose_name="Código do Curso")
    nome_curso = models.CharField(max_length=150, verbose_name="Nome do Curso")
    def __str__(self):
        return "{} ({})".format(self.codigo_curso,self.nome_curso)