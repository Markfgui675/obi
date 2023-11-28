#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    points_highest = 0
    points_lowest = 0
    for s in range(len(scores)):
        if s == 0:
            highest = scores[s]
            lowest = scores[s]
        else:
            if scores[s] > highest:
                highest=scores[s]
                points_highest+=1
            elif scores[s] < lowest:
                lowest=scores[s]
                points_lowest+=1

    return [points_highest, points_lowest]

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
