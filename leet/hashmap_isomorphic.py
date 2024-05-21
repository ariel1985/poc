'''
Isomorphic : R <--> S
    לכל איבר בקבוצה יש תמונה יחידה בקבוצה השניה ולהיפך 
    - R and S are two strings
    - R and S are isomorphic if the characters in R can be replaced to get S
    
    same size, same shape

1. Repeate

Validate two strings are isomorphic
 - same size
 - every character in R has a unique character in S

2. Example

'egg' and 'add' are isomorphic
'foo' and 'bar' are not isomorphic - num of unique characters is different 
'paper' and 'title' are isomorphic

3. Approach

check if the size of the strings is the same
create a hashmap {} to map the chars from R to S : R[k]->S[k] 
iterate over the strings
    if the char is NOT in the hashmap
        add the char to the hashmap
    else if the char in the hashmap is not equal to the char in S
            return False

create a side dict
keys are the R values 
go over R enter the char as the key in dict
 - you want in an ideal world that every value from S will have a key from R
 
check values if key or value from the hashmap already exists in the hashmap

b -> y : True
a -> x : True
a -> y : False
b -> x : False

'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # must be the same size
        if len(s) != len(t):
            return False
        
        hashmap = {}
        
        for i, hKey in enumerate(s):
            hVal = t[i]
            
            # Key in hashmap and value is also in hashmap - ideal
            # if hKey in hashmap.keys() and hVal == hashmap[hKey]: continue
            
            # Key is already in hashmap but the value is different - bad - function can only have 1 res
            if hKey in hashmap.keys() and hVal != hashmap[hKey]: 
                return False
            
            # Key is not in hashmap keys - check the hashmap values
            if hKey not in hashmap.keys():
                # if not in keys but in values - send false alarm
                if hVal in hashmap.values():
                    return False
            
            # all else - do the mapping
            hashmap[hKey] = hVal
           
        return True

def test_solution():
    solution = Solution()
    assert solution.isIsomorphic("egg", "add") == True
    assert solution.isIsomorphic("foo", "bar") == False
    assert solution.isIsomorphic("paper", "title") == True

print('Starting test')
test_solution()
