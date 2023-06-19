# Generated by Django 3.1.4 on 2023-05-09 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0003_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('matricula', models.IntegerField(primary_key=True, serialize=False, verbose_name='Matrícula')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro.curso', verbose_name='Código do curso')),
            ],
        ),
    ]