from django.urls import path
from . import views

urlpatterns = [
    path('', views.portal, name='portal'),
    path('professor/', views.lista_professor, name='professores'),
    path('professor/cadastro/', views.cadastro_professor, name='cadastro-professor'),
    path('professor/<int:professor_id>/editar', views.editar_professor, name='editar-professor'),
    path('professor/<int:professor_id>/deletar', views.delete_professor, name='deletar-professor'),

    path('usuario/', views.lista_usuario, name='usuarios'),
    path('usuario/cadastro/', views.cadastro_usuario, name='cadastro-usuario'),
    path('usuario/editar', views.editar_usuario, name='editar-usuario'),

    path('aluno/', views.lista_aluno, name='alunos'),
    path('aluno/cadastro/', views.cadastro_aluno, name='cadastro-aluno'),
    path('aluno/<int:aluno_id>/editar', views.editar_aluno, name='editar-aluno'),
    path('aluno/<int:aluno_id>/deletar', views.delete_aluno, name='deletar-aluno'),

    path('turma/', views.lista_turma, name='turmas'),
    path('turma/cadastro/', views.cadastro_turma, name='cadastro-turma'),
    path('turma/<int:turma_id>/editar', views.editar_turma, name='editar-turma'),
    path('turma/<int:turma_id>/deletar', views.delete_turma, name='deletar-turma'),

    path('aula/', views.lista_aula, name='aulas'),
    path('aula/<int:aula_id>/deletar', views.delete_aula, name='deletar-aula'),
]