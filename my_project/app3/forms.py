from django import forms
from .models import Captcha

class CaptchaForm(forms.ModelForm):
    class Meta:
        model = Captcha
        fields = ('image',)