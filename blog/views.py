from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm,UserProfileInfoForm, clienteForm,servicioForm
from .models import Cliente,Orden, UserProfileInfo
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse





# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def registrar_cliente(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('index')

    else:
        form = clienteForm()
    return render(request, 'blog/registrarCliente.html', {'form':form})    

def registro(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'foto_perfil' in request.FILES:
                print('found it')
                profile.foto_perfil = request.FILES['foto_perfil']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'blog/registrarTecnico.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def registrar_orden(request):
    if request.method == 'POST':
        form = servicioForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('index')
	
    else:
        form = servicioForm()
    return render(request, 'blog/registrarOrden.html', {'form':form})



def logOut(request):
 logout(request)
 return redirect('/')

def Login(request):  
    return render(request, 'blog/Login.html', {})

@login_required
def special(request):
    return HttpResponse("Has iniciado sesión correctamente")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('register'))

def mostrar(request):
	userito = UserProfileInfo.objects.all()
	contexto = {'UserProfileInfo':userito}
	return render(request, 'blog/index.html',contexto)

def listadoCliente(request):
	Empresa = Cliente.objects.all()
	contexto = {'clientes': Empresa}
	return render(request, 'blog/listadoCliente.html', contexto)

def listadoOrden(request):
	Servicio = Orden.objects.all()
	contexto = {'servicios': Servicio}
	return render(request,'blog/listadoOrden.html', contexto)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Tu cuenta está inactiva")
        else:
            print("Alguien intentó iniciar sesión y falló")
            print("Usó el usuario: {} y contraseña: {}".format(username,password))
            return HttpResponse("Datos de ingreso incorrectos!")
    else:
        return render(request, 'blog/Login.html', {})
