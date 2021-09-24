

# LeetCoding Challenge 2021. September. Day 24. N-th Tribonacci Number

'''

N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:

Input: n = 25
Output: 1389537



Constraints:

    0 <= n <= 37
    The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

   Hide Hint #1
Make an array F of length 38, and set F[0] = 0, F[1] = F[2] = 1.
   Hide Hint #2
Now write a loop where you set F[n+3] = F[n] + F[n+1] + F[n+2], and return F[n].

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
    def tribonacci(self, n: int) -> int:
        fArr = [0] * (n+1)
        fArr[0] = 0
        if n == 0:
            return fArr[n]
        if n == 1:
            fArr[1] = 1
            return fArr[n]
        if n == 2:
            fArr[1] = 1
            fArr[2] = 1
            return fArr[n]
        fArr[1] = 1
        fArr[2] = 1
        for i in range(3, n+1):
            fArr[i] = fArr[i-1] + fArr[i-2] + fArr[i-3]
        return fArr[n]


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.tribonacci(n=4)) # 4
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.tribonacci(n=0)) # 0
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
