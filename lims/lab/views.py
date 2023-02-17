from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from .forms import MethodicCreateForm
from .models import Reagent, Methodic, Equipment, Contract, Protocol, TechnicalMaintenance


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


class ContractDetailView(LoginRequiredMixin, DetailView):
    model = Contract
    template_name = 'lab/contract_detail.html'
    context_object_name = 'contract'
    pk_url_kwarg = 'contract_id'
    login_url = '/login/'


class ProtocolDetailView(LoginRequiredMixin, DetailView):
    model = Protocol
    template_name = 'lab/protocol_detail.html'
    context_object_name = 'protocol'
    pk_url_kwarg = 'protocol_id'
    login_url = '/login/'


class EquipmentDetailView(LoginRequiredMixin, DetailView):
    model = Equipment
    template_name = 'lab/equipment_detail.html'
    context_object_name = 'equipment'
    pk_url_kwarg = 'equipment_id'
    login_url = '/login/'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'lab/dashboard.html'
    login_url = '/login/'
    last_protocols_query = Protocol.objects.all()
    recent_maintenance_query = TechnicalMaintenance.objects.order_by('next_date')
    extra_context = {"test": "Test test", "protocols": last_protocols_query, "next_maintenances": recent_maintenance_query}
