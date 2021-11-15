from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	#email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
	#user_pic = forms.ImageField(label="Imagen de perfil")

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']
		help_texts = {k:"" for k in fields }