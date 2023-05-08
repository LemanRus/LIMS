from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'lab'

urlpatterns = [
    path('', TemplateView.as_view(), name='home'),
    path('reagents/', views.ReagentsListView.as_view(), name='reagents'),
    path('reagents/create/', views.ReagentCreateView.as_view(), name='reagent_create'),
    path('reagents/<int:reagent_id>/', views.ReagentDetailView.as_view(), name='reagent_detail'),
    path('reagents/update_reagent-<int:reagent_id>/', views.ReagentUpdateView.as_view(), name='reagent_update'),

    path('methodics/', views.MethodicsListView.as_view(), name='methodics'),
    path('methodics/create/', views.MethodicCreateView.as_view(), name='methodic_create'),
    path('methodics/<int:methodic_id>/', views.MethodicDetailView.as_view(), name='methodic_detail'),
    path('methodics/update_methodic-<int:methodic_id>/', views.MethodicUpdateView.as_view(), name='methodic_update'),

    path('equipment/', views.EquipmentListView.as_view(), name='equipment'),
    path('equipment/create/', views.EquipmentCreateView.as_view(), name='equipment_create'),
    path('equipment/<int:equipment_id>/', views.EquipmentDetailView.as_view(), name='equipment_detail'),
    path('equipment/update_equipment-<int:equipment_id>/', views.EquipmentUpdateView.as_view(),
         name='equipment_update'),

    path('contracts/', views.ContractsListView.as_view(), name='contracts'),
    path('contracts/create/', views.ContractCreateView.as_view(), name='contract_create'),
    path('contracts/<int:contract_id>/', views.ContractDetailView.as_view(), name='contract_detail'),
    path('contracts/update_contract-<int:contract_id>/', views.ContractUpdateView.as_view(),
         name='contract_update'),

    path('protocols/', views.ProtocolsListView.as_view(), name='protocols'),
    path('protocols/create/', views.ProtocolCreateView.as_view(), name='protocol_create'),
    path('protocols/<int:protocol_id>/', views.ProtocolDetailView.as_view(), name='protocol_detail'),

    path('bids/', views.BidsListView.as_view(), name='bids'),
    path('bids/create/', views.BidCreateView.as_view(), name='bid_create'),
    path('bids/<int:bid_id>/', views.BidDetailView.as_view(), name='bid_detail'),
    path('bids/update_bid-<int:bid_id>/', views.BidUpdateView.as_view(),
         name='bid_update'),

    path('invoices/', views.InvoicesListView.as_view(), name='invoices'),
    path('invoices/create/', views.InvoiceCreateView.as_view(), name='invoice_create'),
    path('invoices/<int:invoice_id>/', views.InvoiceDetailView.as_view(), name='invoice_detail'),
    path('invoices/update_invoice-<int:invoice_id>/', views.InvoiceUpdateView.as_view(),
         name='invoice_update'),

    path('maintenance/create/', views.MaintenanceCreateView.as_view(), name='maintenance_create'),

    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('notebook/', views.NotebookView.as_view(), name='notebook'),
    path('notebook/create/', views.RecordCreateView.as_view(), name='record_create'),
    path('audit_trail/', views.AuditTrailView.as_view(), name='audit_trail'),
]
