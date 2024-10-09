from django.core.management.base import BaseCommand
from .models import Captcha

class Command(BaseCommand):
    def handle(self, *args, **options):
        transport_images = [
            'img/captcha1/structure.png',  # Not a transport medium
            'img/captcha1/helicopter.png',
            'img/captcha1/motorcycle.png',
            'img/captcha1/parachute.png',
            'img/captcha1/plane.png',
        ]

        payment_images = [
            'img/captcha2/barcode.png',  # Not a payment method
            'img/captcha2/coin.png',
            'img/captcha2/coin1.png',
            'img/captcha2/note.png',
            'img/captcha2/wallet.png',
        ]

        for image in transport_images:
            Captcha.objects.create(category=Captcha.CATEGORY_TRANSPORT, image=image, solution=image == 'img/captcha1/structure.png')

        for image in payment_images:
            Captcha.objects.create(category=Captcha.CATEGORY_PAYMENT, image=image, solution=image == 'img/captcha2/barcode.png')