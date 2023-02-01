#!/var/www/argentum93/data/djangoenv/bin/python3
# -*- coding: utf-8 -*-

import sys, os

# Add a custom Python path.
sys.path.insert(0, '/var/www/argentum93/data/www/lims.in-chemistry.ru/lims')
sys.path.insert(1, '/var/www/argentum93/data/djangoenv/lib/python3.6/site-packages ')

os.chdir("/var/www/argentum93/data/www/lims.in-chemistry.ru/")

os.environ['DJANGO_SETTINGS_MODULE'] = 'lims.settings'

import django

django.setup()

from django.core.handlers import wsgi

application = wsgi.WSGIHandler()

import wsgiref.handlers

if __name__ == '__main__':
    wsgiref.handlers.CGIHandler().run(application)