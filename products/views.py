from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''
        Hello,
        I am MohammadReza Qaderi 
        we can have Fun time with eachother :)
    ''')

def new(request):
    return HttpResponse('''
        New Products
    ''')