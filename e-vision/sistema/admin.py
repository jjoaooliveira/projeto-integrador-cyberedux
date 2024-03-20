from django.contrib import admin
from . import models

@admin.register(models.Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['nome']

    
@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    fields = ['nome', 'cpf', 'email', 'condicao_financeira', 'escolaridade', 'trabalha']
    list_display = ('nome', 'cpf', 'email', 'condicao_financeira', 'escolaridade', 'trabalha')


@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome']

    
@admin.register(models.Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'get_cursos')

    def get_cursos(self, obj):
        return ' \ '.join([c.nome for c in obj.cursos.all()])
    
@admin.register(models.Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['disciplina', 'periodo', 'professor', 'aluno']

    def aluno(self, obj):
        return ' \ '.join([a.nome for a in obj.alunos.all()])

    
@admin.register(models.Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ['turma', 'professor', 'data']


@admin.register(models.Presenca)
class Presenca(admin.ModelAdmin):
    fields = ['aluno', 'aula', 'presente']
    list_display = ('aluno', 'aula', 'presente')


@admin.register(models.Matricula)
class Matricula(admin.ModelAdmin):
    fields = ['aluno', 'data', 'desistencia']
    list_display = ('aluno', 'data', 'desistencia')

