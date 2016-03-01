import urlparse

def application(environ,start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	body = ''
	li = urlparse.parse_qsl(environ['QUERY_STRING'])
	start_response(status, headers)
	for i in li:
		body = body + i[0] + '=' + i[1] + '\n'
	return body
