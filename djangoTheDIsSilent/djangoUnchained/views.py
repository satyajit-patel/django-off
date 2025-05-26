from django.shortcuts import render
from .models import superHeroes

# Create your views here.
def appHome(request):
    all_superHeroes = superHeroes.objects.all()
    return render(request, 'app-index.html', {'avengers': all_superHeroes})
