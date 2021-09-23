

# LeetCoding Challenge 2021. September. Day 23. Break a Palindrome

'''

Break a Palindrome

Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.



Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

Example 3:

Input: palindrome = "aa"
Output: "ab"

Example 4:

Input: palindrome = "aba"
Output: "abb"



Constraints:

    1 <= palindrome.length <= 1000
    palindrome consists of only lowercase English letters.

   Hide Hint #1
How to detect if there is impossible to perform the replacement? Only when the length = 1.
   Hide Hint #2
Change the first non 'a' character to 'a'.
   Hide Hint #3
What if the string has only 'a'?
   Hide Hint #4
Change the last character to 'b'.


We need to replace one symbol and to get the smallest string as possible. First, we try to change elements on the smaller positions: imagine we have string xyzyx - where x, y, z can be any symbols. If x is not equal to "a", then if we replace this symbol with "a" we will break palindrome and it will be as small as possible. However if x = "a", it is not optimal to replace it to say "b", we can only make our string bigger. So, we move to the next element y and so on. Notice that we can not change z in this case, because we will not break palindrome property.

What happens, if we reached the last element and were not able to apply strategy above? Then we have string like this aaaaaa..aaaaaa or aaaaaa...z...aaaaaa, where z can be any symbol. In this case to get the smalles string as possible we need to replace last symbol to "b". Also there is case when n = 1, and we can not break palindrome property so we return "".

Complexity

It is O(n) for time and for space.

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
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if len(palindrome) == 1:
            return ""
        pos = 0
        for i in range(n // 2):
            if palindrome[i] != 'a':
                break
            pos = i+1
        return palindrome[:pos] + 'a' + palindrome[pos + 1:] if pos != len(palindrome) // 2 else palindrome[:len(palindrome) - 1] + 'b'


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.breakPalindrome("aa"))
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
