#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades: list[int]) -> list[int]:
    # Write your code here
    resp = []
    for n in grades:
        n5 = 0
        if n < 100 and n%5!=0:
            n = str(n)
            fn = n[0]
            if n[1] != '5':
                if int(n[1]) < 5:
                    f = 5-int(n[1])
                    f = f + int(n[1])
                    n5 = int(str(fn)+str(f))
                elif int(n[1]) > 5:
                    n5 = int(str(int(fn)+1)+str(0))
        n = int(n)
        if n >= 38 and n5 - n < 3:
            n = n5
        resp.append(n)
    return resp


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
