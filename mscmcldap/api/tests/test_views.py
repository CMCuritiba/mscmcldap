# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from mscmcldap.api.models import v_setor, v_pessoa

class SetorAPITestCase(APITestCase):
	fixtures = ['inicial.json']

	def setUp(self):
		super(SetorAPITestCase, self).setUp()
		self.factory = APIRequestFactory()

	def test_retorna_setores_link_ok(self):
		response = self.client.get('/api/setores/')
		self.assertEqual(response.status_code, 200)

	def test_retorna_setores(self):
		response = self.client.get('/api/setores/')
		self.assertEqual(response.data[0]['set_nome'], 'Diretoria Geral')		

class PessoaAPITestCase(APITestCase):
	fixtures = ['inicial.json']

	def setUp(self):
		super(PessoaAPITestCase, self).setUp()
		self.factory = APIRequestFactory()

	def test_retorna_pessoas_setor_link_ok(self):
		response = self.client.get('/api/pessoas_setor/171/')
		self.assertEqual(response.status_code, 200)		

	def test_retorna_pessoa_link_ok(self):
		response = self.client.get('/api/pessoa/2179/')
		self.assertEqual(response.status_code, 200)		

	def test_retorna_pessoas_setor(self):
		response = self.client.get('/api/pessoas_setor/171/')
		self.assertEqual(response.data[0]['pes_nome'], 'Alexandre Odoni')		

	def test_retorna_pessoa(self):
		response = self.client.get('/api/pessoa/2179/')
		self.assertEqual(response.data['pes_nome'], 'Alexandre Odoni')		

	def test_retorna_pessoas_link_ok(self):
		response = self.client.get('/api/pessoas/')
		self.assertEqual(response.status_code, 200)		

	def test_retorna_pessoas(self):
		response = self.client.get('/api/pessoas/')
		self.assertEqual(response.data[0]['pes_nome'], 'Alexandre Odoni')

class CentroCustoAPITestCase(APITestCase):
	fixtures = ['inicial.json']

	def setUp(self):
		super(CentroCustoAPITestCase, self).setUp()
		self.factory = APIRequestFactory()		

	def test_retorna_centro_custo_link_ok(self):
		response = self.client.get('/api/centros_custo/')
		self.assertEqual(response.status_code, 200)				

	def test_retorna_centro_custo(self):
		response = self.client.get('/api/centros_custo/')
		self.assertEqual(response.data[0]['descricao'], 'Departamento de Administração e Finanças')

	def test_retorna_centro_custo_id(self):
		response = self.client.get('/api/centro_custo/4/')
		self.assertEqual(response.data['descricao'], 'Departamento de Administração e Finanças')

class ItemAPITestCase(APITestCase):
	fixtures = ['inicial.json']

	def setUp(self):
		super(ItemAPITestCase, self).setUp()
		self.factory = APIRequestFactory()		

	def test_retorna_item_link_ok(self):
		response = self.client.get('/api/itens/')
		self.assertEqual(response.status_code, 200)				

	def test_retorna_item(self):
		response = self.client.get('/api/itens/')
		self.assertEqual(response.data[0]['desc_item'], 'Lâmpada Suave 23w')		

	def test_retorna_item_id(self):
		response = self.client.get('/api/item/838/')
		self.assertEqual(response.data['desc_item'], 'Lâmpada Suave 23w')