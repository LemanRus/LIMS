from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from .forms import *
from .models import Reagent, Methodic, Equipment, Contract, Protocol, TechnicalMaintenance, Bid, Invoice, Record


class ReagentsListView(LoginRequiredMixin, ListView):
    model = Reagent
    template_name = "lab/reagents_list.html"
    context_object_name = "reagents"
    login_url = '/login/'


class MethodicsListView(LoginRequiredMixin, ListView):
    model = Methodic
    template_name = "lab/methodics_list.html"
    context_object_name = "methodics"
    login_url = '/login/'


class EquipmentListView(LoginRequiredMixin, ListView):
    model = Equipment
    template_name = "lab/equipment_list.html"
    context_object_name = "equipment"
    login_url = '/login/'


class ContractsListView(LoginRequiredMixin, ListView):
    model = Contract
    template_name = "lab/contracts_list.html"
    context_object_name = "contracts"
    login_url = '/login/'


class ProtocolsListView(LoginRequiredMixin, ListView):
    model = Protocol
    template_name = "lab/protocols_list.html"
    context_object_name = "protocols"
    login_url = '/login/'


class ReagentDetailView(LoginRequiredMixin, DetailView):
    model = Reagent
    template_name = "lab/reagent_detail.html"
    context_object_name = "reagent"
    pk_url_kwarg = "reagent_id"
    login_url = '/login/'


class ReagentCreateView(LoginRequiredMixin, CreateView):
    form_class = ReagentCreateForm
    template_name = 'lab/reagent_create.html'
    success_url = reverse_lazy('lab:reagents')
    login_url = '/login/'


class MethodicDetailView(LoginRequiredMixin, DetailView):
    model = Methodic
    template_name = 'lab/methodic_detail.html'
    context_object_name = 'methodic'
    pk_url_kwarg = 'methodic_id'
    login_url = '/login/'


class MethodicCreateView(LoginRequiredMixin, CreateView):
    form_class = MethodicCreateForm
    template_name = 'lab/methodic_create.html'
    success_url = reverse_lazy('lab:methodics')
    login_url = '/login/'


class ContractDetailView(LoginRequiredMixin, DetailView):
    model = Contract
    template_name = 'lab/contract_detail.html'
    context_object_name = 'contract'
    pk_url_kwarg = 'contract_id'
    login_url = '/login/'


class ContractCreateView(LoginRequiredMixin, CreateView):
    model = Contract
    form_class = ContractCreateForm
    login_url = '/login/'


class ProtocolDetailView(LoginRequiredMixin, DetailView):
    model = Protocol
    template_name = 'lab/protocol_detail.html'
    context_object_name = 'protocol'
    pk_url_kwarg = 'protocol_id'
    login_url = '/login/'


class ProtocolCreateView(LoginRequiredMixin, CreateView):
    model = Protocol
    login_url = '/login/'


class EquipmentDetailView(LoginRequiredMixin, DetailView):
    model = Equipment
    template_name = 'lab/equipment_detail.html'
    context_object_name = 'equipment'
    pk_url_kwarg = 'equipment_id'
    login_url = '/login/'


class EquipmentCreateView(LoginRequiredMixin, CreateView):
    model = Equipment
    form_class = EquipmentCreateForm
    template_name = 'lab/equipment_create.html'
    login_url = '/login/'


class BidsListView(LoginRequiredMixin, ListView):
    model = Bid
    template_name = "lab/bids_list.html"
    context_object_name = "bids"
    login_url = '/login/'


class BidDetailView(LoginRequiredMixin, DetailView):
    model = Bid
    template_name = 'lab/bid_detail.html'
    context_object_name = 'bid'
    pk_url_kwarg = 'bid_id'
    login_url = '/login/'


class BidCreateView(LoginRequiredMixin, CreateView):
    model = Bid
    template_name = 'lab/bid_create.html'
    form_class = BidCreateForm
    login_url = '/login/'


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    model = Invoice
    template_name = 'lab/invoice_detail.html'
    context_object_name = 'invoice'
    pk_url_kwarg = 'invoice_id'
    login_url = '/login/'


class InvoiceCreateView(LoginRequiredMixin, CreateView):
    model = Invoice
    form_class = InvoiceCreateForm
    login_url = '/login/'


class InvoicesListView(LoginRequiredMixin, ListView):
    model = Invoice
    template_name = "lab/invoices_list.html"
    context_object_name = "invoices"
    login_url = '/login/'


class MaintenanceCreateView(LoginRequiredMixin, CreateView):
    form_class = MaintenanceCreateForm
    template_name = 'lab/maintenance_create.html'
    success_url = reverse_lazy('lab:equipment')
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class(initial=request.GET)}
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST, request.FILES)
    #     context = {}
    #     if form.is_valid():
    #         maintenance = form.save(commit=False)
    #         maintenance.save()
    #         print(form.cleaned_data)
    #         for eq in form.cleaned_data.get('equipment'):
    #             eq.maintenance.add(*TechnicalMaintenance.objects.filter(pk=maintenance.pk))
    #             print(maintenance)
    #             eq.save()
    #         context['form'] = self.form_class
    #         return redirect(reverse('lab:equipment'))
    #     else:
    #         context['form'] = self.form_class

        # return render(request, self.template_name, context)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'lab/dashboard.html'
    login_url = '/login/'
    last_protocols_query = Protocol.objects.order_by('close_date')
    recent_maintenance_query = TechnicalMaintenance.objects.order_by('next_date')
    extra_context = {"test": "Test test", "protocols": last_protocols_query, "next_maintenances": recent_maintenance_query}


class NotebookView(LoginRequiredMixin, ListView):
    template_name = 'lab/notebook.html'
    model = Record
    context_object_name = 'records'
    paginate_by = 30
    ordering = ['-date_created']
    login_url = '/login/'


class RecordCreateView(LoginRequiredMixin, CreateView):
    template_name = 'lab/record_create.html'
    login_url = '/login'
    form_class = RecordCreateForm
    success_url = reverse_lazy('lab:notebook')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            record = form.save(commit=False)
            record.author = request.user
            record.date_pub = timezone.now()
            record.save()
            context['form'] = self.form_class
            return redirect(reverse('lab:notebook'))
        else:
            context['form'] = self.form_class
            return render(request, self.template_name, context)

