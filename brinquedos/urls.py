from django.urls import path
from .views import brinquedo_list, brinquedo_detail

app_name = 'brinquedos'

urlpatterns = [
    path('api/brinquedos/', brinquedo_list, name='brinquedo_list'),
    path('api/brinquedos/<int:pk>/', brinquedo_detail, name='brinquedo_detail'),
]
