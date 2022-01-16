# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# Function description:
# Complete the  function in the editor below.
# diagonalDifference takes the following parameter:
# int arr[n][m]: an array of integers

# Return:
# int: the absolute diagonal difference

# Input Format:
# The first line contains a single integer, n, the number of rows and columns in the square matrix arr.
# Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].

#Output Format:
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.



# Code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diagonal_sum_1=0
    diagonal_sum_2=0
    rev_cnt=len(arr)-1
    for i in range(n):
        diagonal_sum_1=diagonal_sum_1+arr[i][i]
        diagonal_sum_2=diagonal_sum_2+arr[i][rev_cnt]
        rev_cnt=rev_cnt-1
    return abs(diagonal_sum_1-diagonal_sum_2)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
