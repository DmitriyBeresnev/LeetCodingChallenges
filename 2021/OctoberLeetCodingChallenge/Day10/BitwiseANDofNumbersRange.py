

# LeetCoding Challenge 2021. October. Day 10. Bitwise AND of Numbers Range

'''

201. Bitwise AND of Numbers Range
Medium

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.



Example 1:

Input: left = 5, right = 7
Output: 4

Example 2:

Input: left = 0, right = 0
Output: 0

Example 3:

Input: left = 1, right = 2147483647
Output: 0



Constraints:

    0 <= left <= right <= 231 - 1

Accepted
187,188
Submissions
462,148

Related Topics
Bit Manipulation

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


# naive approach
class Solution2:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        for i, val in enumerate(range(left, right+1)):
            res &= val
            # print(val, i)
        return res


# optimized
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        nShifts = 0
        while left < right:
            left >>= 1
            right >>= 1
            nShifts += 1
        return right << nShifts


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.rangeBitwiseAnd(left=5, right=7))
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.rangeBitwiseAnd(left = 1, right = 2147483647))
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
