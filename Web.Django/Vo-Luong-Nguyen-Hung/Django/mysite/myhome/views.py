from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines('<h1> Wellcome to Django</h1>')
    response.write('Here is app home')
    return response