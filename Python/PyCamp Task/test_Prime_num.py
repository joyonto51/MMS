import unittest

def prime(num):
    p = True
    if num > 2:
        n = num//2 + 1

        for i in range(2, n+1):
            if num % i == 0:
                p = False
                break

    return p

class Testprime(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(prime(4), False)
        self.assertEqual(prime(19), True)

if __name__ == '__main__':
    unittest.main()
