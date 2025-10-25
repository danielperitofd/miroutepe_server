from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('construcao/', views.construcao, name='construcao'),
    path('tecnologia/', views.tecnologia, name='tecnologia'),
    path('perguntas/', views.perguntas, name='perguntas'),
    path('parceiros/', views.parceiros, name='parceiros'),
    path('vantagens/', views.vantagens, name='vantagens'),
    path('ailson_team/', views.ailson_team, name='ailson_team'),
    path('adjailson_team/', views.adjailson_team, name='adjailson_team'),
    path('daniel_team/', views.daniel_team, name='daniel_team'),
    path('vanthuir_team/', views.vanthuir_team, name='vanthuir_team'),
    path('sobre/', views.sobre, name='sobre'),
    path('solucoes/', views.solucoes, name='solucoes'),
    path('suporte/', views.suporte, name='suporte'),
    path('localizacao/', views.localizacao, name='localizacao'),
    path('contato/', views.contato, name='contato'),
    path('login/', views.login_view, name='login'),
    

]
