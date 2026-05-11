from django.urls import path
from . import views

urlpatterns = [
    path('', views.presenca_calendario, name='presenca_calendario'),
    path('dia/<str:data>/', views.presenca_dia, name='presenca_dia'),
    path('toggle/', views.toggle_presenca, name='toggle_presenca'),
]
