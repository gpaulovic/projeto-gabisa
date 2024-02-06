from django.urls import path
from .views import cliente_list, cliente_detail

app_name = 'clientes'

urlpatterns = [
    
    # path('', listar_clientes, name='listar_clientes'),
    # path('<int:cliente_id>/', detalhes_cliente, name='detalhes_cliente'),
    # path('criar/', criar_cliente, name='criar_cliente'),
    # path('<int:cliente_id>/editar/', editar_cliente, name='editar_cliente'),
    # path('<int:cliente_id>/excluir/', excluir_cliente, name='excluir_cliente'), 

    # URLs para as APIs do seu aplicativo
    path('api/clientes/', cliente_list, name='cliente_list'),
    path('api/clientes/<int:pk>/', cliente_detail, name='cliente_detail'),
]
