from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it
from collections import defaultdict

class Solution:
    @time_it         
    def dicGroupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create an empty dictionary to store the anagrams
        anagram_dict = {}
        
        # Iterate over the list of strings
        for word in strs:
            # Sort the characters in the word
            sorted_word = ''.join(sorted(word))
            
            # If the sorted word is not already in the dictionary, add it with an empty list as its value
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = []
            
            # Add the original word to the list of anagrams
            anagram_dict[sorted_word].append(word)
        
        # Convert the dictionary values (list of anagrams) to lists and return them
        return list(anagram_dict.values())
    
    @time_it
    def defaultDicGroupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) # mapping character counter to list of anagrams
        
        for s in strs:
            counter = [0] * 26 # 26 English letters
            
            for c in s:
                counter[ord(c) - ord('a')] += 1
            
            res[tuple(counter)].append(s)
        
        return list(res.values())
    
# Test the solution
solution = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

if __name__ == "__main__":
    print(solution.dicGroupAnagrams(strs))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(solution.defaultDicGroupAnagrams(strs))