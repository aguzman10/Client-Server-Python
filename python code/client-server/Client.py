import socket

s = socket.socket()
host = 'localhost'
port = 9999

s.connect((host,port))

print('Enter your sentence you wish to capatilze: ')
sentence = raw_input()
s.send(sentence)
print('Message after being sent to the server: ')
print (s.recv(1024))
s.close
