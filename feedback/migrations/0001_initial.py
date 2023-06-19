# Generated by Django 3.1.4 on 2023-05-07 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(verbose_name='Código')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback_Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_dis', models.CharField(max_length=400, verbose_name='Feedback da Disciplina')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='feedback.disciplina')),
            ],
        ),
    ]