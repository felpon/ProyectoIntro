from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, request
from django.template.loader import get_template

def pag1(request):
    doc_externo = get_template("login.html")
    documento = doc_externo.render()
    return HttpResponse(documento)

def pag2(request):
    doc_externo = get_template("home.html")
    documento = doc_externo.render()
    return HttpResponse(documento)