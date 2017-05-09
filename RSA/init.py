import select
import socket
import sys
import threading
from ImplementRSA import RSA

class Server:
    def __init__(self):
        self.host = ''
        self.port = 50000
        self.backlog = 5
        self.size = 1024
        self.server = None

    def open_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host,self.port))
            self.server.listen(5)
        except socket.error, (value,message):
            if self.server:
                self.server.close()
            print "Could not open socket: " + message
            sys.exit(1)

    def run(self):
        self.open_socket()
        try:
            while True:
                # handle the server socket
                self.client_socket, self.client_address = self.server.accept()
                self.public_e = int(self.client_socket.recv(self.size))
                self.public_n = int(self.client_socket.recv(self.size))

                self.rsa = RSA()
                p = self.rsa.getPrimeP()
                q = self.rsa.getPrimeQ(p)
                n = self.rsa.getValueN(p, q)
                m = self.rsa.getValueM(p, q)
                e = self.rsa.getValueE(m)
                d = self.rsa.getValueD(m, e)

                self.client_socket.send(str(e))
                self.client_socket.send(str(n))

                c = Client(self.client_socket, self.client_address, d, n)
                c.start()

                while True:
                    message = raw_input("Message: ")
                    chiper = self.rsa.encryption(message, self.public_e, self.public_n)
                    self.client_socket.send(chiper)

        except KeyboardInterrupt:
            self.server.close()

class Client(threading.Thread):
    def __init__(self, client, address, private_e, private_n):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024
        self.private_e = private_e
        self.private_n = private_n
        self.rsa = RSA()

    def run(self):
        try:
            while True:
                chiper = self.client.recv(self.size)
                if chiper:
                    plain = self.rsa.decryption(chiper, self.private_e, self.private_n)
                    print plain
                else:
                    continue
        except KeyboardInterrupt:
            self.client.close()

if __name__ == "__main__":
    s = Server()
    s.run()