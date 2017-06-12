# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from mscmcldap.api.models import VSetor, VPessoa

class SetorAPITestCase(APITestCase):
	fixtures = ['vsetor.json']

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
	fixtures = ['vpessoa.json']

	def setUp(self):
		super(PessoaAPITestCase, self).setUp()
		self.factory = APIRequestFactory()

	def test_retorna_pessoas_link_ok(self):
		response = self.client.get('/api/pessoas/171/')
		self.assertEqual(response.status_code, 200)		

	def test_retorna_pessoa_link_ok(self):
		response = self.client.get('/api/pessoa/2179/')
		self.assertEqual(response.status_code, 200)		

	def test_retorna_pessoas(self):
		response = self.client.get('/api/pessoas/171/')
		self.assertEqual(response.data[0]['pes_nome'], 'Alexandre Odoni')		

	def test_retorna_pessoa(self):
		response = self.client.get('/api/pessoa/2179/')
		self.assertEqual(response.data['pes_nome'], 'Alexandre Odoni')		