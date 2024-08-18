from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it

class Solution:
    @time_it
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Lenght of the array
        n = len(nums)
        
        # Result array
        res = [1] * n
        
        prefix = 1
        
        # Left to Right
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]
        
        suffix = 1
        
        # Right to Left
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res    

solution = Solution()

#Input :

nums1 = [1, 2, 3, 4]

nums2 = [0, 0, 0, 0]

nums3 = [5, 4, 3, 2, 1]

if __name__ == '__main__':
    
    print("Solution 1: \n")
    print(f"Solution for {nums1}: {solution.productExceptSelf(nums1)}")
    print(f"Solution for {nums2}: {solution.productExceptSelf(nums2)}")
    print(f"Solution for {nums3}: {solution.productExceptSelf(nums3)}\n")

    