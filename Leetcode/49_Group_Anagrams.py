from typing import List

class Solution:
             
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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
    
# Test the solution
solution = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

if __name__ == "__main__":
    print(solution.groupAnagrams(strs))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]