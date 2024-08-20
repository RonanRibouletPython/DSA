from typing import List
import sys
sys.path.append('../../Leetcode')
from utils import time_it

class Solution:
    
    @time_it
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest_price = 0
        
        for i in range(len(prices)-1):
            
            if prices[i+1] < prices[lowest_price]:
                lowest_price = i+1
            
            profit = prices[i+1] - prices[lowest_price]
            
            if profit > 0:
                res = max(res, profit)
        
        return res
    

if __name__ == '__main__':
    
    # Test case 1
    prices1 = [10,1,5,6,7,1]
    print(f'Max profit in {prices1}: {Solution().maxProfit(prices1)}')
    
    # Test case 2
    prices2 = [10,8,7,5,2]
    print(f'Max profit in {prices2}: {Solution().maxProfit(prices2)}')
    
    # Test case 3
    prices3 = [2, 4, 1]
    print(f'Max profit in {prices3}: {Solution().maxProfit(prices3)}')
    
    # Test case 4
    prices4 = [7, 6, 4, 3, 1, 2]
    print(f'Max profit in {prices4}: {Solution().maxProfit(prices4)}')