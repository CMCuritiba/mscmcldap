# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

#---------------------------------------------------------------------------------------------
# Model para a view V_SETOR
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class v_setor(models.Model):
	class Meta:
		verbose_name_plural = 'Setores'
		managed = False
		db_table = "v_setor"

	set_id = models.IntegerField(primary_key=True)
	set_nome = models.CharField(max_length=500)
	set_sigla = models.CharField(max_length=100)
	set_id_superior = models.IntegerField(blank=True, null=True)
	set_ativo = models.BooleanField()
	set_tipo = models.CharField(max_length=1)

	def __unicode__(self):
		return self.set_nome

	def __str__(self):
		return self.set_nome

#---------------------------------------------------------------------------------------------
# Model para a view V_PESSOA
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class v_pessoa(models.Model):
	class Meta:
		verbose_name_plural = 'Pessoas'		
		managed = False
		db_table = "v_pessoa"

	pes_matricula = models.IntegerField(primary_key=True)
	pes_nome = models.CharField(max_length=500)
	set_id = models.IntegerField()

	def __unicode__(self):
		return self.pes_nome

	def __str__(self):
		return self.pes_nome
#---------------------------------------------------------------------------------------------
# Model para a view V_CENTRO_CUSTO
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class v_centro_custo(models.Model):
	class Meta:
		verbose_name_plural = 'Centros de Custo'		
		managed = False
		db_table = "v_centro_custo"

	centrocusto = models.IntegerField(primary_key=True)
	local = models.CharField(max_length=500, blank=True, null=True)
	descricao = models.CharField(max_length=500)
	ativoinativoai = models.CharField(max_length=1)
	codigoresponsavel = models.IntegerField()

	def __unicode__(self):
		return self.descricao

	def __str__(self):
		return self.descricao
#---------------------------------------------------------------------------------------------
# Model para a view V_ITEM
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class v_item(models.Model):
	class Meta:
		verbose_name_plural = 'Itens'		
		managed = False
		db_table = "v_item"

	item = models.IntegerField(primary_key=True)
	unidade = models.CharField(max_length=10)
	classificacao = models.CharField(max_length=10)
	desc_classificacao = models.CharField(max_length=500)
	desc_item = models.CharField(max_length=500)
	estocavel = models.CharField(max_length=1)
	ativoinativoai = models.CharField(max_length=1)
	valor = models.CharField(max_length=100, blank=True, null=True)
	ativo_classificacao = models.CharField(max_length=1)
	itememanalisesn = models.CharField(max_length=1)

	def __unicode__(self):
		return self.desc_item

	def __str__(self):
		return self.desc_item		

@python_2_unicode_compatible
class v_cmcfuncionarios(models.Model):
	class Meta:
		managed = False
		db_table = "v_cmcfuncionarios"

	pessoa = models.IntegerField(primary_key=True)
	matricula = models.IntegerField()
	pes_nome = models.CharField(max_length=500)
	funcao = models.IntegerField(blank=True, null=True)
	set_id = models.CharField(max_length=100)
	ind_estagiario = models.IntegerField()

	def __unicode__(self):
		return self.pes_nome

	def __str__(self):
		return self.pes_nome				

		