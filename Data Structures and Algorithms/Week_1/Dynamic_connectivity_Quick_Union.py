#!/usr/bin/env python3
## Week 1 - Video: Quick Union
## This is a lazy execution of this algorithm where the parent of an element can be determined
## by the value present in it and we can continue to do so until the value is equal to the index
## at which we know that we have reached the root of that connectivity tree

class DynamicConnectivity:
    def __init__(self, N):
        '''
        Complexity: n
        '''
        self.N = N
        self.id = [i for i in range(N)]
        print(self.id)

    def root(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p

    def connected(self, p, q):
        '''
        Complexity: 1
        '''
        return self.root(p) == self.root(q)

    def union(self, p, q):
        '''
        Complexity: Worst Case: N
        '''
        first_root = self.root(p)
        second_root = self.root(q)
        self.id[p] = second_root

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

#Output:
# [0, 1, 2, 3, 4, 5]
# [0, 3, 2, 3, 4, 5]
# [0, 3, 4, 3, 4, 5]
# [0, 3, 4, 3, 5, 5]
