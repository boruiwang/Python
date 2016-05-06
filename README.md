# Python network program

In GroupChatServer, chatServer.py is responsible for sending messages to all
connected clients, which uses select() method to handle multi-users. The server will store all messages into MongoDB.

In socket, host.py uses multi-thread to handle send/recv process.
What's more, I implemented GUI for the client.

In WSGIsever, I built a WSGI server to handle request.
