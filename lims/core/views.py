from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'core/index.html'


class HelpPageView(TemplateView):
    template_name = 'core/help.html'
