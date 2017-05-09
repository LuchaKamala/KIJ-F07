import fractions
import random
from MillerRabin import MillerRabin

class RSA:

    # Inisiasi
    def __init__(self):
        self.miller_rabin = MillerRabin()
        self.random_from = 15
        self.random_to = 100

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.egcd(b % a, a)
            return (g, y - (b // a) * x, x)

    # Mendapatkan bilangan prima P
    def getPrimeP(self):
        prime_p = int()
        random_p = random.randint(self.random_from, self.random_to)
        while (True):
            if self.miller_rabin.isPrime(random_p, 2):
                prime_p = random_p
                break
            else:
                random_p = random.randint(self.random_from, self.random_to)
        return prime_p

    # Mendapatkan bilangan prima Q
    def getPrimeQ(self, prime_p):
        prime_q = int()
        random_q = random.randint(self.random_from, self.random_to)
        while (True):
            if self.miller_rabin.isPrime(random_q, 2) and random_q != prime_p:
                prime_q = random_q
                break
            else:
                random_q = random.randint(self.random_from, self.random_to)
        return prime_q

    # Mendapatkan nilai N
    def getValueN(self, prime_p, prime_q):
        value_n = prime_p * prime_q
        return value_n

    # Mendapatkan nilai M
    def getValueM(self, prime_p, prime_q):
        value_m = (prime_p-1) * (prime_q-1)
        return value_m

    # Mendapatkan nilai E
    def getValueE(self, value_m):
        value_e = int()
        while (True):
            temp_e = random.randint(2, value_m)
            if self.miller_rabin.isPrime(temp_e, 2) and value_m % temp_e != 0:
                value_e = temp_e
                break
        return value_e

    def getValueD(self, value_m, value_e):
        x, y, value_d = self.egcd(value_m, value_e)
        if value_d < 0:
            value_d = value_m + value_d
        return value_d

    def encryption(self, msg, value_e, value_n):
        list_of_msg = list(msg)
        chiper_text_ascii = []
        for i in list_of_msg:
            chiper = (ord(i) ** value_e) % value_n
            chiper_text_ascii.append(chiper)
        chiper_text = ";".join(str(i) for i in chiper_text_ascii)
        return chiper_text

    def decryption(self, chiper, value_d, value_n):
        chiper_text = chiper.split(';')
        chiper_text_int = []
        for i in chiper_text:
            chiper_text_int.append(int(i))

        plain_text = []
        for i in chiper_text_int:
            plain = (i ** value_d) % value_n
            plain_text.append(chr(plain))
        return "".join(plain_text)

# rsa = RSA()
# p = rsa.getPrimeP()
# q = rsa.getPrimeQ(p)
# n = rsa.getValueN(p, q)
# m = rsa.getValueM(p, q)
# e = rsa.getValueE(m)
# d = rsa.getValueD(m, e)
#
# msg = "Namamu siapa memangnya?"
# encrypt = rsa.encryption(msg, e, n)
# print "Enkripsi: " + encrypt
#
# decrypt = rsa.decryption(encrypt, d, n)
# print "Dekripsi: " + decrypt