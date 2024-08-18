from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it
from collections import defaultdict

class Solution:
    
    def checkRows(self, board: List[List[str]]) -> bool:
        
        hashset = set()
        
        for row in range(len(board)):
            for num in board[row]:
                if num!= '.':
                    if int(num) < 0 or int(num) > 9:
                        return False
                    
                    else:
                        if num in hashset:
                            return False
                        
                        hashset.add(num)
                        
                hashset.clear()  
                
                return True
                     
    def checkCols(self, board: List[List[str]]) -> bool:
        
        hashmap = {}
        list_nums = []
        
        for row in range(len(board)):
            
            for column, num in enumerate(board[row]):
                list_nums.append([])
                
                if num!= '.':
                    if num in list_nums:
                        return False
                    else:
                        list_nums[column].append(num)
                        hashmap[column] = list_nums[column]
                
            return True
        
    def checkBlocks(self, board: List[List[str]]) -> bool:
        block = ()
        list_nums = []
        res = {}
        
        map = {
                0:0,
                1:1,
                2:3, 
                10:4,
                11:5,
                12:6,
                20:7,
                21:8,
                22:9,
        }
        
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                list_nums.append([])
                if num != '.':
                    block = (i//3, j//3)
                    index = map[block[1]*10+block[0]]
                    if num in list_nums[index]:
                        return False
                    else:
                        list_nums[index].append(num)
                        res[block] = list_nums[index]
        return True                                   
    
    @time_it
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        return self.checkRows(board) and self.checkCols(board) and self.checkBlocks(board)
    
    @time_it
    def defaultDicIsValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
    
            
    
    
if __name__ == '__main__':
    
    board1 = [["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]]
    
    board2 = [["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]]

    print(f"Solution: {Solution().isValidSudoku(board1)}")
    print(f"Solution: {Solution().isValidSudoku(board2)}")
    
    print(f"Solution: {Solution().defaultDicIsValidSudoku(board1)}")
    print(f"Solution: {Solution().defaultDicIsValidSudoku(board2)}")