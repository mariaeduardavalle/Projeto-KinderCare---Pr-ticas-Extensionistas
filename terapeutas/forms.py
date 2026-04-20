from django import forms
from .models import Terapeuta


class TerapeutaForm(forms.ModelForm):
    class Meta:
        model = Terapeuta
        fields = ['nome', 'especialidades', 'usuario', 'ativo']
        widgets = {
            'especialidades': forms.CheckboxSelectMultiple(),
        }
