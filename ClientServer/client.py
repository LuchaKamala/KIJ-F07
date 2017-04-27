import socket
import sys
import Counter
import threading

threads = []

class Config:
    def __init__(self):
        self.sending_state = False
        self.key = ""
        self.A = int()
        self.B = int()
        self.secret_a = 6
        self.secret_b = 5
        self.generator = 11
        self.prime = 23
        self.username = ""
        self.message = ""

class Server(threading.Thread):
    def __init__(self, socket, config):
        threading.Thread.__init__(self)
        self.socket = socket
        self.size = 1024
        self.counter = Counter.counter()
        self.config = config

    def run(self):
        while True:
            data = self.socket.recv(1024)
            if data and self.config.sending_state:
                self.config.B = int(data)

                # Generate K
                config.key = (config.B ** config.secret_a) % config.prime
                self.message = config.username + ": " + config.message

                # Enkripsi
                counter = Counter.counter()
                print "key e: " + str(config.key)
                encrypted = counter.encrypt(str(config.key), config.message)

                # Mengirim Message
                self.socket.send(encrypted)
                config.sending_state = False

            elif data and not self.config.sending_state:
                # Decrypt
                config.A = int(data)
                msg = self.socket.recv(1024)
                config.key = (config.A**config.secret_b) % config.prime
                print "key d: " + str(config.key) + " " + msg

                counter = Counter.counter()
                decrypted = counter.decrypt(str(config.key), msg)
                print decrypted
            else:
                continue

host = '10.151.12.157'
port = 5000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

config = Config()
config.username = raw_input("insert your username: ")

try:
    while True:
        server = Server(s, config)
        server.start()
        threads.append(server)

        config.message = raw_input()
        config.sending_state = True

        # Mengirim A
        A = (config.generator ** config.secret_a) % config.prime
        s.send(str(A))

except KeyboardInterrupt:
    s.close()
    for s in threads:
        s.join()
    sys.exit(0)