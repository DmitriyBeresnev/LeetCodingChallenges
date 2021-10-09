

# LeetCoding Challenge 2021. October. Day 9. Word Search II

'''

212. Word Search II
Hard

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []



Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.

Accepted
353,406
Submissions
925,378
Seen this question in a real interview before?
Word Search
Medium
Unique Paths III
Hard
You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.


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


class TrieNode:
    def __init__(self):
        self.__children = dict()
        self.__isTerminatedNode = False

    @property
    def children(self) -> dict:
        return self.__children

    @children.setter
    def children(self, children: dict) -> None:
        self.__children = children

    @property
    def isTerminatedNode(self) -> bool:
        return self.__isTerminatedNode

    @isTerminatedNode.setter
    def isTerminatedNode(self, isTerminatedNode: bool) -> None:
        self.__isTerminatedNode = isTerminatedNode


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__root = TrieNode()

    @property
    def root(self) -> TrieNode:
        return self.__root

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # set the pointer of current node on root
        curNode = self.root
        for symbol in word:
            if symbol not in curNode.children:
                # get existing children of current node
                curNodeChildren = curNode.children
                # create new node
                curNodeChildren[symbol] = TrieNode()
                # update children of current node
                curNode.children = curNodeChildren
            # move the pointer of current node
            curNode = curNode.children[symbol]
        # labeling the last node as terminated literal (mark $)
        curNode.isTerminatedNode = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curNode = self.root
        for symbol in word:
            if symbol not in curNode.children:
                return False
            curNode = curNode.children[symbol]
        return True if curNode and curNode.isTerminatedNode else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curNode = self.root
        if len(curNode.children) == 0:
            return False
        for symbol in prefix:
            if symbol not in curNode.children:
                return False
            curNode = curNode.children[symbol]
        return True


class Solution:
    def __init__(self):
        self.__nWords = 0
        self.__boardHeight = 0
        self.__boardWidth = 0

    def dfs(self, board: List[List[str]], i: int, j: int, path: str, resultWordsList: list, trieNode: TrieNode):
        if i < 0 or i >= self.__boardHeight or j < 0 or j >= self.__boardWidth:
            return
        if self.__nWords == 0:
            return
        if trieNode.isTerminatedNode:
            resultWordsList.append(path)
            # we do not want to search it once again
            trieNode.isTerminatedNode = False
            self.__nWords -= 1
        symbol = board[i][j]
        if symbol not in trieNode.children:
            return
        # mark (i,j) position in our board as visited: #
        board[i][j] = "#"
        # call dfs for all neighbours
        for xShift, yShift in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            self.dfs(board, i + xShift, j + yShift, path + symbol, resultWordsList, trieNode.children[symbol])
        # restore value of (i,j) position
        board[i][j] = symbol

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.__nWords = len(words)
        resultWordsList = list()
        trie = Trie()
        self.__boardHeight = len(board)
        self.__boardWidth = len(board[0])
        if self.__boardHeight == 1 and self.__boardWidth == 1:
            symbol = board[0][0]
            if self.__nWords == 1:
                if symbol == words[0]:
                    return words
            else:
                for word in words:
                    if symbol == word:
                        resultWordsList.append(word)
                return resultWordsList
        if self.__boardHeight == 1 and self.__boardWidth == 0:
            return []
        if self.__boardHeight == 0:
            return []
        for word in words:
            trie.insert(word)
        for i in range(self.__boardHeight):
            for j in range(self.__boardWidth):
                self.dfs(board, i, j, "", resultWordsList, trie.root)
        return resultWordsList


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.findWords(board=[["a"]], words=["b","a"]))
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.findWords(board=[["a"]], words=["bb","a"]))
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
