from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h4>Проверка работы</h4>')

def about(request):
    return HttpResponse('<h4>About us</h4>')

def price(request):
    return HttpResponse('<h2>Price</h2>')