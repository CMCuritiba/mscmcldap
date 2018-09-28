# -*- coding: utf-8 -*-

import datetime

def formataData(data):
	try:
		dia = data[0:2]
		mes = data[2:4]
		ano = data[4:8]

		return datetime.date(int(ano), int(mes), int(dia))
	except:
		return None