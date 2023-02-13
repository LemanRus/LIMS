from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'core/home.html'


class HelpPageView(TemplateView):
    template_name = 'core/help.html'


def logout_view(request):
    logout(request)
    return redirect(reverse("core:home"))
