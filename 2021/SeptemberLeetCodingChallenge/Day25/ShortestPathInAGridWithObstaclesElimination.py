

# LeetCoding Challenge 2021. September. Day 25. Shortest Path in a Grid with Obstacles Elimination

'''

Shortest Path in a Grid with Obstacles Elimination

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.



Example 1:

Input:
grid =
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example 2:

Input:
grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1
Output: -1
Explanation:
We need to eliminate at least two obstacles to find such a walk.



Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 40
    1 <= k <= m * n
    grid[i][j] == 0 or 1
    grid[0][0] == grid[m - 1][n - 1] == 0

   Hide Hint #1
Use BFS.
   Hide Hint #2
BFS on (x,y,r) x,y is coordinate, r is remain number of obstacles you can remove.



https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/1485220/Python-BFS-Clear-Explanation

Explanation:

m, n - number of rows and columns respectively

The usual/trivial BFS, with parameters (i, j), will find the quickest path from (0, 0) to (m-1, n-1) (if there's a path).
But it cannot do the same when an additional parameter k is added. So, we need to modify BFS by adding this k to it.

Let's consider this example (let's call k as number of tickets we have)

0, 1, 0
0, 0, 0

To reach the co-ordinate (1, 1), you can go like:

    (0, 0) --> (1, 0) --> (1, 1)
    (0, 0) --> (0, 1) by using 1 ticket as (0, 1) has value 1 --> (1, 1)

    We are taking 2 steps to reach (1, 1) in each way - one of the ways uses 0 ticket while the other uses 1 ticket.
    In usual BFS, (1, 1) will get appended to queue only once.
    But here, we will add parameter k - number of tickets remaining.
    So, if we consider initial k to be 1, then the state of 1st way can be defined as (1, 1, 1) and the state of 2nd way will be (1, 1, 0)
    We will also need to keep track of number of steps we have taken to reach the current co-ordinate, so we can add that as 4th parameter
    Another point to note is, we can reach a "1" co-ordinate only by using a ticket,
    and if we have 0 tickets, we cannot go there, so we should not append to queue in such cases.
    We could reach a co-ordinate in 5 steps by using 0 tickets and in another way, we could reach the same co-ordinate in 2 steps by using 3 tickets.
    But we cannot know which one is efficient, until we get to the final point (m-1, n-1). Adding k to BFS will make it possible.

Early break:

    We need a minimum of m+n-2 steps to reach final point as we will have to come down from top row to bottom row (m-1 steps) and scroll through from leftmost column to rightmost column (n-1 steps). Hence, m+n-2.
    If number of tickets is greater than or equal to minimum number of steps, we can use all tickets to travel in the most efficient way.
    So, we can do early return (before BFS) in such cases.



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
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque([(0, 0, 0, k)])
        visited = set()
        if k >= m + n - 2:
            return m + n - 2
        while q:
            nSteps, x, y, k = q.popleft()
            if (x, y) == (n - 1, m - 1):
                return nSteps
            pointsNeighborhoods = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
            for (dx, dy) in pointsNeighborhoods:
                if 0 <= dx < n and 0 <= dy < m and k - grid[dx][dy] >= 0:
                    newState = (dx, dy, k - grid[dx][dy])
                    if newState not in visited:
                        visited.add(newState)
                        #fullNewState = (nSteps + 1,) + newState
                        fullNewState = (nSteps + 1, dx, dy, k - grid[dx][dy])
                        q.append(fullNewState)
        return -1


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1))
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
