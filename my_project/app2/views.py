from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

# Create your views here.
class HelloWorld2(View):
    def get(self, request):
        data={
            'name_aplication': 'Aplicación de prueba 2',
            'fecha_creacion': 'Octubre 04 de 2924', 
            'version' : '1',
            'tecnologias': ['Python', 'Django', 'Html', 'Css']
        }
        return render(request, 'template.html', context=data)