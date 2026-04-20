from django import forms
from .models import AgendaSemanal, Atendimento


class AgendaSemanalForm(forms.ModelForm):
    class Meta:
        model = AgendaSemanal
        fields = ['paciente', 'terapeuta', 'tipo_terapia', 'dia_semana', 'horario', 'ativo']
        widgets = {
            'horario': forms.TimeInput(attrs={'type': 'time'}),
        }


class PresencaForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['status_presenca', 'observacao_presenca']


class AtendimentoExtraForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['paciente', 'terapeuta', 'tipo_terapia', 'data', 'horario', 'observacao_presenca']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'}),
        }
