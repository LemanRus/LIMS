from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'lab'

urlpatterns = [
    path('', TemplateView.as_view(), name='home'),
    path('reagents/', views.ReagentsListView.as_view(), name='reagents'),
    path('methodics/', views.MethodicsListView.as_view(), name='methodics'),
]
