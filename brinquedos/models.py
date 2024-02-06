from django.db import models

class Brinquedo(models.Model):
    nome = models.CharField(max_length=100)
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
