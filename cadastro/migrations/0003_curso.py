# Generated by Django 3.1.4 on 2023-05-09 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_espaco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo_curso', models.IntegerField(primary_key=True, serialize=False, verbose_name='Código do Curso')),
                ('nome_curso', models.CharField(max_length=150, verbose_name='Nome do Curso')),
            ],
        ),
    ]