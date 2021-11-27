from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, Formulario
from django.contrib.auth import authenticate, login
from .models import *
from django.shortcuts import render, redirect, get_object_or_404

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
			post.user = current_user
			post.save()
			messages.success(request, f'Cuestionario guardado')
			return redirect('mensaje')
		else:
			form = Formulario()

	return render(request, "formulario.html", data)

def mensaje(request):
	if authenticate:
		current_user = get_object_or_404(User, pk=request.user.pk)
		perfil = Formu.objects.filter(user=current_user)[:1]
		pregunta = perfil[0]
		puntaje = 0
		puntaje += pregunta.preg1
		puntaje += pregunta.preg2
		puntaje += pregunta.preg3
		puntaje += pregunta.preg4
		puntaje += pregunta.preg5
		puntaje += pregunta.preg6
		puntaje += pregunta.preg7
		puntaje += pregunta.preg8
		puntaje += pregunta.preg9
		puntaje += pregunta.preg10
		puntaje += pregunta.preg11
		puntaje += pregunta.preg12
		puntaje += pregunta.preg13
		puntaje += pregunta.preg14
		return render(request, "mensaje.html", {"puntaje":puntaje})
	else:
		return redirect("home")


def	info(request):
	if authenticate:
		current_user = get_object_or_404(User, pk=request.user.pk)
		info = Formu.objects.filter(user=current_user)
		return render(request, "info.html", {"info":info})
	else:
		return redirect("home")