from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it

class Solution:
    @time_it
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        
        while l < r:
            sum = numbers[l] + numbers[r]
            
            if sum == target:
                return [l+1, r+1]
            if sum > target:
                r -= 1
            if sum < target:
                l += 1
        
        return "No sum to be found"


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    target = 25
    
    print(f"Two sum for target {target} in array {nums}: {Solution().twoSum(nums, target)}")