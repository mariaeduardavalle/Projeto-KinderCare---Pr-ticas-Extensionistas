from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('novo/', views.user_create, name='user_create'),
    path('<int:pk>/editar/', views.user_update, name='user_update'),
    path('<int:pk>/excluir/', views.user_delete, name='user_delete'),
]
