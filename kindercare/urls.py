from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usuarios/', include('users.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('terapeutas/', include('terapeutas.urls')),
    path('agenda/', include('agenda.urls')),
    path('evolucoes/', include('evolucoes.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('presencas/', include('presencas.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
