from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'lab'

urlpatterns = [
    path('', TemplateView.as_view(), name='home'),
    path('reagents/', views.ReagentsListView.as_view(), name='reagents'),
    path('methodics/', views.MethodicsListView.as_view(), name='methodics'),
    path('equipment/', views.EquipmentListView.as_view(), name='equipment'),
    path('contracts/', views.ContractsListView.as_view(), name='contracts'),
    path('protocols/', views.ProtocolsListView.as_view(), name='protocols'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('reagents/<int:reagent_id>/', views.ReagentDetailView.as_view(), name='reagent_detail'),
    path('methodics/<int:methodic_id>/', views.MethodicDetailView.as_view(), name='methodic_detail'),
]
