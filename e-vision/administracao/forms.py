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
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input mb-3'}),
        }


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
        widgets = {
            'user': forms.Select(attrs={'class': 'modalforminput form-select mb-3', 'readonly':'readonly'}),
            'nome': forms.TextInput(attrs={'class':'modalforminput form-control mb-3'}),
            'cpf': forms.TextInput(attrs={'class':'modalforminput form-control mb-3'}),
            'email': forms.TextInput(attrs={'class':'modalforminput form-control mb-3'}),
            'endereco': forms.TextInput(attrs={'class':'modalforminput form-control mb-3'}),
            'telefone': forms.TextInput(attrs={'class':'modalforminput form-control mb-3'}),
        }

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
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'cpf' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'endereco' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'telefone' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'condicao_financeira' : forms.RadioSelect(attrs={'class': 'mb-3'}, choices=Aluno.CondicaoFinanceira),
            'escolaridade' : forms.Select(attrs={'class': 'form-select mb-3'}, choices=Aluno.Escolaridade),
            }

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
        widgets = {
            'periodo': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'qtd_vagas': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'disciplina': forms.Select(attrs={'class':'form-select mb-3'}),
            'professor': forms.Select(attrs={'class':'form-select mb-3'}),
            'alunos': forms.SelectMultiple(attrs={'class':'form-select mb-3'}),
        }

