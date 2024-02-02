from django import forms
from .models import Brinquedo

class BrinquedoForm(forms.ModelForm):
    class Meta:
        model = Brinquedo
        fields = ['nome', 'descricao', 'preco_diaria']
