from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.shortcuts import get_object_or_404  # Adicione esta linha
from .models import Cliente

class ClienteAPITestCase(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nome='Cliente de Teste', telefone='123456789', endereco='Rua Teste', cpf='12345678901')
        self.client = APIClient()

    def test_listar_clientes(self):
        url = reverse('clientes:cliente_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detalhes_cliente(self):
        url = reverse('clientes:cliente_detail', args=[self.cliente.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Cliente de Teste')

    def test_criar_cliente(self):
        url = reverse('clientes:cliente_list')
        data = {'nome': 'Novo Cliente', 'telefone': '987654321', 'endereco': 'Rua Nova', 'cpf': '10987654321'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 2)

    def test_atualizar_cliente(self):
        url = reverse('clientes:cliente_detail', args=[self.cliente.id])
        data = {'nome': 'Cliente Atualizado', 'telefone': '987654321', 'endereco': 'Rua Atualizada', 'cpf': '12345678901'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.nome, 'Cliente Atualizado')

    def test_excluir_cliente(self):
        url = reverse('clientes:cliente_detail', args=[self.cliente.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cliente.objects.count(), 0)
