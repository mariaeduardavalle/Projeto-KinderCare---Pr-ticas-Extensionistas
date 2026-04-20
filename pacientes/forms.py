from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'responsavel', 'contato', 'observacoes', 'terapeutas_responsaveis']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'terapeutas_responsaveis': forms.CheckboxSelectMultiple(),
        }
