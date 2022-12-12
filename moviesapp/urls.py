from django.urls import path
from .views import indexPageView, showMoviePageView, showInfoPageView, displayPageView

urlpatterns = [
    path('', indexPageView, name="index"),
    path('<movie_title>', showMoviePageView, name='movie'),
    path('<movie_title>/<movie_year>', showInfoPageView, name="info"),
    path('display/', displayPageView, name="display"),
]