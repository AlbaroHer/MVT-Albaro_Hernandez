from unittest import loader
from django.shortcuts import render
from django.template.loader import get_template
from .models import Familia
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def list_family(request):
    #template= get_template('list_family.html')
    familia= Familia.objects.all()
    #print(familia)
    context= {
        'familia': familia          
    }
    return render(request,"list_family.html", context)

def framework(request):
    fecha_actual= datetime.now()
    #temp= get_template('plantilla_hija.html')
    ctx= {
        "dame_fecha":fecha_actual
        }

    return render(request,'plantilla_hija.html',ctx)
    
     
