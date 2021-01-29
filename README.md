# Simple-python-socket
A server client socket program using python 

## What is a socket ?
A socket is one endpoint of a two-way communication link between two programs running on the network. A socket is bound to a port number so that the TCP layer can identify the application that data is destined to be sent to. An endpoint is a combination of an IP address and a port number.

## What is the function of a socket?
The socket() function shall create an unbound socket in a communications domain, and return a file descriptor that can be used in later function calls that operate on sockets. The socket() function takes the following arguments: domain. Specifies the communications domain in which a socket is to be created.

## What is socket and its types?
Socket types define the communication properties visible to a user. The Internet family sockets provide access to the TCP/IP transport protocols. Datagram sockets allow processes to use UDP to communicate. ... A datagram socket supports bidirectional flow of messages.

## How socket is created?
A socket is created with no name. A remote process has no way to refer to a socket until an address is bound to the socket. Processes that communicate are connected through addresses. In the Internet family, a connection is composed of local and remote addresses and local and remote ports.

## Can you send and receive on the same socket?
Once connected, a TCP socket can only send and receive to/from the remote machine. This means that you'll need one TCP socket for each client in your application. UDP is not connection-based, you can send and receive to/from anyone at any time with the same socket.
