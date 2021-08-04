from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404
# Create your views here.

def index(request):
	html = 'similar_art/home.html'
	ctxt = {}
	return render(request, html, ctxt)

def prototype(request):
	html = 'similar_art/prototype.html'
	ctxt = {}
	return render(request, html, ctxt)

def initial_results(request):
	html = 'similar_art/initial_results.html'
	ctxt = {}
	return render(request, html, ctxt)

def pdf_view(request):
	print(request.GET.get('fname'))

	return FileResponse(open('similar_art/static/similar_art/papers/' + request.GET.get('fname'), 'rb'), content_type='application/pdf')
