# -*- coding: utf-8 -*-

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import fields, serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from .models import v_setor, v_pessoa, v_centro_custo, v_item, v_cmcfuncionarios

class SetorSerializer(serializers.ModelSerializer):
	class Meta:
		model = v_setor
		fields = ('set_id', 'set_nome', 'set_sigla', 'set_id_superior', 'set_ativo', 'set_tipo')

class PessoaSerializer(serializers.ModelSerializer):
	class Meta:
		model = v_pessoa
		fields = ('pes_matricula', 'pes_nome', 'set_id')		

class CentroCustoSerializer(serializers.ModelSerializer):
	class Meta:
		model = v_centro_custo
		fields = ('centrocusto', 'local', 'descricao', 'ativoinativoai', 'codigoresponsavel')				

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = v_item
		fields = ('item', 'unidade', 'classificacao', 'desc_classificacao', 'desc_item', 'estocavel', 'ativoinativoai', 'valor', 'ativo_classificacao', 'itememanalisesn')						

class FuncionarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = v_cmcfuncionarios
		fields = ('matricula', 'pessoa', 'pes_nome', 'funcao', 'set_id', 'ind_estagiario')								


@api_view(['GET'])
def setores(request):
	setores = v_setor.objects.filter(set_ativo=True).order_by('set_nome')
	serializer = SetorSerializer(setores, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def pessoas_setor(request, set_id):
	pessoas = v_pessoa.objects.filter(set_id=set_id)
	serializer = PessoaSerializer(pessoas, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def pessoa(request, pes_matricula):
	print('------------------1')
	pessoa = v_pessoa.objects.get(pes_matricula=pes_matricula)
	print(pessoa)
	print('------------------2')
	serializer = PessoaSerializer(pessoa)
	return Response(serializer.data)

@api_view(['GET'])
def pessoas(request):
	pessoas = v_pessoa.objects.all()
	serializer = PessoaSerializer(pessoas, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def setor(request, pes_matricula):
	try:
		pessoa = v_pessoa.objects.get(pes_matricula=pes_matricula)
		setor = v_setor.objects.get(set_id=pessoa.set_id)
		serializer = SetorSerializer(setor, many=False)
		return Response(serializer.data)		
	except setor.DoesNotExist:
		raise Http404
		
@api_view(['GET'])
def centros_custo(request):
	centros_custo = v_centro_custo.objects.filter(ativoinativoai='A').order_by('descricao')
	serializer = CentroCustoSerializer(centros_custo, many=True)
	return Response(serializer.data)		

@api_view(['GET'])
def centro_custo(request, centro_custo):
	try:
		centro_custo = v_centro_custo.objects.get(centrocusto=centro_custo)
		serializer = CentroCustoSerializer(centro_custo, many=False)
		return Response(serializer.data)		
	except centro_custo.DoesNotExist:
		raise Http404

@api_view(['GET'])
def itens(request):
	itens = v_item.objects.filter(ativoinativoai='A').order_by('desc_item')
	serializer = ItemSerializer(itens, many=True)
	return Response(serializer.data)			

@api_view(['GET'])
def item(request, item_id):
	try:
		item = v_item.objects.get(item=item_id)
		serializer = ItemSerializer(item, many=False)
		return Response(serializer.data)			
	except item.DoesNotExist:
		raise Http404

@api_view(['GET'])
def setor_setor(request, set_id):
	try:
		setor = v_setor.objects.get(set_id=set_id)
		serializer = SetorSerializer(setor, many=False)
		return Response(serializer.data)		
	except setor.DoesNotExist:
		raise Http404


@api_view(['GET'])
def funcionarios(request):
	funcionarios = v_cmcfuncionarios.objects.all().order_by('pes_nome')
	serializer = FuncionarioSerializer(funcionarios, many=True)
	return Response(serializer.data)			

@api_view(['GET'])
def funcionarios_setor(request, set_id):
	funcionarios = v_cmcfuncionarios.objects.filter(set_id=set_id).order_by('pes_nome')
	serializer = FuncionarioSerializer(funcionarios, many=True)
	return Response(serializer.data)				

@api_view(['GET'])
def funcionario(request, pessoa):
	try:
		funcionario = v_cmcfuncionarios.objects.get(pessoa=pessoa)
		serializer = FuncionarioSerializer(funcionario, many=False)
		return Response(serializer.data)		
	except funcionario.DoesNotExist:
		raise Http404	

@api_view(['GET'])
def funcionario_matricula(request, matricula):
	try:
		funcionario = v_cmcfuncionarios.objects.get(matricula=matricula)
		serializer = FuncionarioSerializer(funcionario, many=False)
		return Response(serializer.data)		
	except funcionario.DoesNotExist:
		raise Http404			