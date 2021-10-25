

# LeetCoding Challenge 2021. October. Day 22. Sort Characters By Frequency

'''

451. Sort Characters By Frequency
Medium

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.



Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.



Constraints:

    1 <= s.length <= 5 * 105
    s consists of uppercase and lowercase English letters and digits.

Accepted
313,625
Submissions
469,987


Related Topics
Hash Table, String, Sorting, Heap (Priority Queue), Bucket Sort, Counting

Similar Questions
Top K Frequent Elements
Medium
First Unique Character in a String
Easy
Sort Array by Increasing Frequency
Easy

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
    def frequencySort(self, s: str) -> str:
        strLen = len(s)
        if strLen > 1:
            repeatingCharactersCountsMap = dict()
            for i in range(0, strLen):
                if s[i] not in repeatingCharactersCountsMap:
                    repeatingCharactersCountsMap.update({s[i]: 1})
                else:
                    repeatingCharactersCountsMap[s[i]] += 1
            # sort hash map by values
            sortedMap = {k: v for k, v in sorted(repeatingCharactersCountsMap.items(), key=lambda item: item[1], reverse=True)}
            resStrSymbolsList = list(sortedMap.keys())
            res = ""
            for symbol, counts in sortedMap.items():
                for sym in [symbol for count in range(0, counts)]:
                    res += str(sym)
            return res
        else:
            return s


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
