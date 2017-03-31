import Counter

key = '132465768'
message = "Im Buzz Lightyear, Im coming in peace"

key = str(input())
message = str(input())

counter = Counter.counter()
encrypt = counter.encrypt(key, message)
print 'Encrypted with counter: ' + encrypt

decrypt = counter.decrypt(key, encrypt)
print 'Decrypted with counter: ' + decrypt