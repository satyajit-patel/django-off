from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def appHome(request):
    return render(request, 'app-index.html')
    # now go to urls in project and copy content and make an urls in app

def appAbout(request):
    return HttpResponse("wellcome to appAbout page")
