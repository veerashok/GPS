"""GPS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from users.views import userHome


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='gpsfrontend/index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='gpsfrontend/about.html'), name='about'),
    path('teachers/', TemplateView.as_view(template_name='gpsfrontend/teachers.html'), name='teachers'),
    path('gallery/', TemplateView.as_view(template_name='gpsfrontend/gallery.html'), name='gallery'),
    path('blog/', TemplateView.as_view(template_name='gpsfrontend/404.html'), name='blog'),
    path('contact/', TemplateView.as_view(template_name='gpsfrontend/contact.html'), name='contact'),
    path('single/', TemplateView.as_view(template_name='gpsfrontend/single.html'), name='single'),
    path('user/', userHome, name='user'),

]
