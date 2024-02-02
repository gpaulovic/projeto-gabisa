from django.urls import path
from .views import listar_clientes, detalhes_cliente, criar_cliente, editar_cliente, excluir_cliente

app_name = 'clientes'

urlpatterns = [
    path('', listar_clientes, name='listar_clientes'),
    path('<int:cliente_id>/', detalhes_cliente, name='detalhes_cliente'),
    path('criar/', criar_cliente, name='criar_cliente'),
    path('<int:cliente_id>/editar/', editar_cliente, name='editar_cliente'),
    path('<int:cliente_id>/excluir/', excluir_cliente, name='excluir_cliente'),
]