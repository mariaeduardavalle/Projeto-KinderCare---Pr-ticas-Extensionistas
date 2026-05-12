from django.urls import path
from . import views

urlpatterns = [
    path('produtividade/', views.produtividade_view, name='produtividade_view'),
    path('produtividade/exportar/', views.exportar_excel, name='exportar_excel'),
]
