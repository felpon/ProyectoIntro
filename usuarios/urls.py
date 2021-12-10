from django.urls import path
from django.contrib.auth.views import  logout_then_login, LoginView
from . import views


urlpatterns = [
    path("accounts/register/", views.register, name="register"),
    path("accounts/login/", LoginView.as_view(template_name='login.html'), name="login"),
    path("", views.feed, name="home"),
    path("logout/", logout_then_login, name="logout"),
    path("profile/", views.perfil, name="perfil"),
    path("formulario/", views.formulario, name="formulario"),
    path("info/", views.info, name="info"),
    path("mensaje/", views.mensajepost, name="mensaje"),
    path("formuhisto/", views.formHisto, name="Histform"),
]
