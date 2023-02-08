from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Reagent, Methodic


class ReagentsListView(ListView):
    model = Reagent
    template_name = "lab/reagents_list.html"
    context_object_name = "reagents"


class MethodicsListView(ListView):
    model = Methodic
    template_name = "lab/methodics_list.html"
    context_object_name = "methodics"

#
# class ReagentDetailView(DetailView):
#     model = Reagent
#     template_name = "lab/reagents_list.html"
#     context_object_name = "reagents"
#
#
# class MethodicDetailView(DetailView):
#     model = Methodic
#     template_name = "lab/methodics_list.html"
#     context_object_name = "methodics"
