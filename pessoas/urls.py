from django.urls import path
from . import views

urlpatterns = [
    path('incluir/', views.incluir),
    path('', views.listar),  
    path('alterar/', views.alterar),
    path('excluir/<int:id>/', views.excluir),
    path('pesquisar/<int:id>/', views.pesquisar),
    path('peso-ideal/', views.peso_ideal),
]
