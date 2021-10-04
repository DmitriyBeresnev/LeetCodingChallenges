

# LeetCoding Challenge 2021. October. Day 4. Island Perimeter

'''

463. Island Perimeter
Easy

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:

Input: grid = [[1]]
Output: 4

Example 3:

Input: grid = [[1,0]]
Output: 4



Constraints:

    row == grid.length
    col == grid[i].length
    1 <= row, col <= 100
    grid[i][j] is 0 or 1.
    There is exactly one island in grid.

Accepted
304,271
Submissions
449,490
Seen this question in a real interview before?
Max Area of Island
Medium
Flood Fill
Easy
Coloring A Border
Medium

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
    def islandPerimeter(self, grid):
        n = len(grid)
        m = len(grid[0])
        p = 0
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == 1:
                    # up
                    if i - 1 >= 0 and grid[i-1][j] == 0:
                        p += 1
                    # down
                    if i + 1 <= n-1 and grid[i+1][j] == 0:
                        p += 1
                    # left
                    if j - 1 >= 0 and grid[i][j-1] == 0:
                        p += 1
                    # right
                    if j + 1 <= m-1 and grid[i][j+1] == 0:
                        p += 1
                    # top border
                    if i == 0:
                        p += 1
                    # bottom border
                    if i == n-1:
                        p += 1
                    # left border
                    if j == 0:
                        p += 1
                    # right border
                    if j == m-1:
                        p += 1
        return p


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
