#!/usr/bin/env python3
## Week 1 - Video: Quick Union
## This with addon to the weights, uses path compression which yields an aromatized time complexity
## of linear time, we just assign not the parent but the grandparent of the tree so with just one line
## we improve the code majorly. In this we flatten the tree a little bit
## This is a lazy execution of this algorithm where the parent of an element can be determined
## by the value present in it and we can continue to do so until the value is equal to the index
## at which we know that we have reached the root of that connectivity tree, what makes it better
## is the addition of weights, it subsiquently reduces the performance as now we can say that
## that depth of any node x is log_2 n

class DynamicConnectivity:
    def __init__(self, N):
        '''
        Complexity: n
        '''
        self.N = N
        self.weight = [0 for _ in range(N)]
        self.id = [i for i in range(N)]
        print(self.id)

    def root(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]] # With just this line we improve the complexity by a major factor
            p = self.id[p]
        return p

    def connected(self, p, q):
        '''
        Complexity: lg N
        '''
        return self.root(p) == self.root(q)

    def union(self, p, q):
        '''
        Complexity: Worst Case: lg N
        '''
        first_root = self.root(p)
        second_root = self.root(q)
        if self.weight[first_root] <= self.weight[second_root] :
            self.id[first_root] = second_root
            self.weight[second_root] += self.weight[first_root]
        else:
            self.id[second_root] = first_root
            self.weight[first_root] += self.weight[second_root]

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




# Output: 
# [0, 1, 2, 3, 4, 5]
# [0, 3, 2, 3, 4, 5]
# [0, 3, 4, 3, 4, 5]
# [0, 3, 4, 3, 5, 5]
