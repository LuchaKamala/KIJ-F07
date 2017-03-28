from DES import des
import Queue

des = des()

key = "irfan"
binary_key = des.stringToBinary(key)
binary_key = des.padding(binary_key)
permuted_key = des.convertToPermutedKey(binary_key)

# c = list(permuted_key[:28])
# d = list(permuted_key[28:])

c = '1111000011001100101010101111'
d = '0101010101100110011110001111'

c, d = des.shifts(c, d)
# c, d = des.rightShifts(c, d)

#print des.subkey[1] == '101111111001000110001101001111010011111100001010'

# STEP 2
# message = '0000000100100011010001010110011110001001101010111100110111101111'
message = '1000010111101000000100110101010000001111000010101011010000000101'
ip_message =  des.initiatePermutation(message)
des.left.append(ip_message[:32])
des.right.append(ip_message[32:])

for i in range(16):
    des.left.append(des.right[i])
    des.right.append(des.xorLF(des.left[i], des.calculateF(des.right[i], des.subkey[16-i])))

l16r16 = ''.join(des.right[16])+''.join(des.left[16])
output = des.inverseIP(l16r16)
print output == '0000000100100011010001010110011110001001101010111100110111101111'