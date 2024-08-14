from typing import List

class Solution:
    def loopSolution(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            
            for j in range(i+1, len(nums)):
                
                if nums[i] + nums[j] == target:
                    
                    return [i, j]

solution = Solution()

#Input :
nums1 = [2, 7, 11, 15]
target1 = 9

nums2 = [3, 2, 4]
target2 = 6

nums3 = [3, 3]
target3 = 6

if __name__ == '__main__':
    print(f"Solution for {nums1} and {target1}: {solution.loopSolution(nums1, target1)}")
    print(f"Solution for {nums2} and {target2}: {solution.loopSolution(nums2, target2)}")
    print(f"Solution for {nums3} and {target3}: {solution.loopSolution(nums3, target3)}")