from django import forms
from .models import Terapeuta


class TerapeutaForm(forms.ModelForm):
    class Meta:
        model = Terapeuta
        fields = ['nome', 'especialidades', 'usuario', 'ativo']
        labels = {
            'nome': 'Nome',
            'especialidades': 'Especialidades',
            'usuario': 'Usuário',
            'ativo': 'Ativo',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome completo do terapeuta', 'required': 'required'}),
            'especialidades': forms.TextInput(attrs={'placeholder': 'Digite a especialidade do terapeuta', 'required': 'required'}),
        }

        help_texts = {
            'nome': None,
            'especialidades': None
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].empty_label = "Escolha um usuário"
