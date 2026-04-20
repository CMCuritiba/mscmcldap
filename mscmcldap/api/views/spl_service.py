import datetime
from django.db import connection
from django.conf import settings
import logging

from mscmcldap.api.mocks.projetos_reuniao import get_projeto_mock, get_projeto_reuniao_mock, get_projetos_reuniao_mock, get_textos_conclusao_mock
from mscmcldap.api.mocks.reuniao import get_rec_id_mock, get_reuniao_mock
from mscmcldap.api.mocks.reuniao_comissao import get_comissao_mock, get_reunioes_mock, get_reunioes_range_mock
from mscmcldap.api.models import v_spl_conjunto_vereadores, v_spl_pauta_comissao, v_spl_reuniao_comissao
from mscmcldap.util.date_util import formataData

logger = logging.getLogger(__name__)

def get_reunioes_comissao():
    hoje = datetime.date.today()  # corrigido aqui 👈

    # --- Mock ---
    if settings.USE_MOCK:
        logger.info("Retornando dados mockados para reuniões de comissão")
        return get_reunioes_mock()

    # --- Real ---
    reunioes_json = []

    reunioes = v_spl_reuniao_comissao.objects.filter(rec_data=hoje)

    for c in reunioes:
        try:
            pauta = v_spl_pauta_comissao.objects.get(rec_id=c.rec_id)

            if pauta.pac_liberada:
                conjunto = v_spl_conjunto_vereadores.objects.get(con_id=c.con_id)

                reunioes_json.append({
                    'rec_id': c.rec_id,
                    'con_id': c.con_id,
                    'con_desc': conjunto.ini_nome,
                    'con_sigla': conjunto.con_sigla,
                    'rec_tipo_reuniao': c.rec_tipo_reuniao,
                    'rec_numero': c.rec_numero,
                    'versao': c.versao,
                    'rec_data': c.rec_data.strftime("%d/%m/%Y"),
                    'pac_id': pauta.pac_id
                })

        except v_spl_pauta_comissao.DoesNotExist:
            continue

    return reunioes_json

def get_projetos_reuniao(reuniao):
    # --- Mock ---
    if settings.USE_MOCK:
        logger.info("Retornando dados mockados para projetos de reunião")
        return get_projetos_reuniao_mock(reuniao)

    # --- Real ---
    projetos_json = []

    with connection.cursor() as c:  
        c.callproc("fn_remoto_projetos_reuniao", [reuniao])
        projetos = c.fetchall()

    for p in projetos:
        projetos_json.append({
            'pac_id': p[0],
            'par_id': p[1],
            'codigo_proposicao': p[2],
            'iniciativa': p[3],
            'sumula': p[4],
            'relator': p[5],
            'conclusao_relator': p[6],
            'conclusao_comissao': p[7],
            'tem_emendas': p[8],
        })

    return projetos_json

def get_reunioes_comissao_range(data_inicio, data_fim):
    inicio = formataData(data_inicio)
    fim = formataData(data_fim)

    # --- MOCK ---
    if settings.USE_MOCK:
        logger.info(f"Mock reuniões range: {data_inicio} - {data_fim}")
        return get_reunioes_range_mock(data_inicio, data_fim)

    # --- REAL ---
    reunioes_json = []

    queryset = v_spl_reuniao_comissao.objects.all()

    if inicio and fim:
        queryset = queryset.filter(rec_data__range=(inicio, fim))
    elif inicio:
        queryset = queryset.filter(rec_data__gte=inicio)
    elif fim:
        queryset = queryset.filter(rec_data__lte=fim)

    for c in queryset:
        try:
            pauta = v_spl_pauta_comissao.objects.get(rec_id=c.rec_id)

            if pauta.pac_liberada:
                conjunto = v_spl_conjunto_vereadores.objects.get(con_id=c.con_id)

                reunioes_json.append({
                    'rec_id': c.rec_id,
                    'con_id': c.con_id,
                    'con_desc': conjunto.ini_nome,
                    'con_sigla': conjunto.con_sigla,
                    'rec_tipo_reuniao': c.rec_tipo_reuniao,
                    'rec_numero': c.rec_numero,
                    'versao': c.versao,
                    'rec_data': c.rec_data.strftime("%d/%m/%Y"),
                    'pac_id': pauta.pac_id
                })

        except v_spl_pauta_comissao.DoesNotExist:
            continue

    return reunioes_json

def get_rec_id(pac_id):
    # --- MOCK ---
    if settings.USE_MOCK:
        logger.info(f"Mock rec_id para pac_id={pac_id}")
        return get_rec_id_mock(pac_id)

    # --- REAL ---
    try:
        pauta = v_spl_pauta_comissao.objects.get(pac_id=pac_id)
    except v_spl_pauta_comissao.DoesNotExist:
        return []

    return [{
        'rec_id': pauta.rec_id
    }]

def get_reuniao(rec_id):
    # --- MOCK ---
    if settings.USE_MOCK:
        logger.info(f"Mock reunião rec_id={rec_id}")
        reuniao = get_reuniao_mock(rec_id)
        return [reuniao] if reuniao else []

    # --- REAL ---
    try:
        reuniao = v_spl_reuniao_comissao.objects.get(rec_id=rec_id)
    except v_spl_reuniao_comissao.DoesNotExist:
        return []

    return [{
        'rec_id': reuniao.rec_id,
        'con_id': reuniao.con_id,
        'rec_tipo_reuniao': reuniao.rec_tipo_reuniao,
        'rec_numero': reuniao.rec_numero,
        'rec_data': reuniao.rec_data.strftime("%d/%m/%Y"),
    }]

def get_comissao(con_id):
    # --- MOCK ---
    if settings.USE_MOCK:
        logger.info(f"Mock comissão con_id={con_id}")
        comissao = get_comissao_mock(con_id)
        return [comissao] if comissao else []

    # --- REAL ---
    try:
        comissao = v_spl_conjunto_vereadores.objects.get(con_id=con_id)
    except v_spl_conjunto_vereadores.DoesNotExist:
        return []

    return [{
        'con_id': comissao.con_id,
        'ini_nome': comissao.ini_nome,
    }]

def get_textos_conclusao(pro_codigo):
    # --- MOCK ---
    if settings.USE_MOCK:
        logger.info(f"Mock textos conclusão pro_codigo={pro_codigo}")
        return get_textos_conclusao_mock(pro_codigo)

    # --- REAL ---
    textos_json = []

    with connection.cursor() as c:
        c.callproc("fn_remoto_texto_conclusao", [pro_codigo])
        textos = c.fetchall()

    for t in textos:
        textos_json.append({
            'pro_id': t[0],
            'pro_codigo': t[1],
            'par_id': t[2],
            'txt_data': t[3].strftime("%d/%m/%Y") if t[3] else None,
            'txt_finalizado': t[4],
            'txt_relator': t[5],
            'txt_id': t[6],
            'ver_id': t[7],
            'vereador': t[8],
            'tcp_id': t[9],
            'tcp_nome': t[10],
            'par_finalizado': t[11],
            'con_id': t[12],
        })

    return textos_json

def get_projeto(pac_id, par_id, codigo_proposicao):
    # --- MOCK ---
    if settings.USE_MOCK:
        logger.info("Retornando dados mockados para projeto")
        return get_projeto_mock(pac_id, par_id, codigo_proposicao)

    # --- REAL ---
    projetos_json = []

    with connection.cursor() as c:
        c.callproc("fn_remoto_projeto", [pac_id, par_id, codigo_proposicao])
        projetos = c.fetchall()

    for p in projetos:
        projetos_json.append({
          'pac_id': p[0],
          'par_id': p[1],
          'codigo_proposicao': p[2],
          'iniciativa': p[3],
          'sumula': p[4],
          'relator': p[5],
          'conclusao_relator': p[6],
          'conclusao_comissao': p[7],
          'tem_emendas': p[8],
        })

    return projetos_json

def get_projeto_reuniao(pac_id, par_id):
    # --- MOCK ---
    if settings.USE_MOCK:
        logger.info("Retornando dados mockados para projeto reunião")
        return get_projeto_reuniao_mock(pac_id, par_id)

    # --- REAL ---
    projetos_json = []

    with connection.cursor() as c:
        c.callproc("fn_remoto_projeto_reuniao", [pac_id, par_id])
        projetos = c.fetchall()

    for p in projetos:
        projetos_json.append({
          'pac_id': p[0],
          'par_id': p[1],
          'codigo_proposicao': p[2],
          'iniciativa': p[3],
          'sumula': p[4],
          'relator': p[5],
          'conclusao_relator': p[6],
          'conclusao_comissao': p[7],
          'tem_emendas': p[8],
        })

    return projetos_json