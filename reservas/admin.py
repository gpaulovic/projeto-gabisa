from django.contrib import admin
from .models import Reserva

class ReservaAdmin(admin.ModelAdmin):
    filter_horizontal = ('brinquedos',)  # Isso permite uma interface mais amigável para selecionar brinquedos

admin.site.register(Reserva, ReservaAdmin)
