from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        add = 0
        
        for i in range(len(nums)):
            add += nums[i]
        
        for i in range(len(nums)):
            output.append(add - nums[i])

        return output

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

    