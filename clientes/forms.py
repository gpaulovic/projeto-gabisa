from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'endereco', 'cpf']

        widgets = {
            'cpf': forms.TextInput(attrs={'data-mask': '000.000.000-00'}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        # Adicione suas validações personalizadas, se necessário
        return cpf
