# The longest increasing subsequence.
# The longest increasing subsequence problem is where we find
# longest increasing subsequence in an array. Here subsequence is different
# from substring

# The CITBRACUD method

# 1. Clarify Input
#   Subsequence vs Substring
# [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
# The LIS is
# [-3, 1, 4, 5, 8, 9]
# The longest increasing substring is
# [4, 5, 8, 9]

# 2. Clarify Input
# Null list
# Maximum size of list
# Increasing vs non decreasing
# Negative numbers

# Test cases:
# [] - 0
# [1] - 1
# [5, 6, 3, 7, 4] - 3
# [5, 6, -1, 1, 4, 7] - 4
# [7,11,-5,-2,15,1,16,6,7,11,8,9,0] - 7 [-5, -2, 1, 6, 7, 8, 9]

# Brainstorming
# Define a sub problem
# LIS upto index k is longest increasing subsequence upto index k
# Now when elt k + 1 comes in, either it is bigger than the biggest elt
# in our LIS or not. If it is bigger, then we increase the LIS by one
# and go to next element. If it is not bigger, we simply move to next
# element
# Array: [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
# LIS:   [1, 2, 2, 2,  3, 3, 4,  4, 4, 4, 4, 4], which will not work.
# LIS    [1, 2, 1, 1, 3, 2,  4,  3, 4, 5, 6, 3]
# In order to do this, we need to find the largest increasing subsequence
# For i < k, where a[i] < a[k] and then add 1 to it.
# Algorithm
# 1. Start with LIS initialized to 1 for all elements. That is the minimum for any number
# for i from 1 to n
#   For j from 0 to i
#       lis[i] = max(lis[i], 1 + lis[j] if arr[j] < arr[i])
# return max(lis)

# Runtime Analysis
# There are two loops
# One from 1 to n
# other from 1 to i, where average i is n/2, which means
# run time is n*n/2

# Coding

import unittest


def longest_increasing_subsequence(a):
    n = len(a)
    if not a:
        return 0
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if a[j] < a[i]:
                lis[i] = max(lis[i], 1 + lis[j])
    return max(lis)


# Unittest
class TestLIS(unittest.TestCase):
    """tests for LIS"""
    # Test cases:
    # [] - 0
    # [1] - 1
    # [5, 6, 3, 7, 4] - 3
    # [5, 6, -1, 1, 4, 7] - 4
    # [7,11,-5,-2,15,1,16,6,7,11,8,9,0] - 7 [-5, -2, 1, 6, 7, 8, 9]
    def setUp(self):
        self.cases = [
            ([], 0),
            ([1], 1),
            ([5, 6, 3, 7, 4], 3),
            ([5, 6, -1, 1, 4, 7], 4),
            ([7, 11, -5, -2, 15, 1, 16, 6, 7, 11, 8, 9, 0], 7)
        ]

    def test_lis(self):
        for case in self.cases:
            self.assertEqual(longest_increasing_subsequence(case[0]), case[1])


if __name__ == '__main__':
    unittest.main()
