from django.shortcuts import render
from .models import superHeroes
from django.shortcuts import get_object_or_404

# Create your views here.
def appHome(request):
    all_superHeroes = superHeroes.objects.all()
    return render(request, 'app-index.html', {'avengers': all_superHeroes})

def hero_detail(request, hero_id):
    data = get_object_or_404(superHeroes, pk=hero_id)
    return render(request, 'hero-detail.html', {'hero': data})
