from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.shortcuts import get_object_or_404
from clientes.models import Cliente
from brinquedos.models import Brinquedo
from .models import Reserva

class ReservaAPITestCase(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nome='Cliente Teste', telefone='123456789', endereco='Endereço Teste', cpf='12345678901')
        self.brinquedo = Brinquedo.objects.create(nome='Brinquedo Teste', preco_diaria='10.00')
        self.reserva = Reserva.objects.create(cliente=self.cliente)
        self.client = APIClient()

    def test_listar_reservas(self):
        url = reverse('reservas:reserva_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detalhes_reserva(self):
        url = reverse('reservas:reserva_detail', args=[self.reserva.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('cliente', response.data)
        cliente_id = response.data['cliente']
        cliente = Cliente.objects.get(id=cliente_id)
        self.assertEqual(cliente.nome, 'Cliente Teste')

    def test_criar_reserva(self):
        url = reverse('reservas:reserva_list')
        data = {'cliente': self.cliente.id, 'brinquedos': [self.brinquedo.id]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reserva.objects.count(), 2)

    def test_atualizar_reserva(self):
        url = reverse('reservas:reserva_detail', args=[self.reserva.id])
        data = {'cliente': self.cliente.id, 'brinquedos': [self.brinquedo.id]}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.reserva.refresh_from_db()
        self.assertEqual(self.reserva.brinquedos.count(), 1)

    def test_excluir_reserva(self):
        url = reverse('reservas:reserva_detail', args=[self.reserva.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reserva.objects.count(), 0)
