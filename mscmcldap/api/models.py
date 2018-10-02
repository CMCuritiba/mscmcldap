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

#---------------------------------------------------------------------------------------------
# Model para a view V_CMCFUNCIONARIOS
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class v_cmcfuncionarios(models.Model):
	class Meta:
		managed = False
		db_table = "v_cmcfuncionarios"

	pessoa = models.IntegerField(primary_key=True)
	matricula = models.IntegerField()
	pes_nome = models.CharField(max_length=500)
	funcao = models.IntegerField(blank=True, null=True)
	set_id = models.IntegerField()
	ind_estagiario = models.IntegerField()

	def __unicode__(self):
		return self.pes_nome

	def __str__(self):
		return self.pes_nome				


#---------------------------------------------------------------------------------------------
# Model para a view V_SPL_REUNIAO_COMISSAO
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class v_spl_reuniao_comissao(models.Model):
	class Meta:
		managed = False
		db_table = "v_spl_reuniao_comissao"

	rec_id = models.IntegerField(primary_key=True)
	con_id = models.IntegerField()
	rec_tipo_reuniao = models.CharField(max_length=500)
	rec_numero = models.CharField(max_length=100)
	versao = models.IntegerField()
	rec_data = models.DateField()

	def __unicode__(self):
		return self.rec_tipo_reuniao

	def __str__(self):
		return self.rec_tipo_reuniao


#---------------------------------------------------------------------------------------------
# Model para a view V_CONJUNTO_VEREADORES
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class v_spl_conjunto_vereadores(models.Model):
	class Meta:
		managed = False
		db_table = "v_spl_conjunto_vereadores"

	con_id = models.IntegerField(primary_key=True)
	con_sigla = models.CharField(max_length=200)
	con_maximo = models.IntegerField(blank=True, null=True)
	ut_id = models.IntegerField()
	ini_nome = models.CharField(max_length=500)
	ini_ativa = models.BooleanField()
	tin_id = models.IntegerField()
	versao = models.IntegerField()
	ini_codigo_prefeitura = models.IntegerField()
	con_descricao = models.CharField(max_length=500)
	ini_nome = models.CharField(max_length=500)
	con_site_ordem = models.IntegerField()
	con_email = models.CharField(max_length=500)

	def __unicode__(self):
		return self.ini_nome

	def __str__(self):
		return self.ini_nome


#---------------------------------------------------------------------------------------------
# Model para a view V_PAUTA_COMISSAO
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class v_spl_pauta_comissao(models.Model):
	class Meta:
		managed = False
		db_table = "v_spl_pauta_comissao"

	pac_id = models.IntegerField(primary_key=True)
	rec_id = models.IntegerField()
	pac_liberada = models.BooleanField()
	pac_notificada = models.BooleanField()
	versao = models.IntegerField()

	def __unicode__(self):
		return self.pac_id

	def __str__(self):
		return self.pac_id


# ---------------------------------------------------------------------------------------------
# Model para a view V_VEREADOR
# ---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class v_spl_vereador(models.Model):
    class Meta:
        managed = False
        db_table = "v_spl_vereador"

    ver_id = models.IntegerField(primary_key=True)
    matricula = models.CharField(max_length=4)
    ver_sexo = models.CharField(max_length=1)
    ut_id = models.IntegerField()
    ini_nome = models.CharField(max_length=100)
    ini_ativa = models.BooleanField()
    ver_nome_completo = models.CharField(max_length=100)
    ini_codigo_prefeitura = models.IntegerField()
    ver_site = models.CharField(max_length=250)
    ver_biografia = models.TextField()
    ver_redes_sociais = models.CharField(max_length=250)
    ver_fone_principal = models.CharField(max_length=20)
    ver_fones = models.CharField(max_length=100)
    ver_legislaturas = models.CharField(max_length=100)
    ver_localizacao = models.CharField(max_length=50)
    ver_partido = models.CharField(max_length=100)
    arq_id = models.IntegerField()
    arq_id_biografia = models.IntegerField()

    def __unicode__(self):
        return self.ini_nome

    def __str__(self):
        return self.ini_nome


# ---------------------------------------------------------------------------------------------
# Model para a view V_CARGO_MESA
# ---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class v_spl_cargos_mesa(models.Model):
    class Meta:
        managed = False
        db_table = "v_spl_cargos_mesa"

    matricula = models.CharField(primary_key=True, max_length=4)
    ini_nome = models.CharField(max_length=100)
    crg_nome = models.CharField(max_length=50)
    crg_ordem = models.IntegerField()

    def __unicode__(self):
        return self.ini_nome

    def __str__(self):
        return self.ini_nome