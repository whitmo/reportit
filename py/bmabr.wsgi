import os, sys
sys.path.append('/usr/local/reportit')
os.environ['DJANGO_SETTINGS_MODULE'] = 'py.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
