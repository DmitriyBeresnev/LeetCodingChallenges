

# LeetCoding Challenge 2021. October. Day 30. Longest Duplicate Substring

'''

1044. Longest Duplicate Substring
Hard

Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".



Example 1:

Input: s = "banana"
Output: "ana"

Example 2:

Input: s = "abcd"
Output: ""



Constraints:

    2 <= s.length <= 3 * 104
    s consists of lowercase English letters.

Accepted
47,356
Submissions
150,039


Related Topics
-

Similar Questions
String, Binary Search, Sliding Window, Rolling Hash, Suffix Array, Hash Function

Hide Hint 1
Binary search for the length of the answer. (If there's an answer of length 10, then there are answers of length 9, 8, 7, ...)

Hide Hint 2
To check whether an answer of length K exists, we can use Rabin-Karp 's algorithm.

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
    def RabinKarp(self, text, M, q):
        if M == 0: return True
        h, t, d = (1 << (8 * M - 8)) % q, 0, 256

        dic = defaultdict(list)

        for i in range(M):
            t = (d * t + ord(text[i])) % q

        dic[t].append(i - M + 1)

        for i in range(len(text) - M):
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            for j in dic[t]:
                if text[i + 1:i + M + 1] == text[j:j + M]:
                    return (True, text[j:j + M])
            dic[t].append(i + 1)
        return (False, "")

    def longestDupSubstring(self, S):
        beg, end = 0, len(S)
        q = (1 << 31) - 1
        Found = ""
        while beg + 1 < end:
            mid = (beg + end) // 2
            isFound, candidate = self.RabinKarp(S, mid, q)
            if isFound:
                beg, Found = mid, candidate
            else:
                end = mid

        return Found


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
