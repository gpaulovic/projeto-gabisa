from django.test import TestCase
from django.urls import reverse
from .models import Cliente
from .forms import ClienteForm

class ClienteModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome='Teste Nome',
            telefone='123456789',
            endereco='Endereço de Teste',
            cpf='123.456.789-09',
        )

    def test_cliente_str(self):
        self.assertEqual(str(self.cliente), 'Teste Nome')

class ClienteFormTest(TestCase):
    def test_criar_cliente_form_valid(self):
        form_data = {
            'nome': 'Teste Nome',
            'telefone': '123456789',
            'endereco': 'Endereço de Teste',
            'cpf': '123.456.789-09',
        }
        form = ClienteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_criar_cliente_form_invalid(self):
        form_data = {
            'nome': 'Teste Nome',
            'telefone': '123456789',
            'endereco': 'Endereço de Teste',
            'cpf': '123456789',  # CPF inválido
        }
        form = ClienteForm(data=form_data)
        self.assertFalse(form.is_valid())

class ClienteViewsTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome='Teste Nome',
            telefone='123456789',
            endereco='Endereço de Teste',
            cpf='123.456.789-09',
        )

    def test_listar_clientes_view(self):
        response = self.client.get(reverse('clientes:listar_clientes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Teste Nome')

    def test_detalhes_cliente_view(self):
        response = self.client.get(reverse('clientes:detalhes_cliente', args=[self.cliente.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Teste Nome')

    def test_criar_cliente_view(self):
        response = self.client.post(reverse('clientes:criar_cliente'), {
            'nome': 'Novo Cliente',
            'telefone': '987654321',
            'endereco': 'Novo Endereço',
            'cpf': '987.654.321-00',
        })
        self.assertEqual(response.status_code, 302)  # Redirecionado após a criação
        novo_cliente = Cliente.objects.get(nome='Novo Cliente')
        self.assertEqual(novo_cliente.telefone, '987654321')

    # Adicione mais testes conforme necessário, como para as views de edição e exclusão
