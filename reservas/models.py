from django.db import models
from clientes.models import Cliente
from brinquedos.models import Brinquedo
from django.core.validators import MinValueValidator
from django.utils import timezone

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    brinquedos = models.ManyToManyField(Brinquedo)
    data_reserva = models.DateTimeField(default=timezone.now)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'Reserva de {self.cliente.nome} em {self.data_reserva}'
