

# LeetCoding Challenge 2021. October. Day 12

'''

374. Guess Number Higher or Lower
Easy

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

    -1: The number I picked is lower than your guess (i.e. pick < num).
    1: The number I picked is higher than your guess (i.e. pick > num).
    0: The number I picked is equal to your guess (i.e. pick == num).

Return the number that I picked.



Example 1:

Input: n = 10, pick = 6
Output: 6

Example 2:

Input: n = 1, pick = 1
Output: 1

Example 3:

Input: n = 2, pick = 1
Output: 1

Example 4:

Input: n = 2, pick = 2
Output: 2



Constraints:

    1 <= n <= 231 - 1
    1 <= pick <= n

Accepted
236,220
Submissions
503,272

Related Topics
Binary Search, Iterative

Similar Questions
First Bad Version
Easy
Guess Number Higher or Lower II
Medium
Find K Closest Elements
Medium

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
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while True:
            mid = low + (high - low) // 2
            if guess(mid) < 0:
                high = mid - 1
            elif guess(mid) > 0:
                low = mid + 1
            else:
                return mid
        return 0


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.twoSum(nums = [2,7,11,15], target = 9))
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.twoSum(nums = [3,2,4], target = 6))
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
