import socket
import time , sys
from loading import *
s = socket.socket()
load()
print('')
host = socket.gethostname()
print('host server name ',host)
port = 8081
s.bind((host,port))
print('waiting for incoming connection')
s.listen(1)
conn , addr = s.accept()
load()
print('')
print(addr,'has connected to sever and now online ')
while 1:
    message = input(str('>>'))
    message = message.encode()
    conn.send(message)
    incomming_message = conn.recv(1024)
    incomming_message  = incomming_message.decode()
    print('client : ',incomming_message )
    
