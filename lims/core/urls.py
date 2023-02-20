from django.contrib.auth.views import LoginView
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('help/', views.HelpPageView.as_view(), name='help'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:profile_id>', views.ProfileView.as_view(), name='profile'),
    path('password_reset/', views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_<int:user_id>/', views.PasswordResetValidateView.as_view(), name="password_reset_validate"),
    path('password_reset_completed/', TemplateView.as_view(template_name='core/password_reset_complete.html'), name='password_reset_completed'),
]
