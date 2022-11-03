import copy
import queue

class Solution:
    def minMutation_failure(self, start: str, end: str, bank: list[str]) -> int:
        """Assumed direct path to end from start, but could be indirect.
        Speed: O(N^mutations) ish
        Space: O(1)

        Args:
            start (str): _description_
            end (str): _description_
            bank (list[str]): _description_

        Returns:
            int: _description_
        """
        
        if end not in bank:
            return -1
        
        #possibleNextMutations = []
        
        muts = 0
        
        #startList = start[:]
        
        startList = start #list(start)
        
        startListStr = str(startList)
        
        #possibleNextMutations = [ start[i] if start[i] == end[i] else end[i] for i in range(8) ]
        
        while startList != end:
            
            mutHappened = False
        
            #walk thru all start 
            for i in range(8):
                #if chars different
                if startList[i] != end[i]:
                    #startList[i] = end[i]
                    
                    #cache overwritten start char
                    ph = startList[i]
                    #overwrite 1 start char w/ end char (create mutate)
                    #startList[i] = end[i]
                    
                    startList = startList[:i] + end[i] + startList[i+1:]
                    
                    #possibleNextMutations.append( copy.copy(startList)  )
                    
                    #if mutated start not in bank
                    if startList not in bank:
                        #erase mutation
                        #startList[i] = ph
                        startList = startList[:i] + ph + startList[i+1:]
                    #if mutated start in bank
                    else:
                        muts += 1
                        
                        mutHappened = True
                        
                        #if reached end
                        if startList == end:
                            return muts
                        #else, keep mutating towards end till found 
            
            if not mutHappened:
                return -1

    def minMutation_attempt2(self, start: str, end: str, bank: list[str]) -> int:
        """Treat start as root, end as goal, and bank as middle nodes in a tree.
        Edges are when hamming distance of 1 between currNode and bank node.
        
        BFS speed: O(Vertices + Edges) so O(bankSize+2 + bankSize+1) so O(bankSize)
        space: O(bankSize)
        
        when an algorithm has O(log n) running time, it means that as the input size grows, the number of operations grows very slowly.

        Args:
            start (str): _description_
            end (str): _description_
            bank (list[str]): _description_

        Returns:
            int: _description_
        """
        
        if end not in bank:
            return -1
        
        Q = queue.Queue()
        
        bankSize = len(bank)
        
        Q.put(start)
        visited = [False] * (bankSize + 2) #tot nodes/vertices in tree
        
        depth = 0
        #already visited root
        visited[0] = True
        
        while not Q.empty():
            
            nodesAtCurrLevel = Q.qsize()
            
            depth += 1
            
            for _ in range(nodesAtCurrLevel):
                
                #print(list(Q.queue))
                
                root = Q.get()
                
                for i in range(bankSize):
                    
                    currBankNode = bank[i] 
                    
                    #calc num of diff chars tween curr root and curr bank node
                    diffChars = sum( root[j] != bank[i][j] for j in range(8) )
                    
                    if (
                        diffChars == 1 #if hamming distance of 1 bc only 1 mutated char
                        and not visited[i+1] #if not visited yet (account for root node at 0)
                    ) :
                        visited[i+1] = True
                        
                        if currBankNode == end:
                            return depth
                        else:
                            Q.put(currBankNode)
                            
                            #print(list(Q.queue))
                            
        return -1

sol = Solution()

"AACCGGTT"
"AACCGGTA"
["AACCGGTA"]
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
"AAAAACCC"
"AACCCCCC"
["AAAACCCC","AAACCCCC","AACCCCCC"]

print(sol.minMutation_attempt2(start=start, end = end, bank = bank))
                