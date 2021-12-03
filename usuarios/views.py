from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, Formulario
from django.contrib.auth import authenticate, login
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
import datetime

def feed(request):
	return render(request, 'Home.html')

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data["password1"])
			login(request, user)
			messages.success(request, f'Usuario {user} creado')
			return redirect('home')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'register.html', context)

def perfil(request):
	return render(request, "profile.html")

def formulario(request):
	data = { 
		"form": Formulario()
	}
	if request.method == "POST":
		current_user = get_object_or_404(User, pk=request.user.pk) 
		form = Formulario(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			puntaje = 0
			puntaje += post.preg1
			puntaje += post.preg2
			puntaje += post.preg3
			puntaje += post.preg4
			puntaje += post.preg5
			puntaje += post.preg6
			puntaje += post.preg7
			puntaje += post.preg8
			puntaje += post.preg9
			puntaje += post.preg10
			puntaje += post.preg11
			puntaje += post.preg12
			puntaje += post.preg13
			puntaje += post.preg14
			post.user = current_user
			post.puntaje = puntaje
			post.save()
			messages.success(request, f'Cuestionario guardado')
			return redirect('mensaje')
		else:
			form = Formulario()

	return render(request, "formulario.html", data)

def mensajepost(request):
	if authenticate:
		current_user = get_object_or_404(User, pk=request.user.pk)
		perfil = Formu.objects.filter(user=current_user)[:1]
		pregunta = perfil[0]
		puntaje = pregunta.puntaje
		puntaje = int(puntaje)
		return render(request, "mensaje.html", {"puntaje":puntaje})
	else:
		return redirect("home")

def mhistorial(request,id):
	if authenticate:
		perfil = Formu.objects.filter(id=id)
		pregunta = perfil[0]
		puntaje = pregunta.puntaje
		puntaje = int(puntaje)
		return render(request, "mensaje.html", {"puntaje":puntaje})
	else:
		return redirect("home")


def	info(request):
	if request.method == "POST":
		id = request.POST.get("id")
		return mhistorial(request,id)
	if authenticate:
		current_user = get_object_or_404(User, pk=request.user.pk)
		info = Formu.objects.filter(user=current_user)
		return render(request, "info.html", {"info":info})
	else:
		return redirect("home")