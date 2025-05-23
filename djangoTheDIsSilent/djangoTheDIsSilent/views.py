from django.http import HttpResponse

def home(request):
    return HttpResponse("wellcome to home page")

def about(request):
    return HttpResponse("wellcome to about page")

def contact(request):
    return HttpResponse("wellcome to contact page")