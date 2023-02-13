from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView

from .models import Reagent, Methodic


class ReagentsListView(ListView):
    model = Reagent
    template_name = "lab/reagents_list.html"
    context_object_name = "reagents"


class MethodicsListView(ListView):
    model = Methodic
    template_name = "lab/methodics_list.html"
    context_object_name = "methodics"


class ReagentDetailView(DetailView):
    model = Reagent
    template_name = "lab/reagent_detail.html"
    context_object_name = "reagent"
    pk_url_kwarg = "reagent_id"


class MethodicDetailView(DetailView):
    model = Methodic
    template_name = 'lab/methodic_detail.html'
    context_object_name = 'methodic'
    pk_url_kwarg = 'methodic_id'


class DashboardView(View):
    template_name = 'lab/dashboard.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            raise Http404('Недоступно для незарегистрированных пользователей')
