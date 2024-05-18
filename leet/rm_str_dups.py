'''
1. Repeat :
remove numbers that are show up more than twice from a sorted array

2. Example
given: 000 will output : 00 
given: 000111 will output : 0011

3. Approach

create 2 pointers and a counter
index that runs over the array
pointer for the current cell 
counter for the amount of occurences in the array
0 - ""      No duplicates, counter is reset
1 - "1"     First appearance of the char "1"
2 - "11"    Second appearance of the char "11"

Each iteration compare the current cell with the index

Same value in both pointers:
    counter == 2 : "111" (2 or more duplicates - increment updater and keep moving with index)
        increment counter and index (skip the duplicate)
    counter < 2 : 
        increment both pointers and counter
        
Unique values in both pointers:

    reset counter
    
    counter < 2 : "012" 
        increment both pointers
    
    counter >= 2 : "112"
        copy index into cell and increment both pointers

Logic:
current cell equals to index :
  increment counter and cell
  counter == 2 : increment counter only
current cell NOT equal to index (unique value) :
  counter == 2 : 
counter < 2 : increment cell and index
  copy index into cell and reset counter 
'''

from typing import List

class Solution:
    
    def showIteration(self, arr: List[int], p1: int, p2: int) -> List[str]:
        newarr = arr.copy()
        for i in range(len(newarr)):
            if i == p1:
                newarr[i] = "="
            elif i == p2:
                newarr[i] = "-"
            else:
                newarr[i] = str(newarr[i])
        return newarr
        
    def removeDuplicates(self, nums: List[int]) -> int:
        num_of_duplicates = 0 # number of duplicates
        updater = 0
        print(">", self.showIteration(nums, 10, 10))
        for index in range(1, len(nums)):
            # same
            if nums[updater] == nums[index]:
                if num_of_duplicates < 2:
                    updater += 1
                    num_of_duplicates += 1
                    nums[updater] = nums[index]
            # unique
            else:
                updater += 1 
                num_of_duplicates = 0
                nums[updater] = nums[index]
            # index += 1 # index is always incremented in for loop
            arr = self.showIteration(nums, updater, index)
            print(index, arr, updater, num_of_duplicates, nums[updater], nums[index])
        return updater

def test_solution():
    arr = [1,1,1,2,2,3]
    solution = Solution()
    a = solution.removeDuplicates(arr)
    print(arr[:a])
    assert arr[:a] == [1,1,2,2,3,3]

    # arr = [0,0,1,1,1,1,2,3,3]
    # Solution.removeDuplicates(Solution, arr)
    # assert arr == [0,0,1,1,2,3,3,3,3]

    
test_solution()    
    