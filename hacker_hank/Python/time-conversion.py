#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    answer = ''
    time = s.split(':')
    hours = int(time[0])
    minutes = int(time[1])
    seconds = time[2][0]+time[2][1]
    if 'AM' in s:
        if hours == 12 and minutes > 0:
            minutes = f'0{minutes}' if minutes < 10 else f'{minutes}'
            answer = f'00:{minutes}:{seconds}'
        elif hours == 12 and minutes == 0:
            answer = f'00:00:00'
        else:
            minutes = f'0{minutes}' if minutes < 10 else f'{minutes}'
            hours = f'0{hours}' if hours < 10 else f'{hours}'
            answer = f'{hours}:{minutes}:{seconds}'
            
    elif 'PM' in s:
        if hours >= 12:
            minutes = f'0{minutes}' if minutes < 10 else f'{minutes}'
            hours = f'0{hours}' if hours < 10 else f'{hours}'
            answer = f'{hours}:{minutes}:{seconds}'
        else:
            hours+=12
            minutes = f'0{minutes}' if minutes < 10 else f'{minutes}'
            answer = f'{hours}:{minutes}:{seconds}'
    return answer

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    #fptr.write(result + '\n')

    #fptr.close()
    print(result)
