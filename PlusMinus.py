# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with 6 places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^4 are acceptable.

# Function Description:
# Complete the plusMinus function in the editor below.
# plusMinus has the following parameter(s):
# int arr[n]: an array of integers

# Print:
# Print the ratios of positive, negative and zero values in the array. 
# Each value should be printed on a separate line with 6 digits after the decimal. The function should not return a value.

# Input Format:
# The first line contains an integer, n, the size of the array.
# The second line contains n space-separated integers that describe arr[n].

# Print the following 3 lines, each to 6 decimals:
# proportion of positive values
# proportion of negative values
# proportion of zeros



# Code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plus=0
    minus=0
    zero=0
    for i in range(len(arr)):
        if "-" in str(arr[i]):
            minus=minus+1
        elif "0" == str(arr[i]):
            zero=zero+1
        else:
            plus=plus+1
    print(round(plus/len(arr),6))
    print(round(minus/len(arr),6))
    print(round(zero/len(arr),6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
