from django.http import HttpResponse
from django.shortcuts import render

from .models import MagicSquare

# Create your views here.
def index(request):
	magic_squares = MagicSquare.objects.all()
	return render(request, 'm9/index.html', {'magic_squares' : magic_squares} )
