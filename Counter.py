import DES

class counter():
    def __init__(self):
        self.des = DES.des()
        self.ddes = DES.des()

    def xor(self, outputDES, message):
        result = []
        for i in range(64):
            result.append(str(int(outputDES[i]) ^ int(message[i])))
        return ''.join(result)

    def stringToBinary(self, data):
        result = []
        for char in data:
            decimal = ord(char)
            binary = "{0:08b}".format(decimal)
            result.append(binary)
        return ''.join(result)

    def counterFormat(self, data):
        data = str(data)
        result = []
        for char in data:
            decimal = ord(char)
            binary = "{0:064b}".format(decimal)
            result.append(binary)
        return ''.join(result)

    def binaryToString(self, data):
        r = []
        result = []
        for i in range(0, len(data), 8):
            num = data[i:i + 8]
            r.append(num)
        for num in r:
            text = chr(int(num, 2))
            result.append(text)
        return ''.join(result)

    def encrypt(self, key, message):
        temp = ''
        per8 = []
        for i in range(len(message)):
            temp += message[i]
            if (i+1) % 8 == 0:
                per8.append(temp)
                temp = ''
        per8.append(temp)

        lastPer8 = len(per8)-1
        if len(per8[lastPer8]) < 8:
            for i in range(8-len(per8[lastPer8])):
                per8[lastPer8] += '\0'

        inputDES = []
        for msg in per8:
            inputDES.append(self.stringToBinary(msg))

        chiper = []
        for i in range(len(inputDES)):
            counter = self.counterFormat(i+1)
            outputDES = self.des.encryptDES(counter, key)
            outputDES = self.stringToBinary(outputDES)
            chiper.append(self.xor(outputDES, inputDES[i]))

        chiper = ''.join(chiper)
        return self.binaryToString(chiper)

    def decrypt(self, key, chiper):
        per64 = []
        temp = ''
        binary_chiper = self.stringToBinary(chiper)
        for i in range(len(binary_chiper)):
            temp += binary_chiper[i]
            if (i+1) % 64 == 0:
                per64.append(temp)
                temp = ''

        plain = []
        for i in range(len(per64)):
            counter = self.counterFormat(i+1)
            outputDes = self.ddes.encryptDES(counter, key)
            outputDes = self.stringToBinary(outputDes)
            plain.append(self.xor(outputDes, per64[i]))

        plainString = []
        for pl in plain:
            plainString.append(self.binaryToString(pl))

        return ''.join(plainString)

# key = "78437298"
# counter = counterFormat(1)
# message = '12345678'
# msg = stringToBinary(message)
#
# outputDES = des.encryptDES(counter, key)
# outputDES = stringToBinary(outputDES)
# chiper = xor(outputDES, msg)
# plain = xor(outputDES, chiper)

# print encrypt == '1000010111101000000100110101010000001111000010101011010000000101'
# print plain == msg