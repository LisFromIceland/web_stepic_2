from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

def app(environ, start_response):
        data parse_qs(environ['QUERY_STRING'])
        start_response("200 OK",
            [("Content-Type", "text/plain")])
	return iter([data])

httpd = make_server('http://127.0.0.1/hello/',  app)
httpd = make_server('http://127.0.0.1', 8080, app)
