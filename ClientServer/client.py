import socket
import sys
import Counter

host = 'localhost'
port = 5000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

try:
    while True:
        key = raw_input("key: ")
        message = raw_input("Message: ")
        counter = Counter.counter()
        encrypted = counter.encrypt(key, message)
        s.send(encrypted)
        r=s.recv(1024)
        print r
except KeyboardInterrupt:
    s.close()
    sys.exit(0)