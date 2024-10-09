from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

# Create your views here.
class AppBootstrap(View):
    def get(self, request):
        
        tareas_comunes = [
            {'icono': 'fas fa-dog', 'nombre': 'Pasear a Tony', 'descripcion': 'Llevar a Tony al parque y jugar un rato.'},  # Icono de perro
            {'icono': 'fas fa-book', 'nombre': 'Estudiar Matemáticas', 'descripcion': 'Repasar el capítulo 3 del libro de álgebra.'},  # Icono de libro
            {'icono': 'fas fa-laptop', 'nombre': 'Terminar proyecto de clase', 'descripcion': 'Completar la presentación y enviarla al profesor.'},  # Icono de computadora
            {'icono': 'fas fa-shopping-cart', 'nombre': 'Comprar materiales', 'descripcion': 'Comprar libros y materiales para el próximo semestre.'},  # Icono de carrito de compras
            {'icono': 'fas fa-cut', 'nombre': 'Cortar el cabello', 'descripcion': 'Ir a la peluquería a cortarme el cabello.'},  # Icono de tijeras
        ]


        
        grouped_tareas = [tareas_comunes[i:i + 3] for i in range(0, len(tareas_comunes), 3)]

        # Crear un contexto que incluya las tareas comunes
        data = {
            'titulo1': 'Tareas Favoritas',
            'titulo2': 'Otras Tareas',
            'grouped_tareas': grouped_tareas,
        }


        return render(request, 'templateBootstrap.html', context=data)