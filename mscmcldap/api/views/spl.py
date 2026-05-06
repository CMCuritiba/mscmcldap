# -*- coding: utf-8 -*-

import logging

from django.conf import settings
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import fields, serializers
from django.http import HttpResponse, JsonResponse
from django.db import connection
from rest_framework.decorators import api_view
import datetime

from mscmcldap.api.views.spl_service import get_reunioes_comissao, get_projetos_reuniao, get_reunioes_comissao_range, get_rec_id, get_reuniao, get_comissao, get_textos_conclusao, get_projeto, get_projeto_reuniao
from ...util.date_util import formataData
from ..models import v_spl_reuniao_comissao, v_spl_conjunto_vereadores, v_spl_pauta_comissao, v_spl_vereador, v_spl_cargos_mesa
from ..mocks.reuniao_comissao import get_comissao_mock, get_reunioes_mock, get_reunioes_range_mock
from ..mocks.reuniao import get_rec_id_mock, get_reuniao_mock
from ..mocks.projetos_reuniao import get_projeto_mock, get_projeto_reuniao_mock, get_projetos_reuniao_mock, get_textos_conclusao_mock

logger = logging.getLogger(__name__)


@api_view(['GET'])
def spl_reuniao_comissao(request):
    reunioes_json = []
    hoje = datetime.datetime.now()
    request.session.flush()

    dados = get_reunioes_comissao()

    return JsonResponse(dados, safe=False)

@api_view(['GET'])
def spl_projetos_reuniao(request, reuniao):
    dados = get_projetos_reuniao(reuniao)
    return JsonResponse(dados, safe=False)


@api_view(['GET'])
def spl_projeto_reuniao(request, pac_id, par_id):
    dados = get_projeto_reuniao(pac_id, par_id)
    return JsonResponse(dados, safe=False)

# ---------------------------------------------------------------------------------------------------
# api que retorna as reuniões dentro de um range de datas
# ---------------------------------------------------------------------------------------------------
@api_view(['GET'])
def spl_reuniao_comissao_range(request, data_inicio, data_fim):
    dados = get_reunioes_comissao_range(data_inicio, data_fim)
    return JsonResponse(dados, safe=False)

# ---------------------------------------------------------------------------------------------------
# api que retorna o rec_id a partir da pac_id
# ---------------------------------------------------------------------------------------------------
@api_view(['GET'])
def spl_get_rec_id(request, pac_id):
    dados = get_rec_id(pac_id)
    return JsonResponse(dados, safe=False)

# ---------------------------------------------------------------------------------------------------
# api que retorna os dados da reuniao atraves do rec_id
# ---------------------------------------------------------------------------------------------------
@api_view(['GET'])
def spl_get_reuniao(request, rec_id):
    dados = get_reuniao(rec_id)
    return JsonResponse(dados, safe=False)

# ---------------------------------------------------------------------------------------------------
# api que retorna os dados da reuniao atraves do rec_id
# ---------------------------------------------------------------------------------------------------
@api_view(['GET'])
def spl_get_comissao(request, con_id):
    dados = get_comissao(con_id)
    return JsonResponse(dados, safe=False)

# ---------------------------------------------------------------------------------------------------
# api que retorna o texto (e outras informações) do projeto
# ---------------------------------------------------------------------------------------------------
@api_view(['GET'])
def spl_textos_conclusao(request, pro_codigo):
    dados = get_textos_conclusao(pro_codigo)
    return JsonResponse(dados, safe=False)

# ---------------------------------------------------------------------------------------------------
# api que retorna os dados especificos do projeto
# ---------------------------------------------------------------------------------------------------
@api_view(['GET'])
def spl_projeto(request, pac_id, par_id, codigo_proposicao):
    dados = get_projeto(pac_id, par_id, codigo_proposicao)
    return JsonResponse(dados, safe=False)