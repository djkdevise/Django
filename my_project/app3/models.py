from django.db import models

class Captcha(models.Model):
    CATEGORY_TRANSPORT = 'transport'
    CATEGORY_PAYMENT = 'payment'

    CATEGORY_CHOICES = (
        (CATEGORY_TRANSPORT, 'Transport'),
        (CATEGORY_PAYMENT, 'Payment'),
    )

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='captcha_images')
    solution = models.BooleanField(default=False)  # True if the image is the solution, False otherwise

    def __str__(self):
        return f"Captcha {self.category} - {self.image.name}"