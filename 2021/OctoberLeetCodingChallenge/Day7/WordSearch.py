

# LeetCoding Challenge 2021. October. Day 7. Word Search

'''

79. Word Search
Medium

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false



Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.



Follow up: Could you use search pruning to make your solution faster with a larger board?
Accepted
772,412
Submissions
2,001,804
Seen this question in a real interview before?
Word Search II
Hard




def exist(self, board, word):
        def dfs(ind, i, j):
            if self.found: return  # early stop if word is found

            if ind == k:
                self.found = True  # for early stopping
                return

            if i < 0 or i >= m or j < 0 or j >= n: return
            tmp = board[i][j]
            if tmp != word[ind]: return

            board[i][j] = "#"
            for x, y in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                dfs(ind + 1, i + x, j + y)
            board[i][j] = tmp

        self.found = False
        m, n, k = len(board), len(board[0]), len(word)

        for i, j in it.product(range(m), range(n)):
            if self.found: return True  # early stop if word is found
            dfs(0, i, j)
        return self.found

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
    def __init__(self):
        self.foundSymbols = ""
        self.coords = list()
        self.isFound = False

    def dfs(self, board: List[List[str]], n: int, m: int, x: int, y: int, word: str) -> None:
        dxdy = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        if board[x][y] in word and (x,y) not in self.coords:
            allSymbolPositionsInWordList = [pos+1 for pos, char in enumerate(word) if char == board[x][y]]
            if len(self.foundSymbols) + 1 not in allSymbolPositionsInWordList:
                return
            self.coords.append((x ,y))
            self.foundSymbols += board[x][y]
            if self.foundSymbols == word:
                self.isFound = True
                return
            for d in dxdy:
                dx = x + d[0]
                dy = y + d[1]
                print(dx, " ", dy)
                if 0 <= dx < n and 0 <= dy < m:
                    self.dfs(board, n, m, dx, dy, word)
        else:
            return

    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        for i in range(0, n):
            for j in range(0, m):
                if board[i][j] == word[0]:
                    self.dfs(board, n, m, i, j, word)
                    self.foundSymbols = ""
                    self.coords.clear()
        return self.isFound


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        c = 0

        def find(i, j, c):
            if c == len(word): return True
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[c]: return False
            board[i][j] = 0
            if find(i, j + 1, c + 1) or find(i + 1, j, c + 1) or find(i, j - 1, c + 1) or find(i - 1, j,
                                                                                               c + 1): return True
            board[i][j] = word[c]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and find(i, j, c): return True
        return False


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")) # true
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    solution = Solution()
    print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")) # true
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    solution = Solution()
    print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")) # false
    end3 = time.perf_counter()
    print(f"test 3: {end3 - start3:10.6f} sec")
    #
    start4 = time.perf_counter()
    solution = Solution()
    print(solution.exist([["a","b"],["c","d"]], "cdba")) # true
    end4 = time.perf_counter()
    print(f"test 4: {end4 - start4:10.6f} sec")
    #
    start5 = time.perf_counter()
    solution = Solution()
    print("========================")
    print(solution.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")) # true
    end5 = time.perf_counter()
    print(f"test 5: {end5 - start5:10.6f} sec")
    #
    start6 = time.perf_counter()
    print(solution.firstMissingPositive([1, 1]))
    end6 = time.perf_counter()
    print(f"test 6: {end6 - start6:10.6f} sec")
