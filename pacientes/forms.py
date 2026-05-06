from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        input_formats=['%Y-%m-%d', '%d/%m/%Y'],
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'responsavel',
                  'contato', 'observacoes', 'cid']
        labels = {
            'nome': 'Nome',
            'data_nascimento': 'Data de Nascimento',
            'responsavel': 'Responsável Legal',
            'contato': 'Telefone de Contato',
            'observacoes': 'Informações Adicionais / Quadro Clínico',
            'cid': 'CID',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome completo do paciente', 'required': 'required'}),
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'responsavel': forms.TextInput(attrs={'placeholder': 'Digite o nome completo do responsável', 'required': 'required'}),
            'contato': forms.DateInput(attrs={'type': 'tel', 'placeholder': '(00) 00000-0000', 'pattern': '[0-9]*'}),
            'observacoes': forms.Textarea(attrs={'rows': 4}),
            'cid': forms.TextInput(attrs={'placeholder': 'Digite o CID do paciente', 'required': 'required'}),
        }
