

# LeetCoding Challenge 2021. September. Day 18. Expression Add Operators

'''

Expression Add Operators

Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.



Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]

Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]

Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]

Example 5:

Input: num = "3456237490", target = 9191
Output: []



Constraints:

    1 <= num.length <= 10
    num consists of only digits.
    -231 <= target <= 231 - 1

   Hide Hint #1
Note that a number can contain multiple digits.
   Hide Hint #2
Since the question asks us to find all of the valid expressions, we need a way to iterate over all of them. (Hint: Recursion!)
   Hide Hint #3
We can keep track of the expression string and evaluate it at the very end. But that would take a lot of time. Can we keep track of the expression's value as well so as to avoid the evaluation at the very end of recursion?
   Hide Hint #4
Think carefully about the multiply operator. It has a higher precedence than the addition and subtraction operators.
1 + 2 = 3
1 + 2 - 4 --> 3 - 4 --> -1
1 + 2 - 4 * 12 --> -1 * 12 --> -12 (WRONG!)
1 + 2 - 4 * 12 --> -1 - (-4) + (-4 * 12) --> 3 + (-48) --> -45 (CORRECT!)
   Hide Hint #5
We simply need to keep track of the last operand in our expression and reverse it's effect on the expression's value while considering the multiply operator.




[Python] dfs with stack of monomials, explained

Quite diffucult problem, which is similar to Basic Calculators problem (0224, 0227). Let us consider dfs with the following parameters:

    idx is the index of current element we traverse in num.
    path is the string built so far.
    value is current value of created path.
    last is the value of the last monomial.

Here we use idea of stack of monomials: imagine, that we have expression 1*2 + 3*4*5, then we have the following steps: [1], [2], [2, 3], [2,12], [2,60]: each time we have + or - we add one element to the end of stack; each time we have * we update the last element in stack.

Then when we traverse our string, we can have several options: each time we need to create tmp = int(num[idx: i]) and make sure that this is valid number: tmp will be the next number we are going to use. Then if last == None, we have only one option. If last != None, we can have 3 options which symbol we can take: if it is + or -, we just update value and sign of tmp. If it is multiplication, we need to update both value and last should be multiplied by tmp.

Complexity

It is potentially O(4^n * n), because on each step we have 4 options: +, -, * or no sign. Space complexity potentially the same.

solution from the link: https://leetcode.com/problems/expression-add-operators/discuss/1470156/Python-dfs-with-stack-of-monomials-explained


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
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(idx, path, value, last):
            if idx == n and value == target:
                ans.append(path)

            for i in range(idx + 1, n + 1):
                tmp = int(num[idx: i])
                if i == idx + 1 or (i > idx + 1 and num[idx] != "0"):
                    if last is None:
                        dfs(i, num[idx: i], tmp, tmp)
                    else:
                        dfs(i, path + '+' + num[idx: i], value + tmp, tmp)
                        dfs(i, path + '-' + num[idx: i], value - tmp, -tmp)
                        dfs(i, path + '*' + num[idx: i], value - last + last * tmp, last * tmp)

        ans, n = [], len(num)
        dfs(0, "", 0, None)
        return ans


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
