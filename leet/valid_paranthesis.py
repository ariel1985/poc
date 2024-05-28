'''
1. Repeat

Make sure that every paranthesis that opens, is closed 

2. Examples

[] - True
[ - False
(] - False
[()[]] - True
[({})] - True

3. Approach

create a side stack that will hold the paranthesis
divide the paranthesis into opening and closing

loop over the string, 
if opening string - push to the stack
else if closing string 
- pop from the stack and compare 
- the popped string should be the opening string of this closing string
- if the popped string is the opening string of the closing string, continue
- else return False

At the end string should be empty

*Notice - first and last push/pop

'''

class Solution:
    def isValid(self, s: str) -> bool:
        # stack to hold the paranthesis
        stack = []
        opening = ['[', '(', '{']
        closing = [']', ')', '}']
        
        for i,v in enumerate(s):
            if v in opening:
                stack.append(v)
            elif v in closing:
                char = stack.pop()
                # get the index of the closing paranthesis
                index = closing.index(v)
                # char needs to be the opening paranthesis of the closing paranthesis
                if char == opening[index]:
                    continue
            else:
                # char is invalid
                return False
                
        
        pass
    
    
    
def test_solution():
    s = Solution()
    assert s.isValid("[]") == True
    assert s.isValid("[") == False
    assert s.isValid("(]") == False
    assert s.isValid("[()[]]") == True
    assert s.isValid("[({})]") == True
    
    
test_solution()