

# LeetCoding Challenge 2021. October. Day 27. Sort Colors

'''

75. Sort Colors
Medium

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:

Input: nums = [0]
Output: [0]

Example 4:

Input: nums = [1]
Output: [1]



Constraints:

    n == nums.length
    1 <= n <= 300
    nums[i] is 0, 1, or 2.



Follow up: Could you come up with a one-pass algorithm using only constant extra space?
Accepted
812,251
Submissions
1,549,146


Related Topics
Array, Two Pointers, Sorting

Similar Questions
Sort List
Medium
Wiggle Sort
Medium
Wiggle Sort II
Medium

Hide Hint 1
A rather straight forward solution is a two-pass algorithm using counting sort.
Hide Hint 2
Iterate the array counting number of 0's, 1's, and 2's.
Hide Hint 3
Overwrite array with the total number of 0's, then 1's and followed by 2's.

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
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colorsCountsMap = {
            0: 0,
            1: 0,
            2: 0
        }
        for num in nums:
            colorsCountsMap[num] += 1
        resArr = list()
        for color, counts in colorsCountsMap.items():
            for i in range(0, counts):
                resArr.append(color)
        nums.clear()
        nums.extend(resArr)


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.twoSum(nums = [2 ,7 ,11 ,15], target = 9))
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.twoSum(nums = [3 ,2 ,4], target = 6))
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    print(solution.twoSum(nums = [3 ,3], target = 6))
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
