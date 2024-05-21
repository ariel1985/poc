
'''
1. Repeat

function gets a list of integers and a target integer
return the indices of the two numbers such that they add up to the target

2. Example

[2,7,11,15], target = 9 -> [0,1]
[3,2,4], target = 6 -> [1,2]
[3,3], target = 6 -> [0,1]

3. Approach

create a results array
make 2 pointers:
one will iterate the array
second will iterate for every value in the array and check the sum
if sum == target return the pointers in results array
else keep searching
'''

# import List
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # create a results array
        res_dict = {}
        
        # go over the array
        for i, num in enumerate(nums):
            complement = target - num
            
            # if complement is in the array send the results
            if complement in res_dict:
                return [res_dict[complement], i]
            
            res_dict[num] = i
            
        return []


def test_solution() -> None:
    s = Solution()
    
    print(s.twoSum([2,7,11,15], 9))
    
    assert s.twoSum([2,7,11,15], 9) == [0,1]
    assert s.twoSum([3,2,4], 6) == [1,2]
    assert s.twoSum([3,3], 6) == [0,1]

test_solution()