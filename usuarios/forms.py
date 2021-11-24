from django import forms
from .models import Formu, User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	username = forms.CharField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
	#user_pic = forms.ImageField(label="Imagen de perfil")

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']
		help_texts = {k:"" for k in fields }


class Formulario(forms.ModelForm):
	class Meta:
		model = Formu
		fields = "__all__"
		help_texts = {k:"" for k in fields }

