from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prototype', views.prototype, name='prototype'),
    path('initial_results', views.initial_results, name='initial_results'),
    path('viewpdf', views.pdf_view, name="pdf_view")
]