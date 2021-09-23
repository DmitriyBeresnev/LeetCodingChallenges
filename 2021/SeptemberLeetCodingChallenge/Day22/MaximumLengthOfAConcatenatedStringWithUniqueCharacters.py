

# LeetCoding Challenge 2021. September. Day 22. Maximum Length of a Concatenated String with Unique Characters

'''

Maximum Length of a Concatenated String with Unique Characters

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26



Constraints:

    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] contains only lower case English letters.

   Hide Hint #1
You can try all combinations and keep mask of characters you have.
   Hide Hint #2
You can use DP.



Idea

    The idea is that we try all possible subset of arr by using Bitmasking, same with 78. Subsets.
    Let mask represent the appearance of arr[i], ith bit of mask = 1 means there exists arr[i].
    There are total 2^n bitmasking states: 0..000, 0..001, 0..010, ..., 1..111.
    For each subsets of arr, we check if it can form a valid string? If we can form then we update the maximum length so far.

Complexity:

    Time: O(2^n * (26 + n)), where n <= 16 is length of arr array.
        There is 2^n bitmask states.
        There are up to 26 distinct characters we can form.
    Space: O(26)


This problem is medium, not hard, because given constraints it is possible to do just bruteforce solution: check for every one of 2^16 subsets if concatenation have all different symbols. However we can do better.

First of all, number of letters in alphabet is not big: only 26, so we can use the idea of bitmask: encode every word with number. For example for word dab, we can use mask 1011 (we start from end).

    First of all, we take only words with different letters, and remove all others.
    Next step is for every word evaluate its mask and also number of letters. We keep tuple. For example d[1<<i] = (1011, 3) for word dab, where i is index of this word. Why we use 1<<i, not just i? You will see it later.
    dp(m) is maximum answer we can have if we use bitmask of words indexes m. Notice, it is another bitmask, not what we discussed previously. For example, if we have arr = [ab, cd, ef, gh], then m = 1011 means that we take ab, cd, gh as our solution. dp(m) will return two values: bitmask of used letters and number of used letters.
    How we can find dp(m)? If m == 0, we return (0, 0). Next we find the last 1 in our m, usint m & (m-1) trick. Then we check if m_last & d[m - prev][0] != 0. If it is the case, it means that we have some letters repeated, so we return (0, -10000) in this case where -10000 represents minus infinity. In the opposite case we return (m_last | d[m - prev][0], bits_last + d[m - prev][1]), because we need to turn on bits d[m - prev][0] in mask m_last and number of bits is bits_last + d[m - prev][1]. Notice that we can keep in fact only one value and evaluate the second on flight, but it will not be true O(1).
    In the end we just check all masks dp(x) and return one with the biggest number of letters on.

Complexity

It is O(2^n) for time and O(2^n) for space.

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
    def maxLength(self, arr: List[str]) -> int:
        arr = [word for word in arr if len(set(word)) == len(word)]

        d = {}
        for i, word in enumerate(arr):
            d[1 << i] = (sum(1 << (ord(w) - 97) for w in word), len(word))

        @lru_cache(None)
        def dp(m):
            if m == 0: return (0, 0)
            prev = m & (m - 1)
            m_last, bits_last = dp(prev)
            if m_last & d[m - prev][0] != 0: return (0, -10000)
            return (m_last | d[m - prev][0], bits_last + d[m - prev][1])

        return max(dp(x)[1] for x in range(1 << len(arr)))


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
