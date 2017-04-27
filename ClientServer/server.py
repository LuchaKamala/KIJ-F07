import socket
import sys
import threading
import Counter

class Server:
    def __init__(self):
        self.host = 'localhost'
        self.port = 5000
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []
        self.client_list = []

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
                self.client_list.append(self.client_socket)
                c = Client(self.client_socket, self.client_address, self.client_list)
                c.start()
                self.threads.append(c)
        except KeyboardInterrupt:
            self.server.close()
            for c in self.threads:
                c.join()

class Client(threading.Thread):
    def __init__(self, client, address, client_list):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024
        self.client_list = client_list

    def run(self):
        running = 1
        while running:
            data = self.client.recv(self.size)
            if data:
                print "data encrypted: " + data
                print

                for client in self.client_list:
                    if client == self.client:
                        client.send("\0")
                    else:
                        client.send(data)

            else:
                self.client.close()
                running = 0

if __name__ == "__main__":
    s = Server()
    s.run()