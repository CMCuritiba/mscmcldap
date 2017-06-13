# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory
from unittest.mock import patch, MagicMock, Mock
from ..models import v_setor, v_pessoa
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