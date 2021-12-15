import django
from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone

op1 = [
	[0, "muy mal"],
	[1, "mal"],
	[2, "normal"],
	[3, "bien"],
	[4, "muy bien"],
]
op2 = [
	[2, "capaz"],
	[1, "quizas"],
	[0, "incapaz"],
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
	[1, "Igual que la semana anterior"],
	[2, "Un poco mejor"],
	[3, "Ha mejorado mucho "],
]
op11 = [
	[0, "Casi no puedo dormir"],
	[1, "Duermo mucho más que antes"],
	[2, "Duermo un poco menos"],
	[3, "Estoy durmiendo un poco más"],
	[4, "Duermo lo mismo que siempre"]
]    
op12 = [
	[0, "Siento que tengo muy poco tiempo"],
	[1, "Siento que estoy bien con el tiempo "],
	[2, "Me siento con mucho tiempo libre"],
]
class Formu(models.Model):
	user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
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
	time = models.DateTimeField(default=django.utils.timezone.now , null=True,blank=True)
	puntaje = models.CharField(null=True,blank=True, max_length=4)
	class Meta:
		ordering = ['-time']

	def __str__(self):
		return f'{self.user.username}: {self.time}'
