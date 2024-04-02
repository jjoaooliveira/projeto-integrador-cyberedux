from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('turma/<int:turma_id>', views.turma, name='turma'),
    path('turma/aluno/<int:aluno_id>', views.aluno, name='aluno'),
    path('turma/<int:turma_id>/presencas/', views.lista_presenca, name='presencas'),
    path('turma/<int:turma_id>/aulas/<int:aula_id>/presencas', views.cadastro_presenca, 
    name='cadastro-presenca'),
    path('turma/<int:turma_id>/presenca/<int:presenca_id>/delete', views.delete_presenca, name='deletar-presenca'),
    path('turma/<int:turma_id>/aulas/cadastro/', views.cadastro_aula, name='cadastro-aula'), 
    path('turma/<int:turma_id>/aulas/', views.lista_aulas, name='aulas'), 
    path('turma/<int:turma_id>/aulas/<int:aula_id>/editar', views.editar_aula, name='editar-aula'),
    path('turma/<int:turma_id>/presencas/<int:presenca_id>/editar', views.editar_presenca, name='editar-presenca'), 
]
