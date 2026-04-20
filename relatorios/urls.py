from django.urls import path
from .views import produtividade_view

urlpatterns = [
    path('produtividade/', produtividade_view, name='produtividade_view'),
]
