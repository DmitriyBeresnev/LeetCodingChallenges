

# LeetCoding Challenge 2021. October. Day 5. Climbing Stairs

'''

70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step



Constraints:

    1 <= n <= 45

Accepted
1,161,506
Submissions
2,333,491

Seen this question in a real interview before?

Related topics
Math, Dynamic programming, Memorization

Similar questions
Min Cost Climbing Stairs
Easy
Fibonacci Number
Easy
N-th Tribonacci Number
Easy

Hide Hint 1
To reach nth step, what could have been your previous steps? (Think about the step sizes)

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
    def climbStairs(self, n: int) -> int:
        '''
        return round((0.5 + math.sqrt(5) / 2) ** (n + 1) / math.sqrt(5))
        '''
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        if n == 1:
            return dp[1]
        dp[2] = 2
        if n == 2:
            return dp[2]
        if n > 2:
            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.climbStairs(n=3))
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
