from django.contrib import admin
from .models import Familia

# Register your models here.

class Familia_admin(admin.ModelAdmin):
    list_display= ('nombre','apellido','edad','fecha')
    
admin.site.register(Familia,Familia_admin)

