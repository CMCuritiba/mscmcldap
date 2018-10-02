# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory
from unittest.mock import patch, MagicMock, Mock
from ..models import v_setor, v_pessoa, v_centro_custo, v_item, v_cmcfuncionarios
from ...api.spl.models import v_spl_reuniao_comissao, v_spl_conjunto_vereadores, v_spl_pauta_comissao, v_spl_vereador, v_spl_cargos_mesa
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


class VCMCFuncionarios(TestCase):
	fixtures = ['inicial.json']

	def test_view_v_cmcfuncionarios(self):
		funcionario = v_cmcfuncionarios.objects.get(pk=5336)
		self.assertEqual(funcionario.pes_nome, "KARINE MARINS")				

class VSPLReuniaoComissao(TestCase):
	fixtures = ['inicial.json']

	def test_view_v_spl_reuniao_comissao(self):
		reuniao = v_spl_reuniao_comissao.objects.get(pk=3)
		self.assertEqual(reuniao.con_id, 699)						

class VSPLConjuntoVereadores(TestCase):
	fixtures = ['inicial.json']

	def test_view_v_spl_conjunto_vereadores(self):
		conjunto = v_spl_conjunto_vereadores.objects.get(pk=1)
		self.assertEqual(conjunto.con_sigla, "C.Executiva")								

class VSPLPautaComissao(TestCase):
	fixtures = ['inicial.json']

	def test_view_v_spl_pauta_comissao(self):
		pauta = v_spl_pauta_comissao.objects.get(pk=1)
		self.assertEqual(pauta.rec_id, 1806)


class VSPLVereador(TestCase):
	fixtures = ['inicial.json']

	def test_view_v_spl_vereador(self):
		vereador = v_spl_vereador.objects.get(pk=5)
		self.assertEqual(vereador.matricula, "1097")


class VSPLCargosMesa(TestCase):
	fixtures = ['inicial.json']

	def test_view_v_spl_cargos_mesa(self):
		cargos_mesa = v_spl_cargos_mesa.objects.get(pk="1094")
		self.assertEqual(cargos_mesa.ini_nome, "Sergio R. B. Balaguer (Serginho do Posto)")