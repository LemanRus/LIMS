from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ManyToManyField
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.apps import apps

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
    paginate_by = 15
    login_url = '/login/'


class EquipmentListView(LoginRequiredMixin, ListView):
    model = Equipment
    template_name = "lab/equipment_list.html"
    context_object_name = "equipment"
    paginate_by = 15
    login_url = '/login/'


class ContractsListView(LoginRequiredMixin, ListView):
    model = Contract
    template_name = "lab/contracts_list.html"
    context_object_name = "contracts"
    paginate_by = 15
    login_url = '/login/'


class ProtocolsListView(LoginRequiredMixin, ListView):
    model = Protocol
    template_name = "lab/protocols_list.html"
    context_object_name = "protocols"
    paginate_by = 15
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


class ReagentUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ReagentCreateForm
    model = Reagent
    template_name = 'lab/reagent_update.html'
    pk_url_kwarg = 'reagent_id'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('lab:reagent_detail', kwargs={'reagent_id': self.object.pk})


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


class MethodicUpdateView(LoginRequiredMixin, UpdateView):
    form_class = MethodicCreateForm
    model = Methodic
    template_name = 'lab/methodic_update.html'
    pk_url_kwarg = 'methodic_id'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('lab:methodic_detail', kwargs={'methodic_id': self.object.pk})


class ContractDetailView(LoginRequiredMixin, DetailView):
    model = Contract
    template_name = 'lab/contract_detail.html'
    context_object_name = 'contract'
    pk_url_kwarg = 'contract_id'
    login_url = '/login/'


class ContractCreateView(LoginRequiredMixin, CreateView):
    form_class = ContractCreateForm
    template_name = 'lab/contract_create.html'
    success_url = reverse_lazy('lab:contracts')
    login_url = '/login/'


class ContractUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ContractCreateForm
    model = Contract
    template_name = 'lab/contract_update.html'
    pk_url_kwarg = 'contract_id'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('lab:contract_detail', kwargs={'contract_id': self.object.pk})


class ProtocolDetailView(LoginRequiredMixin, DetailView):
    model = Protocol
    template_name = 'lab/protocol_detail.html'
    context_object_name = 'protocol'
    pk_url_kwarg = 'protocol_id'
    login_url = '/login/'


class ProtocolCreateView(LoginRequiredMixin, CreateView):
    form_class = ProtocolCreateForm
    template_name = 'lab/protocol_create.html'
    success_url = reverse_lazy('lab:protocols')
    login_url = '/login/'


class EquipmentDetailView(LoginRequiredMixin, DetailView):
    model = Equipment
    template_name = 'lab/equipment_detail.html'
    context_object_name = 'equipment'
    pk_url_kwarg = 'equipment_id'
    login_url = '/login/'


class EquipmentCreateView(LoginRequiredMixin, CreateView):
    form_class = EquipmentCreateForm
    template_name = 'lab/equipment_create.html'
    success_url = reverse_lazy('lab:equipment')
    login_url = '/login/'


class EquipmentUpdateView(LoginRequiredMixin, UpdateView):
    form_class = EquipmentCreateForm
    model = Equipment
    template_name = 'lab/equipment_update.html'
    pk_url_kwarg = 'equipment_id'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('lab:equipment_detail', kwargs={'equipment_id': self.object.pk})


class BidsListView(LoginRequiredMixin, ListView):
    model = Bid
    template_name = "lab/bids_list.html"
    context_object_name = "bids"
    paginate_by = 15
    login_url = '/login/'


class BidDetailView(LoginRequiredMixin, DetailView):
    model = Bid
    template_name = 'lab/bid_detail.html'
    context_object_name = 'bid'
    pk_url_kwarg = 'bid_id'
    login_url = '/login/'


class BidCreateView(LoginRequiredMixin, CreateView):
    form_class = BidCreateForm
    template_name = 'lab/bid_create.html'
    success_url = reverse_lazy('lab:bids')
    login_url = '/login/'


class BidUpdateView(LoginRequiredMixin, UpdateView):
    form_class = BidCreateForm
    model = Bid
    template_name = 'lab/bid_update.html'
    pk_url_kwarg = 'bid_id'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('lab:bid_detail', kwargs={'bid_id': self.object.pk})


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    model = Invoice
    template_name = 'lab/invoice_detail.html'
    context_object_name = 'invoice'
    pk_url_kwarg = 'invoice_id'
    login_url = '/login/'


class InvoiceCreateView(LoginRequiredMixin, CreateView):
    form_class = InvoiceCreateForm
    template_name = 'lab/invoice_create.html'
    success_url = reverse_lazy('lab:invoices')
    login_url = '/login/'


class InvoicesListView(LoginRequiredMixin, ListView):
    model = Invoice
    template_name = "lab/invoices_list.html"
    context_object_name = "invoices"
    paginate_by = 15
    login_url = '/login/'


class InvoiceUpdateView(LoginRequiredMixin, UpdateView):
    form_class = InvoiceCreateForm
    model = Invoice
    template_name = 'lab/invoice_update.html'
    pk_url_kwarg = 'invoice_id'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('lab:invoice_detail', kwargs={'invoice_id': self.object.pk})


class MaintenanceCreateView(LoginRequiredMixin, CreateView):
    form_class = MaintenanceCreateForm
    template_name = 'lab/maintenance_create.html'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('lab:equipment_detail', kwargs={'equipment_id': self.request.POST.get('equipment')})

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['next_maintenances'] = TechnicalMaintenance.objects.order_by('next_date')[:6]
        context['nearest_reagents'] = Reagent.objects.order_by('best_before')[:6]
        context['invoices_in_progress'] = Invoice.objects.filter(status='w')[:6]
        context['protocols'] = Protocol.objects.order_by('close_date')[:6]
        return context


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


class AuditTrailView(LoginRequiredMixin, TemplateView):
    template_name = 'lab/audit_trail.html'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        changed_records = {}
        for model in apps.get_models():
            for item in model.objects.all():
                fields = {}
                if hasattr(item, 'history'):
                    if hasattr(item.history, 'all'):
                        for history_record in item.history.all():
                            field_names = {}
                            for field in item._meta.get_fields():
                                if hasattr(field, 'verbose_name'):
                                    if isinstance(field, ManyToManyField):
                                        previous_record = history_record.prev_record
                                        if previous_record:
                                            delta = history_record.diff_against(previous_record)
                                        else:
                                            delta = history_record.diff_against(history_record)
                                        for change in delta.changes:
                                            if isinstance(change.new, list) and field.name == change.field:
                                                last_m2m = {field.verbose_name: change.new}
                                                for changed_m2m_field in last_m2m.get(field.verbose_name):
                                                    m2m_values = {}
                                                    for name, pk in changed_m2m_field.items():
                                                        m2m_model = apps.get_model('lab', name)
                                                        if m2m_model != model:
                                                            m2m_values[m2m_model._meta.verbose_name + ' id' + str(
                                                                pk)] = m2m_model.objects.get(pk=pk)
                                                            field_names.update(m2m_values)
                                    else:
                                        temp = {k: v for k, v in
                                                [(field.verbose_name, getattr(history_record, field.name))]}
                                        field_names.update(temp)
                            fields[history_record] = field_names
                        if fields:
                            if hasattr(item, 'name'):
                                changed_records[item.name] = fields
                            else:
                                changed_records[str(item.number)] = fields
        context['constructed_history'] = changed_records
        return context
