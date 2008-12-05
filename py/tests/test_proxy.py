from webtest import TestApp
from paste.deploy.loadwsgi import loadapp
import os
import pkg_resources


dist = pkg_resources.Requirement.parse('reportedit')

def setup(tc):
    doc_path = pkg_resources.resource_filename(dist, 'docs')
    gc = dict(data_path='reportedit:tests')
    app2 = loadapp('config:reportedit-conf.ini',
                   name='test',
                   **dict(global_conf=gc, relative_to=doc_path))
    global app
    app = TestApp(app2)

def teardown(tc):
    pass

def test_basic():
    global app
    app.get('/', status=200)
