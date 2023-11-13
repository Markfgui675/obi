#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    w = 0
    for l in s:
        if l == l.upper():
            w+=1
    return w+1

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
