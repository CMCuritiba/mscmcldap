from datetime import datetime
from .data import REUNIOES  


def hoje_str():
    return datetime.now().strftime("%d/%m/%Y")

def get_reunioes_mock():
    data_str = hoje_str()

    reunioes_do_dia = [
        {
            'rec_id': r['rec_id'],
            'con_id': r['con_id'],
            'con_desc': r['con_desc'],
            'con_sigla': r['con_sigla'],
            'rec_tipo_reuniao': r['rec_tipo_reuniao'],
            'rec_numero': r['rec_numero'],
            'versao': '1.0',
            'rec_data': data_str,
            'pac_id': r['pac_id']
        }
        for r in REUNIOES
    ]

    return reunioes_do_dia

def get_comissao_mock(con_id):
  con_id = int(con_id)
  for r in REUNIOES:
    if r['con_id'] == con_id:
        return {
                'con_id': r['con_id'],
                'ini_nome': r['con_desc'],
            }
  return None


def parse_data(data_str):
    if not data_str:
        return None

    for fmt in ("%d%m%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(data_str, fmt)
        except:
            continue

    return None


def get_reunioes_range_mock(data_inicio, data_fim):
    inicio = parse_data(data_inicio)
    fim = parse_data(data_fim)

    resultados = []

    for r in REUNIOES:
        rec_data = datetime.now()

        # ----------------------------
        # Filtro por data
        # ----------------------------
        if inicio and fim:
            if not (inicio <= rec_data <= fim):
                continue
        elif inicio:
            if not (rec_data >= inicio):
                continue

        # ----------------------------
        # Simula pauta liberada
        # ----------------------------
        pac_liberada = True  

        if not pac_liberada:
            continue

        # ----------------------------
        # Monta retorno
        # ----------------------------
        resultados.append({
            'rec_id': r['rec_id'],
            'con_id': r['con_id'],
            'con_desc': r['con_desc'],
            'con_sigla': r['con_sigla'],
            'rec_tipo_reuniao': r['rec_tipo_reuniao'],
            'rec_numero': r['rec_numero'],
            'versao': 1,  
            'rec_data': hoje_str(),
            'pac_id': r['pac_id'],
        })

    return resultados

