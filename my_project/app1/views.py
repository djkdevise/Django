from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

# Create your views here.
class HelloWorld(View):
    def get(self, request):
        return HttpResponse(content="Hola mundo desde django")
