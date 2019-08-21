#from django.shortcuts import render

from django.views.generic import (
    ListView, DetailView,
)

# Create your views here.

from core.models import Movie

class MovieDetail(DetailView):
    model = Movie
    
class MovieList(ListView):
    model = Movie
