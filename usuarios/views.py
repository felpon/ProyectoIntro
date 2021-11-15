
from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib.auth.models import Group
# Create your views here.

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