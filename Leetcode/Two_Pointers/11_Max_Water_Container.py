from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it

class Solution:
    
    @time_it
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1
        
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            
            if heights[l] >= heights[r]:
                r -= 1
            
            if  heights[l] < heights[r]:
                l += 1
            
            res = max(res, area)
        
        return res

if __name__ == '__main__':
    heights1 = [1,7,2,5,4,7,3,6]
    heights2 = [2,2,2]
    heights3 = [4, 3, 2, 1, 4]
    
    solution = Solution()
    
    print(f'Solution for {heights1}: {solution.maxArea(heights1)}') 
    print(f'Solution for {heights2}: {solution.maxArea(heights2)}')
    print(f'Solution for {heights3}: {solution.maxArea(heights3)}')