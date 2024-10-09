import random
from django.shortcuts import render
from django.views.generic import View
from .models import Captcha

class CaptchaView(View):
    def get(self, request):
        # Selecciona una categoría al azar
        category = Captcha.objects.order_by('?').first().category
        # Obtiene los captchas asociados a esa categoría
        captchas = Captcha.objects.filter(category=category)
        return render(request, 'captcha.html', {'captchas': captchas})

    def post(self, request):
        # Obtiene la categoría del formulario
        category = request.POST.get('category')
        # Filtra los captchas por esa categoría
        captchas = Captcha.objects.filter(category=category)
        # Captura la solución enviada por el usuario
        solution = request.POST.get('solution')
        
        # Validación: revisa si la solución es la correcta
        captcha_correcto = None
        for captcha in captchas:
            if captcha.image == solution:
                captcha_correcto = captcha.solution
                break

        # Verifica si la solución es correcta
        if captcha_correcto:
            # Si es correcto, muestra el mensaje de éxito en la misma página
            return render(request, 'captcha.html', {
                'captchas': captchas,
                'message': '¡Has resuelto el captcha correctamente!',
                'message_type': 'success'
            })
        else:
            # Si es incorrecto, muestra el mensaje de error en la misma página
            return render(request, 'captcha.html', {
                'captchas': captchas,
                'message': 'Lo siento, no has resuelto el captcha correctamente.',
                'message_type': 'error'
            })

class ErrorView(View):
    def get(self, request):
        return render(request, 'error.html')
    
class SuccessView(View):
    def get(self, request):
        return render(request, 'success.html')
