from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prototype', views.prototype, name='prototype'),
    path('initial_results', views.initial_results, name='initial_results'),
    path('viewpdf', views.pdf_view, name="pdf_view"),
    path('art_images', views.images, name = 'art_images'),
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)