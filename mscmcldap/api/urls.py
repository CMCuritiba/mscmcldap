# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
from ..api.spl import views as spl_views


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
	url(r'^setor_setor/(?P<set_id>[0-9]+)/$', views.setor_setor, name='api-setor-setor'),
	url(r'^funcionarios/$', views.funcionarios, name='api-funcionarios'),
	url(r'^funcionarios_setor/(?P<set_id>[0-9]+)/$', views.funcionarios_setor, name='api-funcionarios-setor'),
	url(r'^funcionario/(?P<pessoa>[0-9]+)/$', views.funcionario, name='api-funcionario'),
	url(r'^funcionario_matricula/(?P<matricula>[0-9]+)/$', views.funcionario_matricula, name='api-funcionario-matricula'),
	url(r'^spl/reuniao_comissao/$', spl_views.spl_reuniao_comissao, name='api-spl-reuniao-comissao'),
	url(r'^spl/projetos_reuniao/(?P<reuniao>[0-9]+)/$', spl_views.spl_projetos_reuniao, name='api-spl-projetos-reuniao'),
	url(r'^spl/projeto_reuniao/(?P<pac_id>[0-9]+)/(?P<par_id>[0-9]+)/$', spl_views.spl_projeto_reuniao, name='api-spl-projeto-reuniao'),
	url(r'^spl/reuniao_comissao_range/(?P<data_inicio>\d{8})/(?P<data_fim>\d{8})/$', spl_views.spl_reuniao_comissao_range, name='api-spl-reuniao-comissao-range'),
	url(r'^spl/vereadores/$', spl_views.spl_vereadores, name='api-spl-vereadores'),
	url(r'^spl/vereador_matricula/(?P<matricula>[0-9]+)/$', spl_views.spl_vereador_matricula, name='api-spl-vereador-matricula'),
	url(r'^spl/cargos_mesa/$', spl_views.spl_cargos_mesa, name='api-spl-cargos_mesa'),
	url(r'^spl/spl_get_rec_id/(?P<pac_id>[0-9]+)/$', spl_views.spl_get_rec_id, name='api-spl-spl-get-rec-id'),
	url(r'^spl/spl_get_reuniao/(?P<rec_id>[0-9]+)/$', spl_views.spl_get_reuniao, name='api-spl-spl-get-reuniao'),
	url(r'^spl/spl_get_comissao/(?P<con_id>[0-9]+)/$', spl_views.spl_get_comissao, name='api-spl-spl-get-comissao'),
	
]
