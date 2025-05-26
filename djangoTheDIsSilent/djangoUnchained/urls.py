from django.urls import path
from . import views

# localhost:8000/djangoUnchained/
# localhost:8000/djangoUnchained/about

urlpatterns = [
    path('', views.appHome, name='appHome'),
    path('<int:hero_id>/', views.hero_detail, name='hero_detail'),
]