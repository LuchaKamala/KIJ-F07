class KeyExchange:
    def __init__(self):
        self.prime = 23
        self.generator = 11

    def generatePublicNumber(self, secret_number):
        public_number = (self.generator**secret_number) % self.prime
        return public_number

    def generateKey(self, public_number, secret_number):
        key = (public_number**secret_number) % self.prime
        return key