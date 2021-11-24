import django
from sistemalogin.views import pag1, pag2
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls'))
]
