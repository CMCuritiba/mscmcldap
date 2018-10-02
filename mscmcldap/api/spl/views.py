# -*- coding: utf-8 -*-


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import fields, serializers
from django.http import HttpResponse, JsonResponse
from django.db import connection
from rest_framework.decorators import api_view
import datetime
from mscmcldap.util.date_util import formataData

from ...api.spl.models import v_spl_reuniao_comissao, v_spl_conjunto_vereadores, v_spl_pauta_comissao, v_spl_vereador, v_spl_cargos_mesa


class VereadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = v_spl_vereador
        fields = ('ver_id', 'matricula', 'ver_sexo', 'ut_id', 'ini_nome', 'ini_ativa', 'ver_nome_completo',
                  'ini_codigo_prefeitura', 'ver_site', 'ver_biografia', 'ver_redes_sociais', 'ver_fone_principal',
                  'ver_fones', 'ver_legislaturas', 'ver_localizacao', 'ver_partido', 'arq_id', 'arq_id_biografia')


class CargosMesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = v_spl_cargos_mesa
        fields = ('matricula', 'ini_nome', 'crg_nome', 'crg_ordem')


@api_view(['GET'])
def spl_reuniao_comissao(request):
    reunioes_json = []
    hoje = datetime.datetime.now()
    # hoje = datetime.date(2018,9,5)

    reunioes = v_spl_reuniao_comissao.objects.filter(rec_data=hoje)
    for c in reunioes:
        pauta = v_spl_pauta_comissao.objects.get(rec_id=c.rec_id)
        if pauta.pac_liberada:
            conjunto = v_spl_conjunto_vereadores.objects.get(con_id=c.con_id)
            e_json = {}
            e_json['rec_id'] = c.rec_id
            e_json['con_id'] = c.con_id
            e_json['con_desc'] = conjunto.ini_nome
            e_json['con_sigla'] = conjunto.con_sigla
            e_json['rec_tipo_reuniao'] = c.rec_tipo_reuniao
            e_json['rec_numero'] = c.rec_numero
            e_json['versao'] = c.versao
            e_json['rec_data'] = c.rec_data.strftime("%d/%m/%Y")
            e_json['pac_id'] = pauta.pac_id
            reunioes_json.append(e_json)

    return JsonResponse(reunioes_json, safe=False)


@api_view(['GET'])
def spl_projetos_reuniao(request, reuniao):
    projetos_json = []
    c = connection.cursor()
    c.callproc("fn_remoto_projetos_reuniao", [reuniao, ])
    projetos = c.fetchall()
    c.close()
    for p in projetos:
        e_json = {}
        e_json['pac_id'] = p[0]
        e_json['par_id'] = p[1]
        e_json['codigo_proposicao'] = p[2]
        e_json['iniciativa'] = p[3]
        e_json['sumula'] = p[4]
        e_json['relator'] = p[5]
        e_json['conclusao_relator'] = p[6]
        e_json['conclusao_comissao'] = p[7]
        e_json['tem_emendas'] = p[8]
        projetos_json.append(e_json)
    return JsonResponse(projetos_json, safe=False)


@api_view(['GET'])
def spl_projeto_reuniao(request, pac_id, par_id):
    projetos_json = []
    c = connection.cursor()
    c.callproc("fn_remoto_projeto_reuniao", [pac_id, par_id, ])
    projetos = c.fetchall()
    c.close()
    for p in projetos:
        e_json = {}
        e_json['pac_id'] = p[0]
        e_json['par_id'] = p[1]
        e_json['codigo_proposicao'] = p[2]
        e_json['iniciativa'] = p[3]
        e_json['sumula'] = p[4]
        e_json['relator'] = p[5]
        e_json['conclusao_relator'] = p[6]
        e_json['conclusao_comissao'] = p[7]
        e_json['tem_emendas'] = p[8]
        projetos_json.append(e_json)
    return JsonResponse(projetos_json, safe=False)


# ---------------------------------------------------------------------------------------------------
# api que retorna as reuniões dentro de um range de datas
# ---------------------------------------------------------------------------------------------------
@api_view(['GET'])
def spl_reuniao_comissao_range(request, data_inicio, data_fim):
    reunioes_json = []

    inicio = formataData(data_inicio)
    fim = formataData(data_fim)

    if fim is not None:
        reunioes = v_spl_reuniao_comissao.objects.filter(rec_data__range=(inicio, fim))
    elif inicio is not None:
        reunioes = v_spl_reuniao_comissao.objects.filter(rec_data__gte=inicio)
    for c in reunioes:
        pauta = v_spl_pauta_comissao.objects.get(rec_id=c.rec_id)
        if pauta.pac_liberada:
            conjunto = v_spl_conjunto_vereadores.objects.get(con_id=c.con_id)
            e_json = {}
            e_json['rec_id'] = c.rec_id
            e_json['con_id'] = c.con_id
            e_json['con_desc'] = conjunto.ini_nome
            e_json['con_sigla'] = conjunto.con_sigla
            e_json['rec_tipo_reuniao'] = c.rec_tipo_reuniao
            e_json['rec_numero'] = c.rec_numero
            e_json['versao'] = c.versao
            e_json['rec_data'] = c.rec_data.strftime("%d/%m/%Y")
            e_json['pac_id'] = pauta.pac_id
            reunioes_json.append(e_json)

    return JsonResponse(reunioes_json, safe=False)


@api_view(['GET'])
def spl_vereadores(request):
    vereadores = v_spl_vereador.objects.all().order_by('ini_nome')
    serializer = VereadorSerializer(vereadores, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def spl_vereador_matricula(request, matricula):
    vereador = None
    try:
        vereador = v_spl_vereador.objects.get(matricula=matricula)
        serializer = VereadorSerializer(vereador, many=False)
        return Response(serializer.data)
    except vereador.DoesNotExist:
        raise Http404


@api_view(['GET'])
def spl_cargos_mesa(request):
    cargos_mesa = v_spl_cargos_mesa.objects.all().order_by('crg_ordem')
    serializer = CargosMesaSerializer(cargos_mesa, many=True)
    return Response(serializer.data)


# ---------------------------------------------------------------------------------------------------
# api que retorna o rec_id a partir da pac_id
# ---------------------------------------------------------------------------------------------------
@api_view(['GET'])
def spl_get_rec_id(request, pac_id):
    pauta_json = []
    e_json = {}
    try:
        pauta = v_spl_pauta_comissao.objects.get(pac_id=pac_id)
    except:
        pauta = None
    if pauta is not None:
        e_json['rec_id'] = pauta.rec_id
        pauta_json.append(e_json)
    return JsonResponse(pauta_json, safe=False)


# ---------------------------------------------------------------------------------------------------
# api que retorna os dados da reuniao atraves do rec_id
# ---------------------------------------------------------------------------------------------------
@api_view(['GET'])
def spl_get_reuniao(request, rec_id):
    reuniao_json = []
    e_json = {}
    try:
        reuniao = v_spl_reuniao_comissao.objects.get(rec_id=rec_id)
    except:
        reuniao = None
    if reuniao is not None:
        e_json['rec_id'] = reuniao.rec_id
        e_json['con_id'] = reuniao.con_id
        e_json['rec_tipo_reuniao'] = reuniao.rec_tipo_reuniao
        e_json['rec_numero'] = reuniao.rec_numero
        reuniao_json.append(e_json)
    return JsonResponse(reuniao_json, safe=False)


# ---------------------------------------------------------------------------------------------------
# api que retorna os dados da reuniao atraves do rec_id
# ---------------------------------------------------------------------------------------------------
@api_view(['GET'])
def spl_get_comissao(request, con_id):
    comissao_json = []
    e_json = {}
    try:
        comissao = v_spl_conjunto_vereadores.objects.get(con_id=con_id)
    except:
        comissao = None
    if comissao is not None:
        e_json['con_id'] = comissao.con_id
        e_json['ini_nome'] = comissao.ini_nome
        comissao_json.append(e_json)
    return JsonResponse(comissao_json, safe=False)

