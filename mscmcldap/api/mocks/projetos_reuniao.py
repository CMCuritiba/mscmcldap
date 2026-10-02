from datetime import datetime

from .data import PROJETOS_REUNIAO, TEXTOS_CONCLUSAO

def get_projetos_reuniao_mock(pac_id):
    pac_id = int(pac_id)
    projetos = [
        {
            'pac_id': p['pac_id'],
            'par_id': p['par_id'],
            'codigo_proposicao': p['codigo_proposicao'],
            'iniciativa': p['iniciativa'],
            'sumula': p['sumula'],
            'relator': p['relator'],
            'conclusao_relator': p['conclusao_relator'],
            'conclusao_comissao': p['conclusao_comissao'],
            'tem_emendas': p['tem_emendas']
        }
        for p in PROJETOS_REUNIAO
        if p['pac_id'] == pac_id
    ]
    return projetos

def get_projeto_mock(pac_id, par_id, codigo_proposicao):
    resultados = []

    for p in PROJETOS_REUNIAO:
        if (
            str(p['pac_id']) == str(pac_id) and
            str(p['par_id']) == str(par_id) and
            str(p['codigo_proposicao']) == str(codigo_proposicao)
        ):
            resultados.append({
                'pac_id': p['pac_id'],
                'par_id': p['par_id'],
                'codigo_proposicao': p['codigo_proposicao'],
                'iniciativa': p['iniciativa'],
                'sumula': p['sumula'],
                'relator': p['relator'],
                'conclusao_relator': p['conclusao_relator'],
                'conclusao_comissao': p['conclusao_comissao'],
                'tem_emendas': p['tem_emendas'],
            })

    return resultados

def get_projeto_reuniao_mock(pac_id, par_id):
    resultados = []

    for p in PROJETOS_REUNIAO:
        if (
            str(p['pac_id']) == str(pac_id) and
            str(p['par_id']) == str(par_id)
        ):
            resultados.append({
                'pac_id': p['pac_id'],
                'par_id': p['par_id'],
                'codigo_proposicao': p['codigo_proposicao'],
                'iniciativa': p['iniciativa'],
                'sumula': p['sumula'],
                'relator': p['relator'],
                'conclusao_relator': p['conclusao_relator'],
                'conclusao_comissao': p['conclusao_comissao'],
                'tem_emendas': p['tem_emendas'],
            })

    return resultados

def get_textos_conclusao_mock(pro_codigo):
    resultados = []

    for i, t in enumerate(TEXTOS_CONCLUSAO):
        if str(t['pro_codigo']) != str(pro_codigo):
            continue

        resultados.append({
            'pro_id': i + 1,
            'pro_codigo': t['pro_codigo'],
            'par_id': 0,  # mock fixo
            'txt_data': datetime.now().strftime("%d/%m/%Y"),
            'txt_finalizado': True,
            'txt_relator': False,
            'txt_id': t['txt_id'],
            'ver_id': i + 100,
            'vereador': t['vereador'],
            'tcp_id': i + 200,
            'tcp_nome': t['tcp_nome'],
            'par_finalizado': True,
            'con_id': 0,  # mock fixo
        })

    return resultados