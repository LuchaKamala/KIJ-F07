import Counter

key = '87654321'
message = "Im Buzz Lightyear, Im coming in peace"

counter = Counter.counter()
encrypt = counter.encrypt(key, message)
print 'Encrypted with counter: ' + encrypt

decrypt = counter.decrypt(key, encrypt)
print 'Decrypted with counter: ' + decrypt