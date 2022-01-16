# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Function Description:
# Complete the miniMaxSum function in the editor below.
# miniMaxSum has the following parameter(s):
# arr: an array of 5 integers

# Print:
# Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

# Input Format:
# A single line of five space-separated integers.

# Output Format:
# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# (The output can be greater than a 32 bit integer.)

# Hints: Beware of integer overflow! Use 64-bit Integer.


# Program:
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
    arr.sort()
    cnt=len(arr)
    min_sum=0
    max_sum=0
    for i in range(4):
        min_sum=min_sum+arr[i]
    for i in range(1,5):
        max_sum=max_sum+arr[i]
        
    print("{} {}".format(min_sum,max_sum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
