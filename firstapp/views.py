from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse


# def products(request, product_id=0):
#     category = request.GET.get('category', '')
#     output = "<h2>Product № {0}, category: {1}</h2>".format(product_id, category)
#     return HttpResponse(output)
#
#
# def user(request):
#     id = request.GET.get('id', 0)
#     username = request.GET.get('username', '')
#     phone = request.GET.get('phone', '')
#     output = '<h2>ID: {0}, username: {1}, phone: {2}</h2>'.format(id, username, phone)
#     return HttpResponse(output)


# def category(request, id, name):
#     output = '<h2>Categories</h2><h3>Category ID: {0} Category Name: {1}</h3>'.format(id, name)
#     return HttpResponse(output)


# def index(request):
#     return HttpResponse('index')
#
#
# def about(request):
#     return HttpResponse('about')
#
#
# def contacts(request):
#     return HttpResponseRedirect('/about')
#
#
# def details(request):
#     return HttpResponsePermanentRedirect('/')


# def index(request):
#     data = {'header': 'test_header', 'message': 'test_message'}
#     return render(request, 'first_app/home.html', context=data)


# def index(request):
#     header = 'Personal data'
#     language = ['English', 'Rushian', 'Ukrainian']
#     user = {
#         'name': 'Ivan',
#         'age': 14,
#     }
#     address = ('Marsel', 17)
#     data = {
#         'header': header,
#         'language': language,
#         'user': user,
#         'address': address
#     }
#     return render(request, 'index.html', context=data)


# def about(request):
#     test = 1
#     pers = {
#         'name': 'Amazon',
#         'count': 100,
#         'when': '27.03.2004',
#         'location': 'Berlin'
#     }
#     data = {
#         'pers': pers,
#         'test': test
#     }
#     # return render(request, 'first_app/about.html', context=data)
#     return TemplateResponse(request, 'first_app/about.html', data)
#
#
# def users(request):
#     name = 'Ivan'
#     surname = 'Ivanow'
#     age = 24
#     locate = 'Ukraine'
#     married = False
#     data = {'name': name, 'surname': surname, 'age': age, 'locate': locate, 'married': married}
#     return render(request, 'first_app/users.html', context=data)
#
#
# def basket(request):
#     data = {'products': 'meat', 'technics': 'phone', 'money': '250'}
#     return render(request, 'first_app/basket.html', context=data)
#
#
# def login(request):
#     data = {'user_username': 'admin', 'user_password': '********', 'terms': 'We dont use your information...'}
#     return render(request, 'first_app/login.html', context=data)