

# LeetCoding Challenge 2021. September. Day 29.

'''



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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curNode = head
        res = list()
        listSize = 0
        if curNode is not None:
            if head.next is not None:
                fastPointer = head
                while fastPointer is not None:
                    if fastPointer.next is not None:
                        listSize += 2
                        fastPointer = fastPointer.next.next
                    else:
                        listSize += 1
                        fastPointer = fastPointer.next
                residue = listSize % k
                nodesInBlock = listSize // k
                if listSize > k:
                    i = 0
                    isFirstBlock = True
                    partlyListHead = None
                    partlyListCur = None
                    while curNode is not None:
                        if isFirstBlock:
                            if i == 0:
                                partlyListHead = ListNode(curNode.val)
                                partlyListCur = partlyListHead
                                res.append(partlyListHead)
                            if i == nodesInBlock + residue - 1:
                                i = -1
                                isFirstBlock = False
                                partlyListCur.next = ListNode(curNode.val)
                                partlyListCur = partlyListCur.next
                            if i > 0 and i < nodesInBlock + residue:
                                partlyListCur.next = ListNode(curNode.val)
                                partlyListCur = partlyListCur.next
                        else:
                            if i == 0:
                                partlyListHead = ListNode(curNode.val)
                                partlyListCur = partlyListHead
                                res.append(partlyListHead)
                            if i == nodesInBlock - 1 and nodesInBlock > 1:
                                i = -1
                                partlyListCur.next = ListNode(curNode.val)
                                partlyListCur = partlyListCur.next
                            if i > 0 and i < nodesInBlock:
                                partlyListCur.next = ListNode(curNode.val)
                                partlyListCur = partlyListCur.next
                        i += 1
                        curNode = curNode.next
                else:
                    while curNode is not None:
                        res.append(curNode)
                        curNode = curNode.next
                    for node in res:
                        node.next = None
            else:
                res.append(head)
        nEmptyBlocks = k - len(res)
        if nEmptyBlocks > 0:
            for i in range(nEmptyBlocks):
                res.append(None)
        return res


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(solution.splitListToParts(head, 5))
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)
    head.next.next.next.next.next.next.next.next = ListNode(9)
    head.next.next.next.next.next.next.next.next.next = ListNode(10)
    print(solution.splitListToParts(head, 3))
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    print(solution.splitListToParts(head, 2))
    end3 = time.perf_counter()
    print(f"test 3: {end3 - start3:10.6f} sec")
    #
    start4 = time.perf_counter()
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    print(solution.splitListToParts(head, 3))
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
