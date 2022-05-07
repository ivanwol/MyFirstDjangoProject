from django.shortcuts import render
from django.http import HttpResponse


def products(request, product_id=0):
    category = request.GET.get('category', '')
    output = "<h2>Product № {0}, category: {1}</h2>".format(product_id, category)
    return HttpResponse(output)


def user(request):
    id = request.GET.get('id', 0)
    username = request.GET.get('username', '')
    phone = request.GET.get('phone', '')
    output = '<h2>ID: {0}, username: {1}, phone: {2}</h2>'.format(id, username, phone)
    return HttpResponse(output)


# def category(request, id, name):
#     output = '<h2>Categories</h2><h3>Category ID: {0} Category Name: {1}</h3>'.format(id, name)
#     return HttpResponse(output)