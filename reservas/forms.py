from django import forms
from .models import Reserva
from brinquedos.models import Brinquedo

class ReservaForm(forms.ModelForm):
    brinquedos = forms.ModelMultipleChoiceField(
        queryset=Brinquedo.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Reserva
        fields = ['cliente', 'brinquedos', 'data_reserva', 'valor_total']
