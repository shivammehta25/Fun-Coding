#!/usr/bin/env python3
"""
## Week 1 - Video: Quick Union Improvements
## This is a lazy execution of this algorithm where the parent of an element can be determined
## by the value present in it and we can continue to do so until the value is equal to the index
## at which we know that we have reached the root of that connectivity tree, what makes it better
## is the addition of weights, it subsiquently reduces the performance as now we can say that
## that depth of any node x is log_2 n
"""

class DynamicConnectivity:
    """
    Main Class with connected and union methods
    """
    def __init__(self, n):
        '''
        Complexity: n
        '''
        self.n = n
        self.weight = [0 for _ in range(n)]
        self.id = [i for i in range(n)]
        print(self.id)

    def root(self, p):
        '''
        Complexity: lg N
        '''
        while self.id[p] != p:
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
        if self.weight[first_root] <= self.weight[second_root]:
            self.id[first_root] = second_root
            self.weight[second_root] += self.weight[first_root]
        else:
            self.id[second_root] = first_root
            self.weight[first_root] += self.weight[second_root]

    def printit(self):
        """
        Prints the array
        """
        print(self.id)

def main():
    """
    Main function for running the program
    """
    total_nodes = 6
    union_pairs = [(1, 3), (2, 4), (4, 5)]
    dynamic_connectivity = DynamicConnectivity(total_nodes)
    for p, q in union_pairs:
        dynamic_connectivity.union(p, q)
        dynamic_connectivity.printit()

if __name__ == '__main__':
    main()
# Output:
# [0, 1, 2, 3, 4, 5]
# [0, 3, 2, 3, 4, 5]
# [0, 3, 4, 3, 4, 5]
# [0, 3, 4, 3, 5, 5]
