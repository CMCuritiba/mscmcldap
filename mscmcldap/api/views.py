# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import fields, serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from .models import v_setor, v_pessoa, v_centro_custo, v_item

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

@api_view(['GET'])
def setores(request):
	setores = v_setor.objects.filter(set_ativo=True)
	serializer = SetorSerializer(setores, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def pessoas_setor(request, set_id):
	pessoas = v_pessoa.objects.filter(set_id=set_id)
	serializer = PessoaSerializer(pessoas, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def pessoa(request, pes_matricula):
	pessoa = v_pessoa.objects.get(pes_matricula=pes_matricula)
	serializer = PessoaSerializer(pessoa)
	return Response(serializer.data)

@api_view(['GET'])
def pessoas(request):
	pessoas = v_pessoa.objects.all()
	serializer = PessoaSerializer(pessoas, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def setor(request, pes_matricula):
	pessoa = v_pessoa.objects.filter(pes_matricula=pes_matricula).first()
	setor = v_setor.objects.filter(set_id=pessoa.set_id).first()
	serializer = SetorSerializer(setor, many=False)
	return Response(serializer.data)	

@api_view(['GET'])
def centros_custo(request):
	centros_custo = v_centro_custo.objects.filter(ativoinativoai='A').order_by('descricao')
	serializer = CentroCustoSerializer(centros_custo, many=True)
	return Response(serializer.data)		

@api_view(['GET'])
def centro_custo(request, centro_custo):
	centro_custo = v_centro_custo.objects.filter(centrocusto=centro_custo).first()
	serializer = CentroCustoSerializer(centro_custo, many=False)
	return Response(serializer.data)		

@api_view(['GET'])
def itens(request):
	itens = v_item.objects.filter(ativoinativoai='A').order_by('desc_item')
	serializer = ItemSerializer(itens, many=True)
	return Response(serializer.data)			

@api_view(['GET'])
def item(request, item_id):
	item = v_item.objects.filter(item=item_id).first()
	serializer = ItemSerializer(item, many=False)
	return Response(serializer.data)			