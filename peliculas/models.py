from django.db import models
from django.utils import timezone

# Create your models here.

class Occupation(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name
    
class Category(models.Model):
    idCategory = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    idMovie = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    releaseDate = models.DateField(null=True)
    imdbUrl = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
class User(models.Model):
    idUser = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.ForeignKey('Occupation', on_delete=models.CASCADE)
    zipCode = models.CharField(max_length=5)

    class Meta:
        ordering = ('occupation', )

    def __str__(self):
        return self.occupation.name + ", " + str(self.age)
    
    
class Rating(models.Model):
    idUser = models.ForeignKey('User', on_delete=models.CASCADE)
    idMovie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    rating = models.IntegerField()
    timestamp = models.DateField(default=timezone.now)

    def __str__(self):
        return self.rating
