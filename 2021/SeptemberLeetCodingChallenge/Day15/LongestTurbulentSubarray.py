

# LeetCoding Challenge 2021. September. Day 15. Longest Turbulent Subarray

'''

Longest Turbulent Subarray

Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

    For i <= k < j:
        arr[k] > arr[k + 1] when k is odd, and
        arr[k] < arr[k + 1] when k is even.
    Or, for i <= k < j:
        arr[k] > arr[k + 1] when k is even, and
        arr[k] < arr[k + 1] when k is odd.



Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

Example 2:

Input: arr = [4,8,12,16]
Output: 2

Example 3:

Input: arr = [100]
Output: 1



Constraints:

    1 <= arr.length <= 4 * 104
    0 <= arr[i] <= 109



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
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        flag = 0
        maxTurbulentSubarraySize = 1
        curTurbulentSubarraySize = 1
        if len(arr) == 1:
            return 1
        if len(arr) == 2:
            if arr[0] > arr[1] or arr[0] < arr[1]:
                return 2
            else:
                return 1
        if len(arr) > 2:
            if len(set(arr)) == 1:
                return 1
            if arr[0] > arr[1]:
                flag = 1
            if arr[0] < arr[1]:
                flag = -1
            if arr[0] == arr[1]:
                flag = 0
            for i in range(1, n-1):
                if arr[i] < arr[i+1]:
                    if flag == 1:
                        curTurbulentSubarraySize += 1
                    if flag == -1:
                        maxTurbulentSubarraySize = max(maxTurbulentSubarraySize, curTurbulentSubarraySize)
                        curTurbulentSubarraySize = 1
                    if flag == 0:
                        maxTurbulentSubarraySize = max(maxTurbulentSubarraySize, curTurbulentSubarraySize)
                        curTurbulentSubarraySize = 1
                    flag = -1
                if arr[i] > arr[i + 1]:
                    if flag == 1:
                        maxTurbulentSubarraySize = max(maxTurbulentSubarraySize, curTurbulentSubarraySize)
                        curTurbulentSubarraySize = 1
                    if flag == -1:
                        curTurbulentSubarraySize += 1
                    if flag == 0:
                        maxTurbulentSubarraySize = max(maxTurbulentSubarraySize, curTurbulentSubarraySize)
                        curTurbulentSubarraySize = 1
                    flag = 1
                if arr[i] == arr[i + 1]:
                    maxTurbulentSubarraySize = max(maxTurbulentSubarraySize, curTurbulentSubarraySize)
                    curTurbulentSubarraySize = 1
                    flag = 0
        return max(maxTurbulentSubarraySize, curTurbulentSubarraySize)+1


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.maxTurbulenceSize([9,4,2,10,7,8,8,1,9])) # 5
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.maxTurbulenceSize([4,8,12,16])) # 2
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    print(solution.maxTurbulenceSize([100])) # 1
    end3 = time.perf_counter()
    print(f"test 3: {end3 - start3:10.6f} sec")
    #
    start4 = time.perf_counter()
    print(solution.maxTurbulenceSize([2,0,2,4,2,5,0,1,2,3])) # 6
    end4 = time.perf_counter()
    print(f"test 4: {end4 - start4:10.6f} sec")
    #
    start5 = time.perf_counter()
    print(solution.maxTurbulenceSize([0,8,45,88,48,68,28,55,17,24])) # 8
    end5 = time.perf_counter()
    print(f"test 5: {end5 - start5:10.6f} sec")
    #
    start6 = time.perf_counter()
    print(solution.maxTurbulenceSize([100,100,100])) # 1
    end6 = time.perf_counter()
    print(f"test 6: {end6 - start6:10.6f} sec")
