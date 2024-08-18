from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it

class Solution:
  
    @time_it
    def delimiterEncode(self, strs: List[str]) -> str:
        
        encoded_str = ""
        # Use a the number of characters in all strings + a delimiter to decode the string
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
            
        return encoded_str
    
    @time_it
    def delimiterDecode(self, s: str) -> List[str]:
        
        decoded_list = []
        i = 0
        
        while i < len(s):
            # Find the length of the current string
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
                    
            decoded_list.append(s[j+1: j+1+length])
            
            i = j + 1 + length
        
        return decoded_list
        
# Testing the solution
solution = Solution()

if __name__ == "__main__":
    
    list_to_encode_decode = ["I#", "love", "you2", "Cricri", "  ", "."]
        
    encoded_string = solution.delimiterEncode(list_to_encode_decode)
    decoded_list = solution.delimiterDecode(encoded_string)

    print(f"Encoded String: {encoded_string}")
    print(f"Decoded list: {decoded_list}")