import django
from django.db import models
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

op1 = [
	[0, "muy mal"],
	[1, "mal"],
	[2, "normal"],
	[3, "bien"],
	[4, "muy bien"],
]
op2 = [
	[0, "capaz"],
	[1, "quizas"],
	[2, "incapaz"],
]
op3 = [
	[0, "mucho"],
	[1, "me  preocupa"],
	[2, "poco "],
	[3, "no me afecta"],
]
op4 = [
	[0, "Muy presionado"],
	[1, "poco presionado"],
	[2, "Ninguna presión"],
]
op5 = [
	[0, "Si"],
	[1, "No"],
]
op6 = [
	[0, "siempre"],
	[1, "casi siempre"],
	[2, "a veces"],
	[3, "casi nunca"],
	[4, "nunca"],
]
op7 = [
	[0, "Me cuesta mucho"],
	[1, "Me cuesta poco"],
	[2, "Me relajo fácilmente"],
]
op8 = [
	[0, "mucho"],
	[1, "más o menos"],
	[2, "poco"],
	[3, "nada"],
]
op9 = [
	[0, "mucho"],
	[1, "más o menos"],
	[2, "poco"],
	[3, "nada"],
	[4, "saltar"],
]
op10 = [
	[0, "Ha sido peor"],
	[1, "Un poco mejor"],
	[2, "igual que la semana anterior"],
	[3, "Ha mejorado mucho "],
]
op11 = [
	[0, "Casi no puedo dormir"],
	[1, "Duermo un poco menos"],
	[2, "duermo lo mismo que siempre"],
	[3, "estoy durmiendo un poco más"],
	[4, "Duermo mucho más que antes"]
]    
op12 = [
	[0, "Siento que tengo muy poco tiempo"],
	[1, "Siento que estoy bien con el tiempo "],
	[2, "Me siento con mucho tiempo libre"],
]
class Formu(models.Model):
	#user = models.ForeignKey(User, on_delete=models.CASCADE)
	preg1 = models.IntegerField(choices=op1)
	preg2 = models.IntegerField(choices=op2)
	preg3 = models.IntegerField(choices=op1)
	preg4 = models.IntegerField(choices=op3)
	preg5 = models.IntegerField(choices=op4)
	preg6 = models.IntegerField(choices=op5)
	preg7 = models.IntegerField(choices=op6)
	preg8 = models.IntegerField(choices=op6)
	preg9 = models.IntegerField(choices=op7)
	preg10 = models.IntegerField(choices=op8)
	preg11 = models.IntegerField(choices=op9)
	preg12 = models.IntegerField(choices=op10)
	preg13 = models.IntegerField(choices=op11)
	preg14 = models.IntegerField(choices=op12)


