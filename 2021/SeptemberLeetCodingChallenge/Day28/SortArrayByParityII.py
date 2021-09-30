

# LeetCoding Challenge 2021. September. Day 28. Sort Array By Parity II

'''

Sort Array By Parity II

Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.



Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:

Input: nums = [2,3]
Output: [2,3]



Constraints:

    2 <= nums.length <= 2 * 104
    nums.length is even.
    Half of the integers in nums are even.
    0 <= nums[i] <= 1000



Follow Up: Could you solve it in-place?



from forum

O(n) space complexity soluiton is straightforward. It is more interseting to investigate O(1) solution. The idea is to use two pointers approach, where we start with index 0 for even numbers and with index 1 for odd numbers. We traverse our numbers, where we can have the following options:

    if nums[i] % 2 == 0, then number is already on place, so we look at the next place for i.
    if nums[j] % 2 == 1, then number is already on place, so we look ate the next place for j.
    In the opposite case we need to sweich elements.

Complexity

Time complexity is O(n), space complexity is O(1).


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


# my solution
class Solution2:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0, n-1):
            if nums[i] % 2 != 0 and i % 2 == 0:
                j = i
                while j < n:
                    j += 1
                    if nums[j] % 2 == 0 and j % 2 != 0:
                        break
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            if nums[i] % 2 == 0 and i % 2 != 0:
                j = i
                while j < n:
                    j += 1
                    if nums[j] % 2 != 0 and j % 2 == 0:
                        break
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        return nums


# solution from forum
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j, n = 0, 1, len(nums)
        while j < n and i < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.sortArrayByParityII(nums = [4,2,5,7])) # [4,5,2,7]
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.sortArrayByParityII(nums = [3,1,4,2])) # [2,1,4,3]
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
