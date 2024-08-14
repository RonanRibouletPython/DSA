from typing import List

class HashsetSolution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a hashmap
        seen = set()
        
        # Iterate over the list and return True if a value is already stored in the hashmap
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

class PointersSolution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Sort the list
        nums.sort()
        
        # Iterate over the sorted list
        for i in range(len(nums) - 1):
            # If the current element is equal to the next element, return True
            if nums[i] == nums[i + 1]:
                return True
        
        # If no duplicate is found, return False
        return False
        
            

list1 = [1, 2, 3, 1]
list2 = [1, 2, 3, 4]
list3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

solution = HashsetSolution()

solution2 = PointersSolution()

if __name__ == '__main__':
    
    print("Solution 1: \n")
    print(f"Solution for {list1}: {solution.hasDuplicate(list1)}")
    print(f"Solution for {list2}: {solution.hasDuplicate(list2)}")
    print(f"Solution for {list3}: {solution.hasDuplicate(list3)}\n")
    
    print("Solution 2: \n")
    print(f"Solution for {list1}: {solution2.hasDuplicate(list1)}")
    print(f"Solution for {list2}: {solution2.hasDuplicate(list2)}")
    print(f"Solution for {list3}: {solution2.hasDuplicate(list3)}\n")
    
    

    
    