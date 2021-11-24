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
		form = Formulario(request.POST) 
		if form.is_valid:
			form.save()
		return redirect('perfil')
	else:
		form = Formulario()

	return render(request, "formulario.html", data)

def	info(request):
	info = Formu.objects.all()
	return render(request, "info.html", {"info":info})