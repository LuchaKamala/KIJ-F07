import socket
import sys
import Counter
import threading
import DiffieHellman

threads = []

class Config:
    def __init__(self):
        self.key = ""
        self.message = ""
        self.sending_state = False

class Server(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket
        self.size = 1024
        self.counter = Counter.counter()

    # Proses Penerimaan
    def run(self):
        while True:
            data = self.socket.recv(self.size)

            # Menerima untuk mengirim kembali chiper text
            if data and config.sending_state:
                public_b = int(data)
                config.key = diffie_hellman.generateKey(public_b, secret_a)
                config.key = str(config.key)

                config.message = username + ": " + config.message

                encrypted = self.counter.encrypt(config.key, config.message)
                self.socket.send(encrypted)
                config.sending_state = False

            # Menerima untuk ditampilkan
            elif data and not config.sending_state:
                secret_b = 5
                public_b = diffie_hellman.generatePublicNumber(secret_b)
                public_b = str(public_b)
                self.socket.send(public_b)

                config.message = self.socket.recv(self.size)

                public_a = int(data)
                config.key = diffie_hellman.generateKey(public_a, secret_b)
                config.key = str(config.key)

                decrypted = self.counter.decrypt(config.key, config.message)
                print "enkripsi: " + config.message
                print "key: " + config.key
                print decrypted
            else:
                continue

host = '192.168.43.125'
port = 5000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
username = raw_input("insert your username: ")

try:
    server = Server(s)
    server.start()
    threads.append(server)

    config = Config()
    diffie_hellman = DiffieHellman.KeyExchange()

    # Proses Pengiriman
    while True:
        config.message = raw_input()
        config.sending_state = True

        secret_a = 6
        public_a = diffie_hellman.generatePublicNumber(secret_a)
        public_a = str(public_a)

        s.send(public_a)

except KeyboardInterrupt:
    s.close()
    for s in threads:
        s.join()
    sys.exit(0)