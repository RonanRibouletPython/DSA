from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it

class Solution:
    
    @time_it
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        result = []
        
        for i in range(len(nums) - 1):
            first = nums[i]
            
            l, r = i+1, len(nums)-1
            
            while l < r:
                
                sum = nums[l] + nums[r] + first
                
                if sum == 0:
                    result.append([first, nums[l], nums[r]])
                    break
                
                if sum > 0:
                    r -= 1
                
                if sum < 0:
                    l += 1
                    
        return result
                
                

if __name__ == '__main__':
    s = Solution()
    
    nums = [-1, 0, 1, 2, -1, -4]
    
    print(s.threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]] but O(n^2)