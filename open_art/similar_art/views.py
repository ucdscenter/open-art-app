from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	html = 'similar_art/home.html'
	ctxt = {}
	return render(request, html, ctxt)

def prototype(request):
	html = 'similar_art/prototype.html'
	ctxt = {}
	return render(request, html, ctxt)