from re import template
from django.shortcuts import render
from django.template import loader
from .models import Familia
from django.http import HttpResponse

# Create your views here.

def list_family(request):
    template= loader.get_template('list_family.html')
    familia= Familia.objects.all()
    #print(familia)
    context= {
        'familia': familia        
    }
    return HttpResponse(template.render(context, request))
     
