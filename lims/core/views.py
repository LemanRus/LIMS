from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<p>LIMS come soon!</p>"
                        "<p>Stay with us and be patient.</p>")
