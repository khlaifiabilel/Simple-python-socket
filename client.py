import socket
import threading
import sys

#importing of the SHA256 algo  
from Crypto.Hash import SHA256
#importing of the AES algo  
from Crypto.Cipher import AES

hash = SHA256.new()

#Wait for incoming data from server
#.decode is used to turn the message in bytes to a string
def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(str(data.decode("utf-8")))
        except:
            print("You have been disconnected from the server")
            signal = False
            break

#Get host and port
host = input("Host: ")
port = int(input("Port: "))

#Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

#Create new thread to wait for data
receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()

#Send data to server
#str.encode is used to turn the string message into bytes so it can be sent across the network
while True:
    #encryption key 
    hash = SHA256.new()
    message = input()
    hash.update('message')
    hash.digest()
    sock.sendall(str.encode(message))


  git config --global user.email "kalifiabillal@gmail.com"
  git config --global user.name "kalifiabillal"