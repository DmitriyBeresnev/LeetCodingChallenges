

# LeetCoding Challenge 2021. October. Day 8. Implement Trie (Prefix Tree)

'''

208. Implement Trie (Prefix Tree)
Medium

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.



Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True



Constraints:

    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 104 calls in total will be made to insert, search, and startsWith.

Accepted
473,714
Submissions
859,473
Seen this question in a real interview before?
Design Add and Search Words Data Structure
Medium
Design Search Autocomplete System
Hard
Replace Words
Medium
Implement Magic Dictionary
Medium
Implement Trie II (Prefix Tree)
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
    pass


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
