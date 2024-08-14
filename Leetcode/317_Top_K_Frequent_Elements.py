from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        sort = {key: value for key, value in sorted(hashmap.items(), key=lambda x: x[1])}
        
        liste = list(sort.items())
        
        result = []
        
        for i in range(k):
            result.append(liste[-1][0])
            liste.pop(-1)
            
        return result

# Test the function
nums = [1, 1, 1, 2, 2, 3]
k = 2

sol = Solution()

if __name__ == "__main__":
    print(sol.topKFrequent(nums, k))  # Output: [1, 2]