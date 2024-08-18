from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it


class Solution:
    @time_it
    def setHasDuplicate(self, nums: List[int]) -> bool:
        # Create a hashset
        seen = set()
        
        # Iterate over the list and return True if a value is already stored in the hashmap
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

    @time_it
    def pointerHasDuplicate(self, nums: List[int]) -> bool:
        # Sort the list
        nums.sort()
        
        # Iterate over the sorted list
        for i in range(len(nums) - 1):
            # If the current element is equal to the next element, return True
            if nums[i] == nums[i + 1]:
                return True
        
        # If no duplicate is found, return False
        return False
        
            

list1 = [1, 2, 3, 1]
list2 = [1, 2, 3, 4]
list3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

solution = Solution()



if __name__ == '__main__':
    
    print("Solution 1: \n")
    print(f"Solution for {list1}: {solution.setHasDuplicate(list1)}")
    print(f"Solution for {list2}: {solution.setHasDuplicate(list2)}")
    print(f"Solution for {list3}: {solution.setHasDuplicate(list3)}\n")
    
    print("Solution 2: \n")
    print(f"Solution for {list1}: {solution.pointerHasDuplicate(list1)}")
    print(f"Solution for {list2}: {solution.pointerHasDuplicate(list2)}")
    print(f"Solution for {list3}: {solution.pointerHasDuplicate(list3)}\n")
    
    

    
    