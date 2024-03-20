import json
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import FormAluno, FormProfessor, FormChangeUser, FormCreationUser, FormTurma
from sistema.models import Aluno, Aula, Professor, Turma 

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
    form = FormProfessor(request.POST or None, instance=professor)

    if form.is_valid():
        form.save()
        
        return HttpResponseRedirect(reverse('professores'))

    return render(request, 'editar-professor.html', {'form': form, 'professor': professor})


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
    
            return HttpResponseRedirect(reverse('professores'))

    form = FormProfessor()
    return render(request, 'cadastro-professor.html', {'form': form})

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
    form = FormAluno(request.POST or None, instance=aluno)
    
    if form.is_valid():
        form.save()
        print('oi')
        return redirect('alunos')

    return render(request, 'editar-aluno.html', {'aluno': aluno, 'form': form})


@staff_member_required(login_url='login')
def cadastro_aluno(request):

    if request.method == 'POST':
        form = FormAluno(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('alunos'))
        
    form = FormAluno()
    return render(request, 'cadastro-aluno.html', {'form': form})


@staff_member_required(login_url='login')
def delete_aluno(request, aluno_id):
    aluno = Aluno.objects.get(pk=aluno_id)
    aluno.delete()

    return HttpResponseRedirect(reverse('alunos'))


@staff_member_required(login_url='login')
# turma
def cadastro_turma(request):
    
    if request.method == 'POST':
        form = FormTurma(request.POST)
        if form.is_valid():
            form.save()
                
            return redirect('turmas')

    form = FormTurma()
    return render(request, 'cadastro-turma.html', {'form': form})


@staff_member_required(login_url='login')
def lista_turma(request):
    turmas = Turma.objects.all()
    return render(request, 'lista-turma.html', {'turmas': turmas})


@staff_member_required(login_url='login')
def editar_turma(request, turma_id):
    turma = Turma.objects.get(pk=turma_id)
    form = FormTurma(request.POST or None, instance=turma)
 
    if form.is_valid():
        form.save()
        # messages.sucess()
        return redirect('turmas')

    return render(request, 'editar-turma.html', {'form': form, 'turma': turma})


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
