#!/usr/bin/env python3
## Week 1 - Video : Quick Find
## This is an Eager execution of this algorithm and will perform poorly with large dataset
## In this we store the numbers in an array and  try to match the index of the connecting
## nodes, so if in an array of 5 nodes 1 and 3 are connected the array will look like
## [0,1,2,1,4]




class DynamicConnectivity:
    def __init__(self,N):
        '''
        Complexity : n
        '''
        self.N = N
        self.id = [i for i in range(N)]
        print(self.id)

    def connected(self, p, q):
        '''
        Complexity: 1
        '''
        return self.id[p] == self.id[q] 

    def union(self, p, q):
        '''
        Complexity: n
        '''
        pid = self.id[p]
        qid = self.id[q]
        
        if not self.connected(p,q):
            for i in range(self.N):
                if self.id[i] == pid: self.id[i] = qid

    def printit(self):
        print(self.id)

    
def main():
    total_nodes = 6
    union_pairs = [(1,3), (2,4), (4,5)]
    dynamic_connectivity = DynamicConnectivity(total_nodes)
    for p,q in union_pairs:
        dynamic_connectivity.union(p,q)
        dynamic_connectivity.printit()


if __name__ == '__main__':
    main()
    
    
## Output :
## [0, 1, 2, 3, 4, 5]
## [0, 3, 2, 3, 4, 5]
## [0, 3, 4, 3, 4, 5]
## [0, 3, 5, 3, 5, 5]
