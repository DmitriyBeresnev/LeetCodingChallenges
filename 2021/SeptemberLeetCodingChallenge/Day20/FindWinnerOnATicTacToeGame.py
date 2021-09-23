

# LeetCoding Challenge 2021. September. Day 20. Find Winner on a Tic Tac Toe Game

'''

Find Winner on a Tic Tac Toe Game

Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

    Players take turns placing characters into empty squares ' '.
    The first player A always places 'X' characters, while the second player B always places 'O' characters.
    'X' and 'O' characters are always placed into empty squares, never on filled ones.
    The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
    The game also ends if all squares are non-empty.
    No more moves can be played if the game is over.

Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.



Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.

Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.



Constraints:

    1 <= moves.length <= 9
    moves[i].length == 2
    0 <= rowi, coli <= 2
    There are no repeated elements on moves.
    moves follow the rules of tic tac toe.

   Hide Hint #1
It's straightforward to check if A or B won or not, check for each row/column/diag if all the three are the same.
   Hide Hint #2
Then if no one wins, the game is a draw iff the board is full, i.e. moves.length = 9 otherwise is pending.


Idea

    Let rows[r] is the total score after player A and player B place on the cell with row r.
    Let cols[c] is the total score after player A and player B place on the cell with col c.
    mainDiag is the total score after player A and player B place on the main diagonal cell.
    antiDiag is the total score after player A and player B place on the anti diagonal cell.
    Where player A has score 1, player B has score -1.
    When the absolute value of score by rows or cols or mainDiag or antiDiag reach to N=3 then the player who places the current cell WIN.
    Now, try yourself to solve 348. Design Tic-Tac-Toe which has N <= 100 to see the performance clearly.

Complexity:

    Time: O(moves.length)
    Space: O(N), where N = 3.


Not difficult problem, but in my opinion you need to code quite a lot for an easy problem. The idea is to keep number of X and O on each of vertical, horizontal and two diagonals. In fact we do not need to keep both of them, but do the following trick: we can add -1 to score if we meet X and +1 to score if we meet O. In this way game is finished if some score is equal to 3 or -3: if we have this numbers, it means, that we have full OOO of full XXX on the line.

So, we traverse moves one by one do the steps:

    Calculate player, it will be either 1 or -1 depending on parity of turn.
    Update rows[x], cols[y] and if needed diag and anti.
    Check if given move will finish the game: it can happen if one of the values rows[x], cols[y], diag, anti becomes equal to 3 or -3.
    In the end if we make 9 moves, we have Draw, in the opposite case it is Pending.

Complexity

If we have m moves, then we have O(m) time complexity. Space complexity is O(n), where here n = 3 is the size of our board.

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
    def tictactoe(self, moves: List[List[int]]) -> str:
        N = 3
        rows, cols = [0] * N, [0] * N
        mainDiag = antiDiag = 0

        player = 1
        for r, c in moves:
            rows[r] += player
            cols[c] += player
            if r == c: mainDiag += player
            if r + c == N - 1: antiDiag += player
            if abs(rows[r]) == N or abs(cols[c]) == N or abs(mainDiag) == N or abs(antiDiag) == N:
                return "A" if player == 1 else "B"
            player = -player

        return "Draw" if len(moves) == N * N else "Pending"


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
