
class des():

    def __init__(self):
        self.pc1 = [
            57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4
        ]

        self.pc2 = [
            
        ]

        self.left_shift = [
            1, 1, 2, 2, 2, 2, 2, 2,
            1, 2, 2, 2, 2, 2, 2, 1
        ]

        self.subkey = []

        self.ip = [
            14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26
        ]

    def stringToBinary(self, data):
        data_lenght = len(data)
        result = []
        for char in data:
            decimal = ord(char)
            binary = "{0:08b}".format(decimal)
            result.append(binary)
        return ''.join(result)

    def convertToPermutedKey(self, key):
        permuted_key = []
        for bit_index in self.pc1:
            permuted_key.append(key[bit_index])
        return ''.join(permuted_key)

    def padding(self, data):
        diff = 64-len(data)
        while diff:
            data += '0'
            diff -= 1
        return data

    def shifts(self, c, d):
        c = list(c)
        d = list(d)
        self.subkey.append(''.join(c) + ''.join(d))
        for move in self.left_shift:
            for i in range(move):
                c.append(c.pop(0))
                d.append(d.pop(0))
            self.subkey.append(''.join(c)+''.join(d))
        return ''.join(c), ''.join(d)