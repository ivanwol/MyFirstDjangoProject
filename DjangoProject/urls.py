"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from django.views.generic import TemplateView
from firstapp import views

# urlpatterns = [
    # # path('categories/<int:id>/<name>/', views.category, name='categories'),
    # path('products/', views.products),
    # path('products/<int:product_id>/', views.products, name='products'),
    # path('users/', views.user),
    # # path('users/<int:id>/<name>/', views.user, name='users'),
    # path('admin/', admin.site.urls),
    # path('', views.index),
    # path('about/', views.about),
    # path('details/', views.details),
    # path('contacts/', views.contacts),
    # path('', TemplateView.as_view(template_name='index.html', extra_context={
    #     'name': 'Ivan',
    #     'age': 14,
    #     'address': ['Marsell', 46],
    #     'language': ['Ukrainian', 'English', 'Rushian']
    # })),
    # path('about/', views.about),
    # # path('users/', views.users),
    # path('users/', TemplateView.as_view(template_name='first_app/users.html', extra_context={
    #     'name': 'Ivan',
    #     'surname': 'Ivanow',
    #     'age': 14,
    #     'locate': 'Ukraine',
    #     'married': False,
    # })),
    # path('basket/', views.basket),
    # path('login/', TemplateView.as_view(template_name='first_app/login.html', extra_context={
    #     'user_username': 'Admin',
    #     'user_password': '*********',
    #     'terms': 'We don\'t steel yout info...'
#     })),
#     # path('login/', views.login),
# ]
urlpatterns = [
    path('', views.index),
    path('about/', TemplateView.as_view(template_name='first_app/about.html')),
    path('users/', TemplateView.as_view(template_name='first_app/users.html')),
    path('basket/', views.basket),
    path('login/', views.login),
]