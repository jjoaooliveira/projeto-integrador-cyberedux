from django import forms
from sistema.models import Aula, Presenca

class FormAula(forms.ModelForm):
    class Meta:
        model = Aula
        fields = [
            'professor',
            'data',
        ]
        widgets = {
            'professor': forms.Select(attrs={'class': 'form-select'}),
            'data': forms.DateInput(attrs={'class': 'form-control'}),
        }

class FormPresenca(forms.ModelForm):
    class Meta:
        model=Presenca
        fields = [
            'aluno',
            'presente',
        ]
