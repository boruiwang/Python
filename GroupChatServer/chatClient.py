'''
This file is the chat client which can send the message
to other connected clients.

code reference:
http://www.bogotobogo.com/python/python_network_programming_tcp_server_client_chat_server_chat_client_select.php
'''

import socket, select, sys



def client():
	if(len(sys.argv) < 3) :
		print 'Usage : python chat_client.py hostname port'
		sys.exit()

	host = sys.argv[1]
	port = int(sys.argv[2])
	user_name = raw_input('User name: ')

	s = socket.socket()
	s.settimeout(2)
	# connect to remote host
	try:
		s.connect((host, port))
	except :
		print 'Unable to connect to ' + host
		sys.exit()

	print 'Connected to remote %s. You can start sending messages' %host
	sys.stdout.write('[Me] ');
	sys.stdout.flush()

	while True:
		socket_list = [sys.stdin, s]
		
		ready_2_read,ready_2_write,in_error = select.select(socket_list , [], [])
		for sock in ready_2_read:
			if sock == s:
			# incoming message from remote server, s
				data = sock.recv(4096)
				if not data:
					print '\nDisconnected from chat server'
					sys.exit()
				else :
					#print data
					sys.stdout.write(data)
					sys.stdout.write('[Me] ');
					sys.stdout.flush()
			else :
				# user entered a message
				msg = sys.stdin.readline()
				s.send(user_name + ": " + msg)
				sys.stdout.write('[Me] ');
				sys.stdout.flush() 

if __name__ == "__main__":
	sys.exit(client())