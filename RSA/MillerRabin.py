import random

class MillerRabin :
    def millerRabinTest(self, d, n):
        a = random.randint(2, n-2)
        x = (a ** d) % n

        if x == 1 or x == n - 1:
            return True

        while d != n - 1:
            x = (x * x) % n
            d *= 2

            if x == 1:
                return False
            if x == n - 1:
                return True

        return False

    def isPrime(self, n, k):
        if n <= 1 or n == 4:
            return False
        if n <= 3:
            return True

        d = n-1
        while d%2 == 0:
            d/=2

        for i in range(k):
            if self.millerRabinTest(d, n) == False:
                return False

        return True