# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import fields, serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from .models import v_setor, v_pessoa

class SetorSerializer(serializers.ModelSerializer):
	class Meta:
		model = v_setor
		fields = ('set_id', 'set_nome', 'set_sigla', 'set_id_superior', 'set_ativo', 'set_tipo')

class PessoaSerializer(serializers.ModelSerializer):
	class Meta:
		model = v_pessoa
		fields = ('pes_matricula', 'pes_nome', 'set_id')		

@api_view(['GET'])
def setores(request):
	setores = v_setor.objects.all().filter(set_ativo=True)
	serializer = SetorSerializer(setores, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def pessoas(request, set_id):
	pessoas = v_pessoa.objects.all().filter(set_id=set_id)
	serializer = PessoaSerializer(pessoas, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def pessoa(request, pes_matricula):
	pessoa = v_pessoa.objects.get(pes_matricula=pes_matricula)
	serializer = PessoaSerializer(pessoa)
	return Response(serializer.data)