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
    
    subsetsOfEachCol = []
    intermediateSet2 = []
    phSet = []
    allSubSets = []
    
    arrColLen = len(arr)
    
    #assuming all rows have the same length
    arrRowLen = len(arr[0])

    #walk across rows
    #for j in range(arrRowLen):
        #walk down cols
        #for i in range(arrColLen):
        #    subsetsOfEachCol.append(arr[i][j])
            
        #    if( i > int(arrColLen/2) ):
        #        subSets.add(tuple(subsetsOfEachCol))    
    
    #walk down cols
    for i in range(arrColLen):
        #for each row, store all possible subsets of atleast half row's size
        subsetsOfEachCol.append( subsets_of_atleast_given_size(arr[i], int(arrRowLen/2)) )
    
    subsetsOfEachColColLen = len(subsetsOfEachCol)
    subsetsOfEachColRowLen = len(subsetsOfEachCol[0])
    
    for j in range( subsetsOfEachColColLen ):
        #if not at last col
        if j != subsetsOfEachColColLen - 1:
                
            #create two indixes to count across curr and below row
            for k in range( subsetsOfEachColRowLen  ):
                for p in range( subsetsOfEachColRowLen ):
                    
                    #if at first col 
                    if j == 0:
                        #concat every below row elly w/ every curr row elly
                        phSet.append( subsetsOfEachCol[j][k] + subsetsOfEachCol[j+1][p] )
                    else:
                        #concat every below row elly w/ every curr intermediate row elly
                        phSet.append( intermediateSet2[j-1][k] + subsetsOfEachCol[j+1][p] )

                    if j == subsetsOfEachColColLen - 2:
                        allSubSets.append( phSet[-1] )
                
                if j != subsetsOfEachColColLen - 2:
                
                    intermediateSet2.append( phSet )
                
                phSet = []
            
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

    arr_rows = int(input().strip())
    arr_columns = int(input().strip())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    result = getMaxProduct(arr)
    
    print(str(result) + '/n')

    #fptr.write(str(result) + '\n')

    #fptr.close()
