from django.shortcuts import render
from django.http import HttpResponse


def products(request, product_id=0):
    output = "<h2>Product № {0}</h2>".format(product_id)
    return HttpResponse(output)


def user(request, id=0, name='Ivan'):
    output = "<h2>User</h2><h3>ID: {0} Name: {1}</h3>".format(id, name)
    return HttpResponse(output)


def category(request, id, name):
    output = '<h2>Categories</h2><h3>Category ID: {0} Category Name: {1}</h3>'.format(id, name)
    return HttpResponse(output)