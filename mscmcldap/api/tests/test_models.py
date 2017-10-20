# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory
from unittest.mock import patch, MagicMock, Mock
from ..models import v_setor, v_pessoa, v_centro_custo, v_item
from django.db import IntegrityError, DataError
import os

class VSetorTestCase(TestCase):
	fixtures = ['inicial.json']

	def setUp(self):
		super(VSetorTestCase, self).setUp()

	def test_v_setor_ok(self):
		vsetor = v_setor.objects.get(pk=171)
		self.assertEqual(vsetor.set_nome, 'Divisão de Desenvolvimento De Sistemas')


class VPessoaTestCase(TestCase):
	fixtures = ['inicial.json']

	def test_view_v_pessoa_ok(self):
		vpessoa = v_pessoa.objects.get(pk=2179)
		vsetor = v_setor.objects.get(pk=171)
		self.assertEqual(vpessoa.pes_nome, 'Alexandre Odoni')
		self.assertEqual(vpessoa.set_id, vsetor.set_id)

class VCentroCustoTestCase(TestCase):
	fixtures = ['inicial.json']

	def test_view_v_centro_custo_ok(self):
		vcentrocusto = v_centro_custo.objects.get(pk=4)
		self.assertEqual(vcentrocusto.descricao, 'Departamento de Administração e Finanças')

class VCentroCustoTestCase(TestCase):
	fixtures = ['inicial.json']

	def test_view_v_centro_custo_ok(self):
		vitem = v_item.objects.get(pk=838)
		self.assertEqual(vitem.desc_item, "Lâmpada Suave 23w")		