# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^setores/$', views.setores, name='api-setores'),
	url(r'^pessoas/$', views.pessoas, name='api-pessoas'),
	url(r'^pessoas_setor/(?P<set_id>[0-9]+)/$', views.pessoas_setor, name='api-pessoas-setor'),
	url(r'^pessoa/(?P<pes_matricula>[0-9]+)/$', views.pessoa, name='api-pessoa'),
	url(r'^setor/(?P<pes_matricula>[0-9]+)/$', views.setor, name='api-setor'),
	url(r'^centros_custo/$', views.centros_custo, name='api-centros-custo'),
	url(r'^centro_custo/(?P<centro_custo>[0-9]+)/$', views.centro_custo, name='api-centro-custo'),
	url(r'^itens/$', views.itens, name='api-itens'),
	url(r'^item/(?P<item_id>[0-9]+)/$', views.item, name='api-item'),
]