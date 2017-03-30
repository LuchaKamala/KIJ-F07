import DES

des = DES.des()
ddes = DES.des()

def xor(outputDES, message):
    result = []
    for i in range(64):
        result.append(str(int(outputDES[i]) ^ int(message[i])))
    return ''.join(result)

key = "78437298"
counter = '0000000000000000000000000000000000000000000000000000000000000001'
message = '0000000100100011010001010110011110001001101010111100110111101111'

outputDES = des.encryptDES(counter, key)
chiper = xor(outputDES, message)
plain = xor(outputDES, chiper)

# print encrypt == '1000010111101000000100110101010000001111000010101011010000000101'
print plain == message