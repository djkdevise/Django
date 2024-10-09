"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import HelloWorld
from app2.views import HelloWorld2
from app3.views import *
from app4.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', HelloWorld.as_view()),
    path('app2/', HelloWorld2.as_view()),
    path('app3/', CaptchaView.as_view(), name='captcha'),  # Asigna un nombre a la vista del captcha
    path('app3/error/', ErrorView.as_view(), name='error'),
    path('app3/success/', SuccessView.as_view(), name='success'),
    path('app4/', AppBootstrap.as_view(), name='appBootstrap'),  # Asigna un nombre a la vista del appBootstrap
]