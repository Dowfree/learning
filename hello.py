def application(environ, start_response):
    method = environ('REQUEST_METHOD')
    start_response('200 OK', [('Content_Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

