from django.contrib import admin
from .models import Cliente,Orden
from .models import  User, UserProfileInfo


# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Orden)
admin.site.register(Cliente)
