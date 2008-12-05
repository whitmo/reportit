#import cgi
#from paste.deploy import CONFIG
from paste.deploy.config import ConfigMiddleware
from selector import ByMethod
#from webob import Response
from reportedit import wsgi 
import static


# def application(environ, start_response):
#     # Note that usually you wouldn't be writing a pure WSGI
#     # application, you might be using some framework or
#     # environment.  But as an example...
#     start_response('200 OK', [('Content-type', 'text/html')])
#     greeting = CONFIG['greeting']
#     content = [
#         '<html><head><title>%s</title></head>\n' % greeting,
#         '<body><h1>%s!</h1>\n' % greeting,
#         '<table border=1>\n',
#         ]
#     items = environ.items()
#     items.sort()
#     for key, value in items:
#         content.append('<tr><td>%s</td><td>%s</td></tr>\n'
#                         % (key, cgi.escape(repr(value))))
#     content.append('</table></body></html>')
#     return content

                        
class FormHandler(ByMethod): 

    @staticmethod
    def GET(request, start_response):
        static = get_static(request)
        request.environ['PATH_INFO'] = '/form.html'
        return static(request.environ, start_response)

    def POST(self, request, start_response): 
        ''' 
        persist or return error
        ''' 
        pass



def get_static(req):
    return req.environ['paste.config']['reportedit.static_app']

def get_static_res(req, start_response):
    app = get_static(req)
    ec = req.environ.copy()
    ec['PATH_INFO'] = "/" + ec['selector.vars']['filename']
    return app(ec, start_response)

def make_app(global_conf, **kw):
    conf = global_conf.copy()
    conf.update(kw)
    magics = [static.StringMagic(**conf)]
    res_spec = conf.get('resource', 'reportedit:resource').split(":")
    if len(res_spec) == 2:
        pkg, res = res_spec
        static_app = wsgi.shock_wrap(pkg, res, magics=magics)
    else:
        res = res_spec[0]
        static_app = static.Shock(res, magics=magics)

    conf['reportedit.static_app'] = static_app
    app = wsgi.AutoSelector(wrap=wsgi.WebObWrapper)
    app.add("/", FormHandler())

    app = ConfigMiddleware(app, conf)
    return app
