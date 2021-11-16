from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import FileResponse, Http404
from .forms import *
from .models import Art
# Create your views here.

def index(request):
	html = 'similar_art/home.html'
	ctxt = {}
	return render(request, html, ctxt)

def prototype(request):
	html = 'similar_art/prototype.html'
	if request.method == 'GET':
		form = ArtForm()
		ctxt = {'form' : form}
		return render(request, html, ctxt)
	else:
		form = ArtForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			newForm = ArtForm()
			ctxt = {'form' : newForm, 'message': 'Your image was uploaded successfully'}
			return render(request, html, ctxt)
	
def images(request):
	if request.method == 'GET':
		arts = Art.objects.all()[:20]
		html = 'similar_art/images.html'
		ctxt = {'art_images': arts}
		return render(request, html, ctxt)

def initial_results(request):
	html = 'similar_art/initial_results.html'
	ctxt = {}
	return render(request, html, ctxt)

def pdf_view(request):
	print(request.GET.get('fname'))

	return FileResponse(open('similar_art/static/similar_art/papers/' + request.GET.get('fname'), 'rb'), content_type='application/pdf')
