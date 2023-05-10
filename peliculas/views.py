from django.shortcuts import render
from peliculas.populate import populate
from peliculas.models import User, Movie, Rating
from django.db.models import Count

# Create your views here.

def populate_database(request):
    inf = populate()
    return render(request, 'carga.html', {'inf': inf})

def users(request):
    users = User.objects.all().order_by('occupation')
    return render(request, 'users.html', {'users': users})

def moviesTop50(request):
    top50 = Rating.objects.values('idMovie').annotate(valoraciones=Count('idMovie')).order_by()[:50]
    idMoviesTop50 = []
    for i in top50:
        idMoviesTop50.append(i['idMovie'])
    top50 = list(top50)
    movies = Movie.objects.filter(idMovie__in=idMoviesTop50)
    print(movies)
    return render(request, 'movies.html', {'movies': movies, 'valoracionesDict': top50})