from django.urls import path
from .views import reserva_list, reserva_detail

app_name = 'reservas'

urlpatterns = [
    path('api/reservas/', reserva_list, name='reserva_list'),
    path('api/reservas/<int:pk>/', reserva_detail, name='reserva_detail'),
]

