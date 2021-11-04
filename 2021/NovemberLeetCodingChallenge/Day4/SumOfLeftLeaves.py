

# LeetCoding Challenge 2021. October. Day 4. Sum of Left Leaves

'''

404. Sum of Left Leaves
Easy

Given the root of a binary tree, return the sum of all left leaves.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:

Input: root = [1]
Output: 0



Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -1000 <= Node.val <= 1000

Accepted
288,950
Submissions
538,968


Related Topics
Tree, Depth-First Search, Breadth-First Search, Binary Tree

Similar Questions
-


[C++/Python] Recursive & Iterative DFS + BFS + Morris Traversal O(1) w/ Explanation | Beats 100%
https://leetcode.com/problems/sum-of-left-leaves/discuss/1558055/C%2B%2BPython-Recursive-and-Iterative-DFS-%2B-BFS-%2B-Morris-Traversal-O(1)-w-Explanation-or-Beats-100

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
    def sumOfLeftLeaves(self, root: Optional[TreeNode], isFromLeftJump=False) -> int:
        if not root:
            return 0

        if root.left is None and root.right is None:
            return root.val if isFromLeftJump else 0

        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, isLeft):
            if not root: return 0
            if not root.left and not root.right:
                return root.val if isLeft else 0
            return dfs(root.left, True) + dfs(root.right, False)
        return dfs(root, False)


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    solution2 = Solution2()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.sumOfLeftLeaves(root))
    print(solution2.sumOfLeftLeaves(root))
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
