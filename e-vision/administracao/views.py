from django.contrib.admin.views.decorators import staff_member_required
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import FormAluno, FormProfessor, FormChangeUser, FormCreationUser, FormTurma
from sistema.models import Aluno, Aula, Disciplina, Professor, Turma 

@staff_member_required(login_url='login')
def portal(request):
    return render(request, 'portal.html')


# professor
@staff_member_required(login_url='login')
def lista_professor(request):

    professores = Professor.objects.all()
    form = FormProfessor()
    return render(request, 'lista-professor.html', {'professores': professores, 'form': form})


@staff_member_required(login_url='login')
def editar_professor(request, professor_id):
    professor = Professor.objects.get(pk=professor_id)
    
    if request.method == 'POST':
        form = FormProfessor(request.POST, instance=professor)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('professores')

    professores_usuarios = Professor.objects.values_list('user', flat=True)
    usuarios = User.objects.exclude(id__in=professores_usuarios).exclude(is_superuser=True)
    return render(request, 'editar-professor.html', {'professor': professor, 'usuarios': usuarios})


@staff_member_required(login_url='login')
def delete_professor(request, professor_id):
    professor = Professor.objects.get(pk=professor_id)
    professor.delete()
    return HttpResponseRedirect(reverse('professores'))

    
@staff_member_required(login_url='login')
def cadastro_professor(request):
    
    if request.method == 'POST':
        form = FormProfessor(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('professores')

    professores_usuarios = Professor.objects.values_list('user', flat=True)
    usuarios = User.objects.exclude(id__in=professores_usuarios).exclude(is_superuser=True)
    return render(request, 'cadastro-professor.html', {'usuarios': usuarios})


# Usuario
@staff_member_required(login_url='login')
def lista_usuario(request):

    usuarios = list(User.objects.all().values('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined'))
    
    form = FormChangeUser()
    return render(request, 'lista-usuario.html', {'usuarios': usuarios, 'form': form})


@staff_member_required(login_url='login')
def cadastro_usuario(request):

    if request.method == 'POST':
        form = FormCreationUser(request.POST)

        if form.is_valid():
            form.save()
                
            return HttpResponseRedirect(reverse('usuarios'))
        
    form = FormCreationUser()
    return render(request, 'cadastro-usuario.html', {'form': form})


@staff_member_required(login_url='login')
def editar_usuario(request):

    if request.method == 'POST':
        usuario = User.objects.get(pk=request.POST['id_user'])
        form = FormChangeUser(request.POST, instance = usuario)

        if form.is_valid:
            form.save()
            
        return HttpResponseRedirect(reverse('usuarios'))
  
    
# aluno
@staff_member_required(login_url='login')
def lista_aluno(request):
    alunos = Aluno.objects.all()
    return render(request, 'lista-aluno.html', {'alunos': alunos})


@staff_member_required(login_url='login')
def editar_aluno(request, aluno_id):
    aluno = Aluno.objects.get(pk=aluno_id)
    escolaridade = Aluno.Escolaridade.choices
    condicoes = Aluno.CondicaoFinanceira.choices
    form = FormAluno(request.POST or None, instance=aluno)
    
    if form.is_valid():
        form.save()
        return redirect('alunos')

    return render(request, 'editar-aluno.html', {'aluno': aluno, 'escolaridades': escolaridade, 'condicoes': condicoes})


@staff_member_required(login_url='login')
def cadastro_aluno(request):

    if request.method == 'POST':
        form = FormAluno(request.POST)

        if form.is_valid():
            form.save()
            return redirect('alunos')

    escolaridade = Aluno.Escolaridade.choices
    condicoes = Aluno.CondicaoFinanceira.choices
    return render(request, 'cadastro-aluno.html', {'escolaridades': escolaridade, 'condicoes': condicoes})


@staff_member_required(login_url='login')
def delete_aluno(request, aluno_id):
    
    aluno = Aluno.objects.get(pk=aluno_id)
    aluno.delete()
    return HttpResponseRedirect(reverse('alunos'))


# turma
@staff_member_required(login_url='login')
def cadastro_turma(request):
    
    if request.method == 'POST':
        form = FormTurma(request.POST)

        if form.is_valid():
            form.save()
            return redirect('turmas')

    disciplinas = Disciplina.objects.all()
    alunos = Aluno.objects.all()
    professores = Professor.objects.all()

    return render(request, 'cadastro-turma.html', {'disciplinas': disciplinas, 'alunos': alunos, 'professores': professores})


@staff_member_required(login_url='login')
def lista_turma(request):
    turmas = Turma.objects.all()
    return render(request, 'lista-turma.html', {'turmas': turmas})


@staff_member_required(login_url='login')
def editar_turma(request, turma_id):
    turma = Turma.objects.get(pk=turma_id)
    disciplinas = Disciplina.objects.exclude(id=turma.disciplina.id)
    professores = Professor.objects.exclude(id=turma.professor.id)
    turma_alunos = Turma.objects.filter(id=turma_id).values_list('alunos', flat=True)
    alunos = Aluno.objects.exclude(id_aluno__in=turma_alunos)
    form = FormTurma(request.POST or None, instance=turma)
 
    if form.is_valid():
        form.save()
        # messages.sucess()
        return redirect('turmas')

    return render(request, 'editar-turma.html', {'disciplinas': disciplinas, 'turma': turma, 'professores': professores, 'alunos': alunos})


@staff_member_required(login_url='login')
def delete_turma(request, turma_id):
    turma = Turma.objects.get(pk=turma_id)
    turma.delete()

    return HttpResponseRedirect(reverse('turmas'))


# aula
@staff_member_required(login_url='login')
def lista_aula(request):
    aulas = Aula.objects.all()
    return render(request, 'lista-aula.html', {'aulas': aulas})


@staff_member_required(login_url='login')
def delete_aula(request, aula_id):
    aula = Aula.objects.get(pk=aula_id)
    aula.delete()

    return HttpResponseRedirect(reverse('aulas'))
