from django import forms
from sistema.models import Aula, Presenca

class FormAula(forms.ModelForm):
    class Meta:
        model = Aula
        fields = [
            'data',
        ]
        

class FormPresenca(forms.ModelForm):
    class Meta:
        model=Presenca
        fields = [
            'aluno',
            'presente',
        ]
