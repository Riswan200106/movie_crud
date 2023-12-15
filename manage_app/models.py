from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    title= models.CharField(max_length=25)
    year = models.IntegerField(null=True)
    summary = models.TextField()
   # poster = models.ImageField(upload_to= 'images/',null = True)

    def __str__(self):
        return self.title

class Director(models.Model):
    name = models.CharField(max_length=25)