# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^setores/$', views.setores, name='api-setores'),
	url(r'^pessoas/(?P<set_id>[0-9]+)/$', views.pessoas, name='api-pessoas'),
	url(r'^pessoa/(?P<pes_matricula>[0-9]+)/$', views.pessoa, name='api-pessoa'),
]