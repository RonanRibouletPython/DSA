from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        charSet = set()
        res = 0
        
        for i in range(len(s)):
            if s[i] not in charSet:
                charSet.add(s[i])
            
                res = max(res, len(charSet))
            else:
                charSet.clear()
        
        return res
    
if __name__ == '__main__':
    
    s1 = "abcabcbb"
    s2 = "zxyzxyz"
    s3 = "xxx"
    
    solution = Solution()
    
    print(solution.lengthOfLongestSubstring(s1))  # Output: 3
    print(solution.lengthOfLongestSubstring(s2))  # Output: 3
    print(solution.lengthOfLongestSubstring(s3))  # Output: 1