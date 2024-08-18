from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it

class Solution:
    
    @time_it
    def bucketSortTopKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create the hashmap to store the number of times every number occurs
        hashmap = {}
        
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        # Create the bucket list a length nums
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Add the numbers to the buckets based on their frequency
        for num, freq in hashmap.items():
            buckets[freq].append(num)
        
        # Store the nums in the res list
        res = []
        
        # Iterate the occurences from highest to lowest
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
            
            
             
    

# Test the function
nums = [1, 1, 1, 2, 2, 3, 100]
k = 4

solution = Solution()

if __name__ == "__main__":
    print(solution.bucketSortTopKFrequent(nums, k))