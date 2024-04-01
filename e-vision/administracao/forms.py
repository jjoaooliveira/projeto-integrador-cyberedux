from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from sistema.models import Professor, Aluno, Turma


class FormCreationUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'is_staff',
        ]

class FormChangeUser(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'modalforminput form-control'}),
            'email': forms.EmailInput(attrs={'class': 'modalforminput form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'modalforminput form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'modalforminput form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'modalforminput form-check-input'}),
        }

class FormProfessor(forms.ModelForm):
    class Meta:
        model = Professor
        fields = [
            'user',
            'nome',
            'cpf',
            'email',
            'endereco',
            'telefone'
        ]

class FormAluno(forms.ModelForm):
    class Meta:
        model=Aluno
        fields = [
            'nome',
            'cpf',
            'email',
            'endereco',
            'telefone',
            'condicao_financeira',
            'escolaridade',
            'trabalha'
        ]

class FormTurma(forms.ModelForm):
    class Meta:
        model = Turma
        fields = [
            'periodo',
            'ano',
            'qtd_vagas',
            'disciplina',
            'professor',
            'alunos',
        ]
