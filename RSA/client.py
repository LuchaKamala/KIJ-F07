import socket
import sys
import threading
from ImplementRSA import RSA

class Listen(threading.Thread):
    def __init__(self, socket, private_d, private_n):
        threading.Thread.__init__(self)
        self.socket = socket
        self.size = 1024
        self.private_d = private_d
        self.private_n = private_n
        self.rsa = RSA()

    def run(self):
        while True:
            chiper = self.socket.recv(self.size)

            if chiper:
                plain = self.rsa.decryption(chiper, self.private_d, self.private_n)
                print plain
            else:
                continue



host = 'localhost'
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

rsa = RSA()
p = rsa.getPrimeP()
q = rsa.getPrimeQ(p)
n = rsa.getValueN(p, q)
m = rsa.getValueM(p, q)
e = rsa.getValueE(m)
d = rsa.getValueD(m, e)

s.send(str(e))
s.send(str(n))
public_e = int(s.recv(size))
public_n = int(s.recv(size))

threads = []

try:
    listen = Listen(s, d, n)
    listen.start()
    threads.append(listen)

    while True:
        # read from keyboard
        msg = raw_input("Message: ")
        chiper = rsa.encryption(msg, public_e, public_n)
        s.send(chiper)

except KeyboardInterrupt:
    s.close()