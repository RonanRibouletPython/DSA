import sys
sys.path.append('../../Leetcode')
from utils import time_it

class SortingAlgos():
    @time_it
    def bubbleSort(self, array):
        n = len(array)-1
        
        for i in range(n):
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        
        return array
    
    @time_it
    def selectionSort(self, array):
        
        n = len(array)
        
        for i in range(n-1):
            
            min_idx = i
            
            for j in range(i+1, n, 1):
                
                if array[j] < array[min_idx]:
                    
                    min_idx = j
            
            array[i], array[min_idx] = array[min_idx], array[i]
        
        return array
    
arr = [64, 34, 25, 12, 22, 11, 90]

if __name__ == "__main__":
    print(f"Sorting  with Bubble Sort algorithm: {SortingAlgos().bubbleSort(arr)}")
    print(f"Sorting  with Selection Sort algorithm: {SortingAlgos().selectionSort(arr)}")