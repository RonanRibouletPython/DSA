from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it, alphaNum


class Solution:
    @time_it
    def isPalindrome(self, s: str) -> bool:
        l, r = 0 , len(s)-1
        
        print(s[l], s[r])
        
        while l < r:
        
            while l < r and not alphaNum(s[l]):
                l += 1
            
            while l < r and not alphaNum(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                    
                return False
            
            l += 1
            r -= 1
        
        return True

if __name__ == '__main__':
    
    s1 = "Was it a car oR a Cat I saw?"
    s2 = "tab a cat"
    
    print(f"'{s1}' is a palindrome: {Solution().isPalindrome(s1)}")
    print(f"'{s2}' is a palindrome: {Solution().isPalindrome(s2)}")