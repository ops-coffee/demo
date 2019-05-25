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
from django.contrib.auth.views import LoginView, LogoutView

from ops_coffee.views import index, index_save, index_push
from ops_coffee.views import blog, blog_change, blog_delete, render_blogs

urlpatterns = [
    path('', index, name='url'),

    path('index', index, name='index-url'),
    path('index/save/', index_save, name='index-save-url'),
    path('index/push/', index_push, name='index-push-url'),

    path('blog', blog, name='blog-url'),
    path('blog/change/', blog_change, name='blog-change-url'),
    path('blog/delete/', blog_delete, name='blog-delete-url'),
    path('blog/render/', render_blogs, name='blog-render-url'),

    path('login', LoginView.as_view(template_name='login.html'), name='login-url'),
    path('logout', LogoutView.as_view(template_name='login.html'), name='logout-url'),
]
