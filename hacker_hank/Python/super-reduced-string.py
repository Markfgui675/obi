#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    copy_s = ''
    for i in range(len(s)):
        if len(copy_s) > 0 and copy_s[-1] == s[i]:
            copy_s = copy_s[:len(copy_s)-1]
        else:
            copy_s+=s[i]
                
    if len(copy_s)>1:
        return copy_s
    return 'Empty String'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
