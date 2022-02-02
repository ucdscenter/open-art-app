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
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    
    path('change-password', auth_views.PasswordChangeView.as_view(
        template_name='registration/change-password.html'
    ), name="change-password"),
    path('change-password-done', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/change-password-done.html'
    ), name="password_change_done"),

    path('reset', auth_views.PasswordResetView.as_view(
        template_name='registration/reset.html'
    ), name='password_reset'),
    path('reset-done', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/reset-done.html'
    ), name='password_reset_done'),
    path('reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/reset-confirm.html'
    ), name='password_reset_confirm'),
    path('reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/reset-complete.html'
    ), name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)