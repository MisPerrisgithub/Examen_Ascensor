from django import forms
from .models import Orden, Cliente
from .models import UserProfileInfo
from django.contrib.auth.models import User
from django.forms import TextInput


class UserForm(forms.ModelForm):
   class Meta():
    password = widget=forms.TextInput(attrs={'type' : 'password'})
    model = User
    fields = ('username','password','email')
    help_texts = {
            'username': None,
            'email': None,
        }
    widgets = {
		'password':TextInput(attrs={'type':'password'})
	}

class UserProfileInfoForm(forms.ModelForm):
 
 class Meta():
  model = UserProfileInfo
  fields = ('nombre','rut','telefono')



class clienteForm(forms.ModelForm):

	class Meta:
		model = Cliente

		fields = [
			'nombre',
			'direccion',
			'ciudad',
			'comuna',
			'telefono',
			'email',
		]
		labels = {
			'nombre': 'Nombre',
			'direccion': 'Direccion',
			'ciudad': 'Ciudad',
			'comuna':'Comuna',
			'telefono' : 'Telefono',
			'email' : 'Email',
		}
		widgets = {
			'nombre': forms.TextInput(),
			'direccion': forms.TextInput(),
			'ciudad': forms.TextInput(),
			'comuna': forms.TextInput(),
			'telefono': forms.TextInput(),
			'email': forms.EmailInput(),
		}

class servicioForm(forms.ModelForm):

	class Meta:
		model = Orden

		fields = [
			'folio',
			'empresa' ,
			'fecha' ,
			'horaInicio' ,
			'horaTermino',
			'IdAscensor',
			'modeloAcensor',
			'fallas',
			'reparaciones',
			'piezasCambiadas',
			'tecnico'
		]
		labels = {
			'folio':'Numero de folio',
			'empresa':'Nombre de la empresa' ,
			'fecha':'Fecha de atencion' ,
			'horaInicio':'Hora Inicio' ,
			'horaTermino':'Hora Termino',
			'IdAscensor':'Id Ascensor',
			'modeloAcensor':'Modelo Acensor',
			'fallas':'fallas del Ascensor',
			'reparaciones':'Reparaciones',
			'piezasCambiadas':'Piezas Cambiadas',
			'tecnico':'Tecnico Asignado'
		}
		widgets = {
			'folio': forms.TextInput(),
			'empresa':forms.Select(),
			'fecha': forms.TextInput(),
			'horaInicio': forms.TextInput(),
			'horaTermino': forms.TextInput(),
			'IdAscensor': forms.TextInput(),
			'modeloAcensor':forms.TextInput() ,
			'fallas' :forms.TextInput(), 
			'reparaciones' : forms.TextInput(),
			'piezasCambiadas' : forms.TextInput(),
			'tecnico':forms.Select(),

		}

