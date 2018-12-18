# -*- coding: utf-8 -*-

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import fields, serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
import json

from mscmcldap.util.json_util import JsonConvert

@api_view(['GET'])
def connection(request):
    answer = []
    answer_json = {}
    answer_json['connected'] = True
    answer.append(answer_json)        

    return JsonResponse(answer, safe=False)