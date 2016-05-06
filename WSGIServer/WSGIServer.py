'''
This is a simple WSGI concurrent server.

reference: https://docs.python.org/2/library/wsgiref.html
'''
import sys, socket, os
#from wsgiref.simple_server import make_server

class WSGIServer():
	def __init__(self, server_address):
		self.address = server_address
		self.header = []

	def set_server(self, socket):
		server_socket = socket.socket()
    	server_socket.bind(self.address)
    	server_socket.listen(1)
    	# Get server host name and port
        host, port = server_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port



'''
def grim_reaper(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,          # Wait for any child process
                os.WNOHANG  # Do not block and return EWOULDBLOCK error
            )
            print(
                'Child {pid} terminated with status {status}'
                '\n'.format(pid=pid, status=status)
            )
        except OSError:
            return

        if pid == 0:  # no more zombies
            return
'''
def make_server(server_address, application):
	#signal.signal(signal.SIGCHLD, grim_reaper)
	server = WSGIServer(server_address)
	server.set_app(application)
	return server

# Every WSGI application must have an application object - a callable
# object that accepts two arguments. For that purpose, we're going to
# use a function (note that you're not limited to a function, you can
# use a class for example). The first argument passed to the function
# is a dictionary containing CGI-style envrironment variables and the
# second variable is the callable object (see PEP 333).
def my_app(environ, start_response):
    status = '200 OK' # HTTP Status
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)
	# HTTP Headers
    headers = [
    	('Content-type', 'text/plain'),
    	('Content-Length', str(len(response_body)))
    ]
    start_response(status, headers)

    # The returned object is going to be printed
    return [response_body]

if __name__ == '__main__':
	httpd = make_server('', 8000, my_app)
	print "Serving on port 8000..."
	# Serve until process is killed
	httpd.serve_forever()