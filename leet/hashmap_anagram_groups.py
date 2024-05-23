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
            # of any of the strings in the results array
            for j, w in enumerate(results):
                # if string is an anagram 
                
                # פה הוא שואל רק על הראשון במערך
                if self.isAnagram(v, w[0]):
                    # append it to the results array
                    w.append(v)
                # else add it to the array
                else:
                    results.append([v])
                break
                
        print('results: ', results)
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
    assert s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]
    # assert s.groupAnagrams([""]) == [[""]]
    # assert s.groupAnagrams(["a"]) == [["a"]]
    

test_solution()