#!/usr/bin/python
# This is the client interface
from Tkinter import *
from PIL import ImageTk, Image
from threading import *
import socket, os

def recv(sock):
	# Look for the response
	while True:
		data = sock.recv(1024)
		if data == '':
			mylist.insert(END, "Host disconnect")
			sock.close()
			return
		else:
			print data
			mylist.insert(END, "<Host> " + data)

def connect():
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Connect the socket to the port where the server is listening
	host = ''
	port = 12345
	welcome = 'connecting to %s chat room' % host
	mylist.insert(END, welcome)
	try:
		sock.connect((host, port))
		data = sock.recv(1024)
		mylist.insert(END, data)
	except Exception, e:
		mylist.insert(END, "connection failed")
		#sys.exit(0)

	return sock

def sendMessage(sock):
	message = Message.get()
	# send message
	mylist.insert(END, "<You> " + message)
	mylist.yview_scroll(1, 'units')
	sock.send(message) 
	Message.delete(0, END)

def keyboardMessage(event, sock):
	output = Message.get()
	sock.send(output)
	mylist.insert(END, "<You> " + output)
	mylist.yview_scroll(1, 'units') 
	Message.delete(0, END)

def main():
	global mylist, Message
	root = Tk()
	#root.geometry('400x400+800+400')
	root.title("Samsung ChatRoom")
	img = PhotoImage(file="120430.gif")
	root.tk.call('wm', 'iconphoto', root._w, img)
	
	# screen
	scrollbar = Scrollbar(root)
	scrollbar.pack(side=RIGHT, fill=Y)
	mylist = Listbox(root, yscrollcommand=scrollbar.set)
	mylist.pack(side=TOP, fill=BOTH)
	scrollbar.config(command=mylist.yview)

	message = Label(root, text="Your message:", justify=LEFT)
	message.pack(side = LEFT)
	Message = Entry(root, bd=5, width = 50)
	Message.focus_set()
	Message.pack(side=LEFT)
	
	sock = connect()
	# recv message
	p = Thread(target=recv, args=(sock,))
	p.start()

	btn = Button(root, text="Send", fg="#a1dbcd", bg="#383a39", command=lambda:sendMessage(sock))
	btn.pack(side=RIGHT)
	root.bind("<Return>", lambda event, sock=sock:keyboardMessage(event, sock))

	root.mainloop()
	return sock
############################################################
# Main function
if __name__ == "__main__":
    sock= main()
    sock.send("client disconnect")
    sock.close()
    os._exit(1)
