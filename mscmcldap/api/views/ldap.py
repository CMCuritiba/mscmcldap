# -*- coding: utf-8 -*-


from django.conf import settings
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import fields, serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from ldap3 import Server, Connection, ALL
import json
import re

from mscmcldap.util.json_util import JsonConvert

@api_view(['GET'])
def ldap_usuarios(request):
    server = Server(settings.LDAP_HOST, port=settings.LDAP_PORT)

    usuarios_json = []
    s = Server('localhost', port=389)
    # c = Connection(s)
    conn = Connection(
        server,
        user=settings.LDAP_USER,
        password=settings.LDAP_PASSWORD,
        auto_bind=True
    )

    conn.search(
        search_base=settings.LDAP_BASE_DN,
        search_filter='(employeeNumber=*)',
        attributes=['cn', 'givenName', 'uid', 'employeeNumber', 'mail']
    )
    
    for usuario in conn.response:
        e_json = {}
        e_json['cn'] = re.sub('(\[)*(\])*(\')*', '', str(usuario['attributes']['cn']))
        e_json['givenName'] = re.sub('(\[)*(\])*(\')*', '', str(usuario['attributes']['givenName']))
        e_json['uid'] = re.sub('(\[)*(\])*(\')*', '', str(usuario['attributes']['uid']))
        e_json['employeeNumber'] = int(re.sub('(\[)*(\])*(\')*', '', str(usuario['attributes']['employeeNumber'])))
        e_json['mail'] = re.sub('(\[)*(\])*(\')*', '', str(usuario['attributes']['mail']))
        usuarios_json.append(e_json)        

    return JsonResponse(usuarios_json, safe=False)