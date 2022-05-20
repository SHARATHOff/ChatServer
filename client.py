import socket , sys, time
c = socket.socket()
host = input('ENTER to host code :')
port = 8081
c.connect((host,port))
print('connected succes')
while 1 :
    incomming_message = c.recv(1024)
    incomming_message = incomming_message .decode()
    print('host : ',incomming_message )
    message = input(str('>>'))
    message = message.encode()
    c.send(message)
    
