from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.shortcuts import get_object_or_404
from .models import Brinquedo

class BrinquedoAPITestCase(TestCase):
    def setUp(self):
        self.brinquedo = Brinquedo.objects.create(nome='Brinquedo Teste', preco_diaria='10.00')
        self.client = APIClient()

    def test_listar_brinquedos(self):
        url = reverse('brinquedos:brinquedo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detalhes_brinquedo(self):
        url = reverse('brinquedos:brinquedo_detail', args=[self.brinquedo.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Brinquedo Teste')

    def test_criar_brinquedo(self):
        url = reverse('brinquedos:brinquedo_list')
        data = {'nome': 'Novo Brinquedo', 'preco_diaria': '15.00'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Brinquedo.objects.count(), 2)

    def test_atualizar_brinquedo(self):
        url = reverse('brinquedos:brinquedo_detail', args=[self.brinquedo.id])
        data = {'nome': 'Brinquedo Atualizado', 'preco_diaria': '20.00'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.brinquedo.refresh_from_db()
        self.assertEqual(self.brinquedo.nome, 'Brinquedo Atualizado')

    def test_excluir_brinquedo(self):
        url = reverse('brinquedos:brinquedo_detail', args=[self.brinquedo.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Brinquedo.objects.count(), 0)
