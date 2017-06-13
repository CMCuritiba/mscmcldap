# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory
from unittest.mock import patch, MagicMock, Mock
from ..models import VSetor, VPessoa
from django.db import IntegrityError, DataError
import os

class VSetorTestCase(TestCase):
	
	def setUp(self):
		super(VSetorTestCase, self).setUp()

	def test_v_setor_ok(self):
		vsetor = VSetor.objects.get(pk=171)
		self.assertEqual(vsetor.set_nome, 'Divisão de Desenvolvimento De Sistemas')


class VPessoaTestCase(TestCase):

	def test_view_v_pessoa_ok(self):
		vpessoa = VPessoa.objects.get(pk=2179)
		vsetor = VSetor.objects.get(pk=171)
		self.assertEqual(vpessoa.pes_nome, 'Alexandre Odoni')
		self.assertEqual(vpessoa.set_id, vsetor.set_id)