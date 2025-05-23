from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("wellcome to home page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("wellcome to about page")

def contact(request):
    return HttpResponse("wellcome to contact page")