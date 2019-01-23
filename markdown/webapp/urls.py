"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.views.generic.base import TemplateView

from markdown.views import upload

urlpatterns = [
    path('', TemplateView.as_view(template_name='markdown/index.html'),
         name='index-url'),
    path('preview/', TemplateView.as_view(template_name='markdown/preview.html'),
         name='preview-url'),

    path('api/upload/', upload, name='api-upload-url'),
]
