import socket
import sys
import Counter
import threading

threads = []

class Server(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket
        self.size = 1024
        self.counter = Counter.counter()

    def run(self):
        while True:
            data = self.socket.recv(1024)
            if data != "\0":
                decrypted = self.counter.decrypt(key, data)
                print decrypted
            else: continue

host = 'localhost'
port = 5000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
username = raw_input("insert your username: ")

try:
    while True:
        server = Server(s)
        server.start()
        threads.append(server)

        key = "irfan"
        message = raw_input()
        message = username + ": " + message
        counter = Counter.counter()
        encrypted = counter.encrypt(key, message)
        s.send(encrypted)

except KeyboardInterrupt:
    s.close()
    for s in threads:
        s.join()
    sys.exit(0)