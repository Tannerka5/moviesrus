from django.shortcuts import render
from .models import Movie, Category, Rating

# Create your views here.

def indexPageView(request):
    return render(request, 'moviesapp/index.html')

def showMoviePageView(request, movie_title):
    context = {
        'movie_title': movie_title,
    }
    return render(request, 'moviesapp/show_movie.html', context)

def showInfoPageView(request, movie_title, movie_year):
    context = {
        'movie_title': movie_title,
        'movie_year': movie_year
    }
    return render(request, 'moviesapp/show_info.html', context)
    
def displayPageView(request):
    db_movies = Movie.objects.all()

    return render(request, 'moviesapp/display.html', {'db_movies': db_movies})