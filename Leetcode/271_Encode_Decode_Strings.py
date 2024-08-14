from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""
        
        for i in range(len(strs)):
            encoded_str += "".join(strs[i])
            if i != len(strs) - 1:
                encoded_str += " "
        
        return  encoded_str
        
    def decode(self, s: str) -> List[str]:
        
        decoded_str = []
        
        decoded_str = list(s.split(" "))
        
        return decoded_str

# Testing the solution
solution = Solution()


if __name__ == "__main__":
    
    list_to_encode_decode = ["I", "love", "you", "Cricri"]
    
    encoded_string = solution.encode(list_to_encode_decode)
    decoded_list = solution.decode(encoded_string)

    print(f"Encoded String: {encoded_string}")
    print(f"Decoded list: {decoded_list}")