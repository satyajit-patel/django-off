from django.db import models
from django.utils import timezone

# Create your models here.

class superHeroes(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='') # every time you change something in model make sure to hit make migration and migrate again

    def __str__(self):
        return self.name
