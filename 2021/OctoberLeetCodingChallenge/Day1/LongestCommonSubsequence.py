

# LeetCoding Challenge 2021. October. Day 1. Longest Common Subsequence

'''

1143. Longest Common Subsequence
Medium

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.



Constraints:

    1 <= text1.length, text2.length <= 1000
    text1 and text2 consist of only lowercase English characters.

Accepted
269,364
Submissions
457,346
Seen this question in a real interview before?
Longest Palindromic Subsequence
Medium
Delete Operation for Two Strings
Medium
Shortest Common Supersequence
Hard
Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise


from forum
https://leetcode.com/problems/longest-common-subsequence/discuss/1496922/Python-dp-solution-explained

It is quite classical dynamic programming problem. Let dp[i][j] be the answer for substrings text1[:i] and text2[:i]. Notice that we also add ! symbol in the beginning of both strings to avoid edge cases. Then we an have two options:

    if text1[i] == text2[j], then dp[i][j] = dp[i-1][j-1] + 1.
    in the opposite case, we need to choose maximum between dp[i-1][j] and dp[i][j-1].

Complexity

Time complexity is O(mn), space complexity O(mn) as well.

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


class Solution2:
    # Function to find the length of the longest common subsequence of
    # sequences `X[0…m-1]` and `Y[0…n-1]`
    def lcsLength(self, text1: str, text2: str, m: int, n: int) -> int:
        # return if the end of either sequence is reached
        if m == 0 or n == 0:
            return 0
        # if the last character of `X` and `Y` matches
        if text1[m - 1] == text2[n - 1]:
            return self.lcsLength(text1, text2, m, n) + 1
        # otherwise, if the last character of `X` and `Y` don't match
        return max(self.lcsLength(text1, text2, m, n-1), self.lcsLength(text1, text2, m-1, n))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.lcsLength(text1, text2, len(text1), len(text2))


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        text1 = "!" + text1
        text2 = "!" + text2
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i, j in it.product(range(m), range(n)):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1] - 1



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
