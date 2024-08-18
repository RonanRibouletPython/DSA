from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it


class Solution:
    @time_it
    def loopSolution(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            
            for j in range(i+1, len(nums)):
                
                if nums[i] + nums[j] == target:
                    
                    return [i, j]
    @time_it           
    def mapSolution(self, nums: List[int], target: int) -> List[int]: 
        
        hashmap = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in hashmap:
                return [hashmap[complement], i]
            
            hashmap[num] = i

solution = Solution()

#Input :
nums1 = [2, 7, 11, 15]
target1 = 9

nums2 = [3, 2, 4]
target2 = 6

nums3 = [3, 3]
target3 = 6

if __name__ == '__main__':
    print(f"Bruteforce solution for {nums1} and {target1}: {solution.loopSolution(nums1, target1)}")
    print(f"Bruteforce solution for {nums2} and {target2}: {solution.loopSolution(nums2, target2)}")
    print(f"Bruteforce solution for {nums3} and {target3}: {solution.loopSolution(nums3, target3)}")
    
    print(f"Hashmap solution for {nums1} and {target1}: {solution.mapSolution(nums1, target1)}")
    print(f"Hashmap solution for {nums2} and {target2}: {solution.mapSolution(nums2, target2)}")
    print(f"Hashmap solution for {nums3} and {target3}: {solution.mapSolution(nums3, target3)}")
    
    