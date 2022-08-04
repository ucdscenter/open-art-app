from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import FileResponse, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *
from .models import Art
from PIL import Image


from similar_art.similar_tree import *
import pickle
import vptree
from scipy import spatial

#tree = pickle.load(open('similar_art/data/wikiarts_tree.txt', 'rb'))
# Create your views here.

def index(request):
	html = 'similar_art/home.html'
	ctxt = {}
	return render(request, html, ctxt)

def prototype(request):
	def cosine_similarity(vec1, vec2):
		return spatial.distance.cosine(vec1, vec2)

	def euclidean(vec1,vec2):
		return spatial.distance.euclidean(vec1[0],vec2[0])

	tree = pickle.load(open('similar_art/data/wikiarts_tree.txt', 'rb'))

	
	html = 'similar_art/prototype.html'
	if request.method == 'GET':
		form = ArtForm()
		ctxt = {'form' : form}
		return render(request, html, ctxt)
	else:
		form = ArtForm(request.POST, request.FILES)
		
		if form.is_valid():
			im = Image.open(request.FILES['art_main_Img'])

			results = extract_similar_images(im, tree)
			results = similar_image_paths(results)
			form.save()
			newForm = ArtForm()
			ctxt = {'form' : newForm, 'message': 'Your image was uploaded successfully', 'results' : results}
			return render(request, html, ctxt)
		else:
			im = Image.open(request.FILES['art_main_Img'])
			newForm = ArtForm()
			ctxt = {'form' : newForm, 'message': 'Your image failed to upload'}
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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
