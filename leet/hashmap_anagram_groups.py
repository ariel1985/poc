'''
1. Repeat

Anagram - mix up the letters of a word to form a new word

Given a list of words, group the anagrams together in array

2. Examples

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

3. Approach

O(n^2)

strings must have same letters

strings must be same length 
define array for results

loop through the strings:
    if string is an anagram compared with the first string in the results array,
        append it to the array
    else add it to the array

O(n)

convert strings to Unicode characters and compare the counts

'''
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # results array
        results = []
        # loop through the strings
        for i, v in enumerate(strs):
            # add the first string 
            if not results:
                results.append([v])
                continue
            is_in_array = False
            # of any of the strings in the results array
            for j, r in enumerate(results):
                # if string is an anagram 
                if self.isAnagram(v, r[0]):
                    # append it to the results array
                    r.append(v)
                    is_in_array = True
                    break
            # else, if not in the array add it to the array
            if not is_in_array:
                results.append([v])
        return results
        
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
    print('Final:', s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    assert sorted([sorted(lst) for lst in s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])]) == sorted([sorted(lst) for lst in [["ate","eat","tea"],["nat","tan"],["bat"]]])
    assert s.groupAnagrams([""]) == [[""]]
    assert s.groupAnagrams(["a"]) == [["a"]]
    

test_solution()