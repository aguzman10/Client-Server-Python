import socket

s = socket.socket()
host = 'localhost'
port = 9999
s.bind((host,port))

s.listen(5)
while True:
    c, address = s.accept()
    sen = c.recv(1024)
    sent = sen.upper()
    c.send(sent)
    print ('Connection ready with ', address)
    c.send('Thank you for connecting')
    c.close
