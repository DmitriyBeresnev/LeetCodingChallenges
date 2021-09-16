

# LeetCoding Challenge 2021. September. Day 16. Spiral Matrix

'''

Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]



Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100

   Hide Hint #1
Well for some problems, the best way really is to come up with some algorithms for simulation. Basically, you need to simulate what the problem asks us to do.
   Hide Hint #2
We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column and then we move inwards by 1 and then repeat. That's all, that is all the simulation that we need.
   Hide Hint #3
Think about when you want to switch the progress on one of the indexes. If you progress on

i

out of

[i, j]

, you'd be shifting in the same column. Similarly, by changing values for

j

, you'd be shifting in the same row. Also, keep track of the end of a boundary so that you can move inwards and then keep repeating. It's always best to run the simulation on edge cases like a single column or a single row to see if anything breaks or not.

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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        totalNumsCount = n * m
        startRowIndex = 0
        startColIndex = 0
        num = 0
        res = list()
        while num != totalNumsCount:
            for j in range(startColIndex, m):
                res.append(matrix[startRowIndex][j])
                num += 1
            if num == totalNumsCount:
                return res
            startRowIndex += 1
            for i in range(startRowIndex, n):
                res.append(matrix[i][m-1])
                num += 1
            if num == totalNumsCount:
                return res
            m -= 1
            for j in range(m-1, startColIndex-1, -1):
                res.append(matrix[n-1][j])
                num += 1
            if num == totalNumsCount:
                return res
            startColIndex += 1
            n -= 1
            if num == totalNumsCount:
                return res
            for i in range(n-1, startRowIndex-1, -1):
                res.append(matrix[i][startColIndex-1])
                num += 1
        return res


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
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
