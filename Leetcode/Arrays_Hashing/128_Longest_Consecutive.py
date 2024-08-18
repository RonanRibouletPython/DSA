from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it

class Solution:
    @time_it
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Returns the length of the longest consecutive sequence in the given list of integers.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The length of the longest consecutive sequence.

        Example:
            >>> Solution().longestConsecutive([2, 20, 4, 10, 3, 4, 5])
            4
            >>> Solution().longestConsecutive([1, 2, 3, 4, 5])
            5
            >>> Solution().longestConsecutive([1, 3, 5, 7, 9])
            1
        """
        # Create a set from the input list to remove duplicates
        hashmap = set(nums)

        # Create an empty dictionary to store the lengths of consecutive sequences
        table = {}

        # Initialize a variable to store the maximum length of consecutive sequences
        maxval = 0

        # Iterate over each number in the set
        for num in hashmap:
            # Get the length of the consecutive sequence ending at num - 1 (or 0 if it doesn't exist)
            x = table.get(num - 1, 0)

            # Get the length of the consecutive sequence starting at num + 1 (or 0 if it doesn't exist)
            y = table.get(num + 1, 0)

            # Calculate the length of the consecutive sequence including num
            val = x + y + 1

            # Store the length of the consecutive sequence in the table
            table[num - x] = val
            table[num + y] = val

            # Update the maximum length of consecutive sequences
            maxval = max(maxval, val)

        # Return the maximum length of consecutive sequences
        return maxval

# Check if this script is being run directly (not being imported as a module)
if __name__ == '__main__':
    # Define a list of numbers
    nums1 = [2, 20, 4, 10, 3, 4, 5]
    nums2 = [0,3,2,5,4,6,1,1]

    # Print the solution for the given list of numbers
    print(f"Solution: {Solution().longestConsecutive(nums=nums1)}")
    print(f"Solution: {Solution().longestConsecutive(nums=nums2)}")