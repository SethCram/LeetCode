#!/bin/python3

from faulthandler import disable
import math
import os
import random
import re
import sys



#
# Complete the 'getMinCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY val
#  2. UNWEIGHTED_INTEGER_GRAPH t
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
# Works sometimes

# Sample Input:
# STDIN         FUNCTION
# -----         --------
# 3        →    val[] size n = 3
# 2        →    val = [2, 1, 1]
# 1
# 1
# 3 2      →    t_nodes = 3, t_edges = t_nodes - 1 = 2
# 1 2      →    t_from = [1, 1], t_to = [2, 3]
# 1 3



import queue

def getMinCost(val, t_nodes, t_from, t_to):
    # Write your code here
    
    #if no vals stored 
    #if( val == None or len(val) == 0):
    #    return 0
    
    odds = 0
    oddsPairsList = []
    
    #walk thru nodes
    for i in range(0, t_nodes):
        #cache node val
        currNodeVal = val[i]
        
        #if node val isn't even
        if(currNodeVal % 2 != 0):
            odds += 1
            #if odd number of odds
            if(odds % 2 != 0):
                #cache odd node
                oddPh = i + 1
            else:
                #append prev odd node and curr odd node to list
                oddsPairsList.append((oddPh, i + 1))
         
    print(oddsPairsList)
                
    #didn't find any odds to decr
    if len(oddsPairsList) == 0:
        return 0
    #found odds to decr
    else:
        #find simplest path between odds in pairs 
        # needa use BFS (Breadth First Search)
        
        edges = t_nodes - 1
        
        costSum = 0
        
        #queue to do BFS 
        Q = queue.Queue()
        
        for i in range(len(oddsPairsList)):
            dist_from = 1
            dist = [0] * edges
            visited = [False] * edges
            
            #put first odd node onto Q to start search from
            Q.put(oddsPairsList[i][0])
            
            while not Q.empty():
                
                print(list(Q.queue))
                
                currNode = Q.get()
                
                #if curr node is the second odd node trying to be reached
                if( currNode ==  oddsPairsList[i][1]):
                    print(f"Distance arr {dist}")
                    
                    #add up cost
                    costSum += dist_from - 1
                    #look for next odd pairs
                    break
                    
                    #return dist[currNode - 2] #should be currNode - 1?
                    
                else:
                    #cache Q size
                    qSize = Q.qsize()
                    
                    #walk thru edges
                    for j in range(len(t_from)):
                        #if edge from curr node and haven't visited it
                        if currNode == t_from[j] and not visited[j]:
                            #put dest node into Q
                            Q.put(t_to[j])
                            
                            edgeTraversed = t_from[j]-1
                            
                            #set edge's dist
                            dist[j] = dist_from
                            visited[j] = True
                        #if edge to curr node and haven't visited it
                        elif currNode == t_to[j] and not visited[j]:
                            #put dest node into Q
                            Q.put(t_from[j])
                            
                            edgeTraversed = t_from[j]-1
                            
                            #set edge's dist
                            dist[j] = dist_from
                            visited[j] = True
                        
                    #if node added
                    if qSize != Q.qsize():
                        #incr dist from 1st odd node
                        dist_from += 1
            
        return costSum

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    val_count = int(input().strip())

    val = []

    for _ in range(val_count):
        val_item = int(input().strip())
        val.append(val_item)

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    result = getMinCost(val, t_nodes, t_from, t_to)

    print(str(result) + '\n')

    #fptr.write(str(result) + '\n')

    #fptr.close()
