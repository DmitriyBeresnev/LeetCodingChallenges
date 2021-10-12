

# LeetCoding Challenge 2021. October. Day 11. Diameter of Binary Tree

'''

543. Diameter of Binary Tree
Easy

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1



Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -100 <= Node.val <= 100

Accepted
573,283
Submissions
1,103,635

Related Topics
Tree, Binary Tree, DFS

Similar Questions
Diameter of N-Ary Tree
Medium

'''


import math
import time
import collections
from typing import List, Optional
import numpy as np
import random as rnd
import itertools as it
from collections import defaultdict, Counter
import re
from functools import reduce
from functools import lru_cache
from bisect import bisect, bisect_left


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2:
    def calcBinaryTreeHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.calcBinaryTreeHeight(root.left), self.calcBinaryTreeHeight(root.right)) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        rootDiameter = self.calcBinaryTreeHeight(root.left) + self.calcBinaryTreeHeight(root.right)
        leftDiameter = self.calcBinaryTreeHeight(root.left)
        rightDiameter = self.calcBinaryTreeHeight(root.right)
        return max(rootDiameter, max(leftDiameter, rightDiameter))


class Solution:
    def __init__(self):
        self.res = 0

    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.res = max(self.res, (left + right))
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.dfs(root)
        return self.res


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
