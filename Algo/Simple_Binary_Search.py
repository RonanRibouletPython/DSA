from typing import List

class Algorithm:
    def simpleBinarySearch(self, sorted_list: List[int], target: int) -> List[int]:
        
        # Initialize the start and end indices
        l: int = 0
        r: int = len(sorted_list) - 1
        m: int = 0
        
        while (l <= r):
            # Calculate the midle indice of the list
            m = l + (r - l) // 2
            
            if sorted_list[m] == target:
                return m
            
            # If target is greater, ignore left half
            if sorted_list[m] < target:
                l = m + 1
            
            # If target is smaller, ignore right half
            if sorted_list[m] > target:
                r = m - 1
                
        # If target not in list
        return -1
    
# Testing the algorithm

algo = Algorithm()
sorted_list: List = [2, 3, 4, 10, 40]
target: int = 10



if __name__ == "__main__":
    print(f"Index of {target} in the list: {algo.simpleBinarySearch(sorted_list, target)}")
            