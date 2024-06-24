'''
1. repeat

Given a string, return the smallest lexicographically 
that is greater than the given string

Meaning , mix up the letters to get a new word with an 
Ascii value greater than the given string

2. examples

Input: w = "ab"
Output: "ba"

Input: w = "bb"
Output: "no answer"

Input: w = "hefg"
Output: "hegf"

3. approach

Find how to get the ascii code of the string


'''
#!/bin/python3

import math
import os
import random
import re
import sys


# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
def biggerIsGreater(w):
    # print the ascii value of w
    print('w:', w)
    # get the ascii value of the string w
    ascii_value = [ord(i) for i in w]
    print('ascii_value:', ascii_value)
    
    print('The sum of the ascii values:', sum(ascii_value))
    
    return w

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)
        print('result:', result)

    #     fptr.write(result + '\n')

    # fptr.close()
