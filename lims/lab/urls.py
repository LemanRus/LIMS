from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'lab'

urlpatterns = [
    path('', TemplateView.as_view(), name='home'),
    path('reagents/', views.ReagentsListView.as_view(), name='reagents'),
    path('reagents/create/', views.ReagentCreateView.as_view(), name='reagent_create'),
    path('reagents/<int:reagent_id>/', views.ReagentDetailView.as_view(), name='reagent_detail'),

    path('methodics/', views.MethodicsListView.as_view(), name='methodics'),
    path('methodics/create/', views.MethodicCreateView.as_view(), name='methodic_create'),
    path('methodics/<int:methodic_id>/', views.MethodicDetailView.as_view(), name='methodic_detail'),

    path('equipment/', views.EquipmentListView.as_view(), name='equipment'),
    path('equipment/create/', views.EquipmentCreateView.as_view(), name='equipment_create'),
    path('equipment/<int:equipment_id>/', views.EquipmentDetailView.as_view(), name='equipment_detail'),

    path('contracts/', views.ContractsListView.as_view(), name='contracts'),
    path('contracts/create/', views.ContractCreateView.as_view(), name='contract_create'),
    path('contracts/<int:contract_id>/', views.ContractDetailView.as_view(), name='contract_detail'),

    path('protocols/', views.ProtocolsListView.as_view(), name='protocols'),
    path('protocols/create/', views.ProtocolCreateView.as_view(), name='protocol_create'),
    path('protocols/<int:protocol_id>/', views.ProtocolDetailView.as_view(), name='protocol_detail'),

    path('bids/', views.BidsListView.as_view(), name='bids'),
    path('bids/create/', views.BidCreateView.as_view(), name='bid_create'),
    path('protocols/<int:protocol_id>/', views.BidDetailView.as_view(), name='bid_detail'),

    path('invoices/', views.InvoicesListView.as_view(), name='invoices'),
    path('invoices/create/', views.InvoiceCreateView.as_view(), name='invoice_create'),
    path('invoices/<int:invoice_id>/', views.InvoiceDetailView.as_view(), name='invoice_detail'),

    path('maintenance/create/', views.MaintenanceCreateView.as_view(), name='maintenance_create'),

    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('notebook/', views.NotebookView.as_view(), name='notebook'),
]
