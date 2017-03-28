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
print c == '1111000011001100101010101111'
print d == '0101010101100110011110001111'

print des.subkey[7] == '111011001000010010110111111101100001100010111100'