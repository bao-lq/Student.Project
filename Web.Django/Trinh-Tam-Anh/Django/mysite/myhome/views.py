from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # response = HttpResponse()
    # response.writelines('<h1>Welcome to Django</h1>')
    # response.write('Here is app home')
    # return response
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')