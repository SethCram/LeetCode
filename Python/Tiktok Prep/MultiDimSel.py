#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxProduct' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

from itertools import product

def getMaxProduct(arr):
    # Write your code here
    
    #find all possible subsets taking atleast m/2 vals from each row
    
    subSets = set() 
    
    newSet = []
    
    arrColLen = len(arr)
    
    #assuming all rows have the same length
    arrRowLen = len(arr[0])

    #walk across rows
    for j in range(arrRowLen):
        #walk down cols
        for i in range(arrColLen):
            newSet.append(arr[i][j])
            
            if( i > int(arrColLen/2) ):
                subSets.add(tuple(newSet))    
    
    pass


def subsets(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]
 
# wrapper function
def subsets_of_atleast_given_size(numbers, n):
    return [x for x in subsets(numbers) if len(x)>=n]          

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    numbers = [1, 2, 3, 4]
    n = 3
    print(subsets_of_atleast_given_size(numbers, n))

    arr_rows = int(input().strip())
    arr_columns = int(input().strip())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    result = getMaxProduct(arr)
    
    print(str(result) + '/n')

    #fptr.write(str(result) + '\n')

    #fptr.close()
