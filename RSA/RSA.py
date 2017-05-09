import fractions
import random
from MillerRabin import MillerRabin

miller_rabin = MillerRabin()

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

# Mendapatkan nilai p
random_p = random.randint(15, 100)
while(True):
    if miller_rabin.isPrime(random_p, 2):
        prime_p = random_p
        break
    else:
        random_p = random.randint(15, 100)

# Mendapatkan nilai q
random_q = random.randint(15, 100)
while(True):
    if miller_rabin.isPrime(random_q, 2) and random_q != prime_p:
        prime_q = random_q
        break
    else:
        random_q = random.randint(15, 100)

# Mendapatkan nilai n dan phi
value_n = prime_p * prime_q
phi = (prime_p-1) * (prime_q-1)

# Mendapatkan nilai e
while(True):
    temp_e = random.randint(2, phi)
    if miller_rabin.isPrime(temp_e, 2) and phi%temp_e != 0:
        value_e = temp_e
        break

# Mendapatkan nilai d
x, y, value_d = egcd(phi, value_e)
if value_d < 0:
    value_d = phi+value_d

msg = "Kongres BEM FTIf malam ini loh"

# Encrypting ...
list_of_msg = list(msg)
chiper_text_ascii = []
for i in list_of_msg:
    chiper = (ord(i)**value_e)%value_n
    chiper_text_ascii.append(chiper)
print chiper_text_ascii
chiper_text = ";".join(str(i) for i in chiper_text_ascii)
print chiper_text

# Decrypting ...
chiper_text = chiper_text.split(';')
chiper_text_int = []
for i in chiper_text:
    chiper_text_int.append(int(i))

plain_text = []
for i in chiper_text_int:
    plain = (i**value_d)%value_n
    plain_text.append(chr(plain))
print "".join(plain_text)