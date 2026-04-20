from django.urls import path
from . import views

urlpatterns = [
    path('', views.terapeuta_list, name='terapeuta_list'),
    path('novo/', views.terapeuta_create, name='terapeuta_create'),
    path('<int:pk>/editar/', views.terapeuta_update, name='terapeuta_update'),
    path('<int:pk>/excluir/', views.terapeuta_delete, name='terapeuta_delete'),
]
