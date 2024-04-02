from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Aluno, Presenca, Professor, Turma, Aula
from .forms import FormAula, FormPresenca
# from django.contrib.auth.models import User


@login_required(login_url='login')
def home(request):
    usuario = request.user
    turmas = Turma.objects.filter(professor__user=usuario)
    return render(request, 'home.html', {'turmas': turmas})


@login_required(login_url='login')
def turma(request, turma_id):
    turma = Turma.objects.get(pk=turma_id)
    alunos = Aluno.objects.filter(turma__pk=turma_id)    
    return render(request, 'detalhes.html', {'alunos': alunos, 'turma': turma})   


@login_required(login_url='login')
def lista_presenca(request, turma_id):
    presencas = Presenca.objects.filter(aula__turma__id=turma_id)
    return render(request, 'presencas.html', {'presencas': presencas, 'turma': turma_id})


@login_required(login_url='login')
def cadastro_presenca(request, aula_id, turma_id):
   
    if request.method == "POST":
        form = FormPresenca(request.POST)

        if form.is_valid():
            presenca = Presenca(
                aula=Aula.objects.get(pk=aula_id),
                presente=form.cleaned_data['presente'],
                aluno = form.cleaned_data['aluno']
            )
            presenca.save()
            return HttpResponseRedirect(reverse('aulas', args=[turma_id]))
        
    form = FormPresenca()
    alunos_turma = Turma.objects.filter(id=turma_id).values_list('alunos', flat=True)
    alunos = Aluno.objects.filter(id_aluno__in=alunos_turma)
    return render(request, 'cadastro-presenca.html', {'alunos': alunos, 'turma': turma_id, 'aula': aula_id})


@login_required(login_url='login')
def editar_presenca(request, presenca_id, turma_id):
    presenca = Presenca.objects.get(pk=presenca_id)
    form = FormPresenca(request.POST or None, instance=presenca)

    if form.is_valid():
        aluno = Aluno.objects.get(pk=form.cleaned_data['aluno'].id_aluno),
        presenca.aluno= aluno[0]
        presenca.presente = form.cleaned_data['presente']
        presenca.save()
        return HttpResponseRedirect(reverse('presencas', args=[turma_id]))

    alunos_turma = Turma.objects.filter(id=turma_id).values_list('alunos', flat=True)
    alunos = Aluno.objects.filter(id_aluno__in=alunos_turma).exclude(id_aluno=presenca.aluno.id_aluno)
    return render(request, 'editar-presenca.html', {'alunos': alunos, 'turma': turma_id, 'presenca': presenca})


@login_required(login_url='login')
def delete_presenca(request, presenca_id, turma_id):
    presenca = Presenca.objects.get(pk=presenca_id)
    presenca.delete()
    return HttpResponseRedirect(reverse('presencas', args=[turma_id]))


def aluno(request, aluno_id):
    aluno = Aluno.objects.get(pk=aluno_id)
    return render(request, 'aluno.html', {'aluno': aluno})


@login_required(login_url='login')
def cadastro_aula(request, turma_id):
    
    if request.method == 'POST':
        form = FormAula(request.POST)

        if form.is_valid():
            aula = Aula(
                turma=Turma.objects.get(pk=turma_id),
                professor=Professor.objects.get(user=request.user),
                data=form.cleaned_data['data']
            )
            aula.save()
            return HttpResponseRedirect(reverse('aulas', args=[turma_id]))

    form = FormAula()
    return render(request, 'cadastro-aula.html', {'form': form, 'turma': turma_id})


@login_required(login_url='login')
def lista_aulas(request, turma_id):
    aulas = Aula.objects.filter(turma=turma_id)
    return render(request, 'aulas.html', {'aulas': aulas, 'turma': turma_id})


@login_required(login_url='login')
def editar_aula(request, aula_id, turma_id):
    aula = Aula.objects.get(pk=aula_id)
    data = aula.data.strftime("%Y-%m-%d")
    form = FormAula(request.POST or None, instance=aula)

    if form.is_valid():
        aula = form.save()
        return redirect(reverse('aulas', args=[turma_id]))

    return render(request, 'editar-aula.html', {'turma': turma_id, 'aula': aula, 'data': data})