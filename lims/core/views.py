from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView

from .models import CustomUser


class HomePageView(TemplateView):
    template_name = 'core/home.html'


class HelpPageView(TemplateView):
    template_name = 'core/help.html'


class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'core/profile.html'
    context_object_name = 'profile'
    pk_url_kwarg = 'profile_id'
    login_url = '/login/'


def logout_view(request):
    logout(request)
    return redirect(reverse("core:home"))
