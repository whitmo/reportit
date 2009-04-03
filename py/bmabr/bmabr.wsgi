import os, sys
sys.path.append('/home/ivan/development/bmabr/reportit/py/bmabr')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bmabr.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
