from django.contrib import admin
from django.urls import include, path
from dashsys import plotly_apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portal/', include('sistema.urls')),
    path('', include('usuarios.urls')),
    path('painel/', include('administracao.urls')),
    path('dash/', include('dashsys.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]
