from django.db import models
from django.utils import timezone
from brinquedos.models import Brinquedo
from clientes.models import Cliente
from django.core.validators import MinValueValidator
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    brinquedos = models.ManyToManyField(Brinquedo, blank=True)
    data_reserva = models.DateTimeField(default=timezone.now)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], null=True, blank=True)

    def __str__(self):
        return f'Reserva de {self.cliente.nome} em {self.data_reserva}'

    def save(self, *args, **kwargs):
        if not self.pk:  # Se a instância ainda não foi salva
            super().save(*args, **kwargs)  # Salva a reserva primeiro para obter um ID
        else:
            super().save(*args, **kwargs)

    def calcular_valor_total(self):
        self.valor_total = sum(brinquedo.preco_diaria for brinquedo in self.brinquedos.all())
        self.save(update_fields=['valor_total'])

@receiver(m2m_changed, sender=Reserva.brinquedos.through)
def atualizar_valor_total_reserva(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.calcular_valor_total()
