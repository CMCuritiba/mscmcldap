import datetime
from .data import REUNIOES

def get_reuniao_mock(rec_id):
  rec_id = int(rec_id)
  for r in REUNIOES:
    if r['rec_id'] == rec_id:
      return {
        'rec_id': r['rec_id'],
        'con_id': r['con_id'],
        'con_desc': r['con_desc'], 
        'con_sigla': r['con_sigla'],
        'rec_tipo_reuniao': r['rec_tipo_reuniao'],
        'rec_numero': r['rec_numero'],
        'versao': '1.0',  
        'rec_data': r['rec_data'],
        'pac_id': r['pac_id']
      }
  return None

def get_rec_id_mock(pac_id):
  pac_id = int(pac_id)
  for r in REUNIOES:
    if r['pac_id'] == pac_id:
      return [
        {
          'rec_id': r['rec_id'],
        }
      ]
  return None

