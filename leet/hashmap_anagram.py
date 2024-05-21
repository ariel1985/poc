'''
1. Repeat

Anagram - mix up the letters of a word to form a new word

2. Examples

aba, baa -> True
abc, baa -> False

3. Approach

O(n^2)

strings must be same length 
strings must have same letters

start with going over string s 
for every letter in s delete it from string t
if t is empty return True
else return False


O(n)

convert strings to Unicode characters and compare the counts

'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # strings must be same length 
        if len(s) != len(t):
            return False
        
        s = list(s)
        t = list(t)
                
        s.sort()
        t.sort()
        
        # compare the counts
        return s == t


def test_solution():
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") == True
    assert s.isAnagram("rat", "car") == False
    assert s.isAnagram("a", "ab") == False
    assert s.isAnagram("a", "a") == True
    assert s.isAnagram("ac", "bb") == False
    assert s.isAnagram("a", "") == False
    assert s.isAnagram("", "") == True
    assert s.isAnagram("aacc", "ccac") == False

test_solution()