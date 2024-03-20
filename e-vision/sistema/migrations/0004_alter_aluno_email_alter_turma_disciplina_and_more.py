# Generated by Django 5.0.3 on 2024-03-12 03:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_alter_presenca_aula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.EmailField(max_length=128),
        ),
        migrations.AlterField(
            model_name='turma',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.disciplina'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.professor'),
        ),
    ]