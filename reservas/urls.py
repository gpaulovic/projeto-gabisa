from django.urls import path
from .views import listar_reservas, detalhes_reserva, criar_reserva, editar_reserva, excluir_reserva

app_name = 'reservas'

urlpatterns = [
    path('', listar_reservas, name='listar_reservas'),
    path('<int:reserva_id>/', detalhes_reserva, name='detalhes_reserva'),
    path('criar/', criar_reserva, name='criar_reserva'),
    path('<int:reserva_id>/editar/', editar_reserva, name='editar_reserva'),
    path('<int:reserva_id>/excluir/', excluir_reserva, name='excluir_reserva'),
]
