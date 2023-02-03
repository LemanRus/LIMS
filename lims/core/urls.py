from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('help/', views.HelpPageView.as_view(), name='help'),
]
