from django import forms
from .models import Evolucao


class EvolucaoForm(forms.ModelForm):
    class Meta:
        model = Evolucao
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 6}),
        }
