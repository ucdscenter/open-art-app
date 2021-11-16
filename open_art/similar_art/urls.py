from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prototype', views.prototype, name='prototype'),
    path('initial_results', views.initial_results, name='initial_results'),
    path('viewpdf', views.pdf_view, name="pdf_view"),
    path('art_images', views.images, name = 'art_images')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)