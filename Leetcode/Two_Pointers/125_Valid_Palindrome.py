from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it


class Solution:
    @time_it
    def isPalindrome(self, s: str) -> bool:
        
        pass
        

if __name__ == '__main__':
    s1 = "Was it a car or a cat I saw?"
    s2 = "tab a cat"
    
    print(f"'{s1}' is a palindrome: {Solution().isPalindrome(s1)}")
    print(f"'{s2}' is a palindrome: {Solution().isPalindrome(s2)}")