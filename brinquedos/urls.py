from django.urls import path
from .views import listar_brinquedos, detalhes_brinquedo, criar_brinquedo, editar_brinquedo, excluir_brinquedo

app_name = 'brinquedos'

urlpatterns = [
    path('', listar_brinquedos, name='listar_brinquedos'),
    path('<int:brinquedo_id>/', detalhes_brinquedo, name='detalhes_brinquedo'),
    path('criar/', criar_brinquedo, name='criar_brinquedo'),
    path('<int:brinquedo_id>/editar/', editar_brinquedo, name='editar_brinquedo'),
    path('<int:brinquedo_id>/excluir/', excluir_brinquedo, name='excluir_brinquedo'),
]
