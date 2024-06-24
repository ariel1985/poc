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
        """ Check if the paranthesis is valid
            stack holds the opening paranthesis and checks if the closing paranthesis is valid 

        Args:
            s (str): _description_

        Returns:
            bool: _description_
        """
        # stack to hold the paranthesis
        stack = []
        opening = ['[', '(', '{']
        closing = [']', ')', '}']
        
        # edge cases - if the string is empty
        if not s:
            return False
        # edge case - if the first paranthesis is a closing paranthesis
        if s[0] in closing:
            return False
        
        for i,v in enumerate(s):
            # print(i, '_____ v:', v, 'stack:', stack)
            if v in opening:
                stack.append(v)
            elif v in closing:
                try:
                    char = stack.pop()
                except IndexError:
                    char = False
                    
                # get the index of the closing paranthesis
                index = closing.index(v)
                # print('_____ char:', char, 'index:', index, 'opening:', opening[index])
                # char needs to be the opening paranthesis of the closing paranthesis
                if char and char == opening[index]:
                    continue
                else:
                    return False
            else:
                # char is invalid
                return False
        # stack should be empty
        return not stack
    

def test_solution():
    s = Solution()
    # print(s.isValid("(){}}{"))
    assert s.isValid("]") == False
    assert s.isValid("[]") == True
    assert s.isValid("[") == False
    assert s.isValid("(]") == False
    assert s.isValid("[()[]]") == True
    assert s.isValid("[({})]") == True
    assert s.isValid("(){}}{") == False
    

test_solution()
