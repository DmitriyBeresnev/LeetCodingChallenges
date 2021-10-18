

# LeetCoding Challenge 2021. October. Day 14. Perfect Squares

'''

279. Perfect Squares
Medium

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.



Constraints:

    1 <= n <= 104

Accepted
460,475
Submissions
904,415

Related Topics
Math, Dynamic Programming, Bread-First Search

Similar Questions
Count Primes
Medium
Ugly Number II
Medium



For math solution:

Fermat's theorem on sums of two squares
https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D0%BE%D1%80%D0%B5%D0%BC%D0%B0_%D0%A4%D0%B5%D1%80%D0%BC%D0%B0_%E2%80%94_%D0%AD%D0%B9%D0%BB%D0%B5%D1%80%D0%B0

Legendre's three-square theorem
https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D0%BE%D1%80%D0%B5%D0%BC%D0%B0_%D0%9B%D0%B5%D0%B6%D0%B0%D0%BD%D0%B4%D1%80%D0%B0_%D0%BE_%D1%82%D1%80%D1%91%D1%85_%D0%BA%D0%B2%D0%B0%D0%B4%D1%80%D0%B0%D1%82%D0%B0%D1%85

Lagrange's four-square theorem
https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D0%BE%D1%80%D0%B5%D0%BC%D0%B0_%D0%9B%D0%B0%D0%B3%D1%80%D0%B0%D0%BD%D0%B6%D0%B0_%D0%BE_%D1%81%D1%83%D0%BC%D0%BC%D0%B5_%D1%87%D0%B5%D1%82%D1%8B%D1%80%D1%91%D1%85_%D0%BA%D0%B2%D0%B0%D0%B4%D1%80%D0%B0%D1%82%D0%BE%D0%B2


'''


import math
import time
import collections
from typing import List
import numpy as np
import random as rnd
import itertools as it
from collections import defaultdict, Counter
import re
from functools import reduce
from functools import lru_cache
from bisect import bisect, bisect_left


class Solution:
    def numSquares(self, n: int) -> int:
        if int(math.sqrt(n)) * int(math.sqrt(n)) == n:
            return 1
        #
        # Euler-Fermat's theorem on sums of two squares
        for i in range(int(math.sqrt(n))+1):
            x = n - i*i
            if int(math.sqrt(x)) * int(math.sqrt(x)) == x:
                return 2
        #
        # Legendre's three-square theorem check up
        while n % 4 == 0:
            # n /= 4
            n >>= 2
        if n % 8 == 7:
            # so Lagrange's four-square theorem
            return 4
        #
        # Legendre's three-square theorem
        return 3


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.numSquares(n=2))
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.numSquares(n=8))
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    print(solution.twoSum(nums = [3,3], target = 6))
    end3 = time.perf_counter()
    print(f"test 3: {end3 - start3:10.6f} sec")
    #
    start4 = time.perf_counter()
    print(solution.isIsomorphic("badc", "baba"))
    end4 = time.perf_counter()
    print(f"test 4: {end4 - start4:10.6f} sec")
    #
    start5 = time.perf_counter()
    print(solution.isIsomorphic("abab", "baba"))
    end5 = time.perf_counter()
    print(f"test 5: {end5 - start5:10.6f} sec")
    #
    start6 = time.perf_counter()
    print(solution.firstMissingPositive([1, 1]))
    end6 = time.perf_counter()
    print(f"test 6: {end6 - start6:10.6f} sec")
