#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sums = []
    for i in arr:
        n_sums = [x for x in arr if x != i]
        if len(n_sums) == 0:
            n_sums = arr[:4]
            sums.append(sum(n_sums))
            break
        sums.append(sum(n_sums))
    print(min(sums), max(sums))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
