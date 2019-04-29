# Introduction to dynamic programming using fibonacci numbers
import unittest


def fib_rec(n):
    """Recursive fibonacci, highly useless."""
    assert(n >= 0)
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

# The problem with above method is that we are claculating 
# Entire subtree every time we need a number.

# CITBRACUD
# 1. Clarify Problem
# 2. Clarify Input
# 3. Brainstorm
# 4. Runtime Analysis
# 5. Code
# 6. Unittest
# 7. Debug

# there is nothing here to do CITBRACUD. Only brainstorming.assertEqual
# Brainstorming
# Since we approach DP with n=0 to n=n, lets assume there is an 
# array with n=0 and n=1 filled in. Then we can keep populating the array


def fib_array(n):
    l = [0] * (n + 1)
    if n > 1:
        l[1] = 1
    else:
        return n
    for i in range(2, n + 1):
        l[i] = l[i - 1] + l[i - 2]
    return l[-1]


# To optimize it more, we can see that at every loop,
# we are using only previous two entries. Hence we do
# not need to keep all entries from 0 to n, we only need
# previous two

def fib(n):
    a = 0
    b = 1
    if n < 1:
        return n
    for i in range(1, n):
        a, b = b, a + b
    return b


class fibTest(unittest.TestCase):
    def setup():
        pass

    def test_fib_rec(self):
        self.assertEqual(fib_rec(0), 0)
        self.assertEqual(fib_rec(1), 1)
        self.assertEqual(fib_rec(2), 1)
        self.assertEqual(fib_rec(3), 2)
        self.assertEqual(fib_rec(4), 3)
        self.assertEqual(fib_rec(5), 5)
        self.assertEqual(fib_rec(6), 8)
        self.assertEqual(fib_rec(10), 55)

    def test_fib_array(self):
        self.assertEqual(fib_array(0), 0)
        self.assertEqual(fib_array(1), 1)
        self.assertEqual(fib_array(2), 1)
        self.assertEqual(fib_array(3), 2)
        self.assertEqual(fib_array(4), 3)
        self.assertEqual(fib_array(5), 5)
        self.assertEqual(fib_array(6), 8)
        self.assertEqual(fib_array(10), 55)
        self.assertEqual(fib_array(100), 354224848179261915075)

    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(100), 354224848179261915075)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
