from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'lab'

urlpatterns = [
    path('', TemplateView.as_view(), name='home'),
    path('reagents/', views.ReagentsListView.as_view(), name='reagents'),
    path('methodics/', views.MethodicsListView.as_view(), name='methodics'),
    path('reagents/<int:reagent_id>/', views.ReagentDetailView.as_view(), name='reagent_detail'),
    path('methodics/<int:methodic_id>/', views.MethodicDetailView.as_view(), name='methodic_detail'),
]
