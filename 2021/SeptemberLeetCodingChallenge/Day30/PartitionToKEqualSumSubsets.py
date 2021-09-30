

# LeetCoding Challenge 2021. September. Day 30. Partition to K Equal Sum Subsets

'''

Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false



Constraints:

    1 <= k <= nums.length <= 16
    1 <= nums[i] <= 104
    The frequency of each element is in the range [1, 4].

   Hide Hint #1
We can figure out what target each subset must sum to. Then, let's recursively search, where at each call to our function, we choose which of k subsets the next value will join.


from forum

https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/1495012/C%2B%2B-Simple-and-Elegant-Backtracking-Solution-Detailed-Explanation

Idea:
First, we sum up the nums to see if it's possible.
If sum doesn't divide by k - return false.
Then, we use typical backtracking to find all possible subsets with each sum = sum / k.
Vector visited will help us check if we used each number exactly once.
In Backtrack function:
k is counting the number of subsets with sum = target. Therefor, if k == 0 we have k subsets and we return true.
If curr_sum == target - we finished filling the current subset - call backtrack again with k = k-1 and curr_sum = 0 for the next subset.
Then, we loop through all numbers.
If we got to a number that we used already - visited[j], or curr_sum + nums[j] > target - continue.
Now, we want to use the current number, so we set visited[j] = true, call backtrack with that number.
If we got a true from backtrack, we're done - return true.
Otherwise - change back visited[j] to false and try the next number.

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
    def backtrack(self, nums: List[int], nArr: int, visited: List[bool], targetSubArrSum: int, curSubArrSum: int, curPos: int, k: int) -> bool:
        if k == 0:
            return True
        if curSubArrSum == targetSubArrSum:
            return self.backtrack(nums, nArr, visited, targetSubArrSum, 0, 0, k-1)
        for j in range(curPos, nArr):
            if visited[j] or curSubArrSum + nums[j] > targetSubArrSum:
                continue
            visited[j] = True
            if self.backtrack(nums, nArr, visited, targetSubArrSum, curSubArrSum + nums[j], j+1, k):
                return True
            visited[j] = False
        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalArrSum = sum(nums)
        nArr = len(nums)
        if nArr < k or totalArrSum % k > 0:
            return False
        visited = [False] * nArr
        return self.backtrack(nums, nArr, visited, totalArrSum // k, 0, 0, k)


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
