from django.db import models

# Create your models here.
class Pesquisa(models.Model):
    codigo_pesquisa = models.IntegerField(primary_key=True, verbose_name="Código da pesquisa")
    titulo = models.CharField(max_length=150, verbose_name="Título da Pesquisa")
    data = models.DateTimeField(verbose_name="Data da Pesquisa")

    def __str__(self):
        return "{} ({})".format(self.codigo_pesquisa,self.titulo)
class Questao(models.Model):
    codigo_questao = models.IntegerField(primary_key=True, verbose_name="Código da Questão")
    texto = models.CharField(max_length=400, verbose_name="Texto da questão")

    def __str__(self):
        return "{} ({})".format(self.codigo_questao,self.texto)

class Pesquisa_Questao(models.Model):
    resposta = models.IntegerField(verbose_name="Resposta-Pesquisa")
    codigo_pesquisa = models.ForeignKey(Pesquisa, on_delete=models.PROTECT, verbose_name="Código da Pesquisa")
    codigo_questao = models.ForeignKey(Questao, on_delete=models.PROTECT, verbose_name="Código da Questão")

    def __str__(self):
        return "{} ({}) - {}".format(self.Pesquisa.codigo_pesquisa,self.Questao.codigo_questao, self.resposta)