from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class UserProfileInfo(models.Model):

  user = models.OneToOneField(User,on_delete=models.CASCADE)
  nombre = models.CharField(max_length=50, blank=True, primary_key=True)
  rut = models.CharField(max_length=10,blank=True)
  telefono = models.CharField(max_length=20, blank=True)
  

  def __str__(self):
    return self.nombre

def create_user_profile(request, user, **kwargs):
    profile = Profile.objects.create(user=user)
    profile.save()

class Orden(models.Model):
    folio = models.CharField(max_length=10, primary_key=True)
    empresa = models.ForeignKey('Cliente', null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField()
    horaInicio = models.TimeField()
    horaTermino = models.TimeField()
    IdAscensor = models.CharField(max_length=50 )
    modeloAcensor = models.CharField(max_length=50 )
    fallas = models.TextField()
    reparaciones = models.TextField()
    piezasCambiadas = models.TextField()
    tecnico = models.ForeignKey('UserProfileInfo', null=True, blank=True, on_delete=models.CASCADE)



class Cliente(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField(unique=True)
	
    def __str__(self):
        return '{}'.format(self.nombre)
# Create your models here.



   
