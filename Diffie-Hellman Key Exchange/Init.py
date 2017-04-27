import socket
import sys
import threading
import Counter
import DiffieHellman

class Config:
    def __init__(self):
        self.key = ""
        self.message = ""
        self.sending_state = False
        self.secret_a = int()
        self.username = ""

class Server:
    def __init__(self):
        self.host = 'localhost'
        self.port = 5000
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []
        self.counter = Counter.counter()

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
        config.username = raw_input("insert your username: ")
        try:
            while True:
                # handle the server socket
                self.client_socket, self.client_address = self.server.accept()
                client = Client(self.client_socket, self.client_address)
                client.start()

                # Proses Pengiriman
                while True:
                    config.message = raw_input()
                    config.sending_state = True

                    config.secret_a = 6
                    self.public_a = diffie_hellman.generatePublicNumber(config.secret_a)
                    self.public_a = str(self.public_a)

                    self.client_socket.send(self.public_a)

        except KeyboardInterrupt:
            self.server.close()

class Client(threading.Thread):
    def __init__(self, client, address):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024
        self.counter = Counter.counter()

    # Proses Penerimaan
    def run(self):
        try:
            while True:
                self.message = self.client.recv(self.size)
                if self.message and config.sending_state:
                    public_b = int(self.message)
                    config.key = diffie_hellman.generateKey(public_b, config.secret_a)
                    config.key = str(config.key)

                    config.message = config.username + ": " + config.message

                    encrypted = self.counter.encrypt(config.key, config.message)
                    self.client.send(encrypted)
                    config.sending_state = False

                elif self.message and not config.sending_state:
                    secret_b = 5
                    public_b = diffie_hellman.generatePublicNumber(secret_b)
                    public_b = str(public_b)
                    self.client.send(public_b)

                    config.message = self.client.recv(self.size)

                    public_a = int(self.message)
                    config.key = diffie_hellman.generateKey(public_a, secret_b)
                    config.key = str(config.key)

                    decrypted = self.counter.decrypt(config.key, config.message)
                    print decrypted
        except KeyboardInterrupt:
            self.client.close()

if __name__ == "__main__":
    config = Config()
    diffie_hellman = DiffieHellman.KeyExchange()
    s = Server()
    s.run()