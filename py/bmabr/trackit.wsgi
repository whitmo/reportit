import os, sys
sys.path.append('/usr/local/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'webmaps.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
