# 21/11/2019
# @author Spyros Patmanidis
#
# References
# https://en.wikipedia.org/wiki/Disjoint-set_data_structure
#
#
# Disjoint-set data structure - Union Find
#
# A disjoint-set data structure (also called a union–find data structure) is a
# data structure that tracks a set of elements partitioned into a number of 
# disjoint subsets.
#
# Complexity analysis
# The time complexity of the algorithm is O(n) (O(log n) for union-by-rank) and 
# the space complexity is O(n).
#
# Applications
#
# Disjoint-set data structures model the partitioning of a set, for example to keep
# track of the connected components of an undirected graph. This model can then be 
# used to determine whether two vertices belong to the same component, or whether 
# adding an edge between them would result in a cycle. It is also a key component 
# in implementing Kruskal's algorithm to find the minimum spanning tree of a graph. 


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y):
        x_r = self.find(x)
        y_r = self.find(y)
        self.parent[x_r] = y_r
        
    def unionByRank(self, x, y):
        x_r = self.find(x)
        y_r = self.find(y)
        if self.rank[x_r] < self.rank[y_r]:
            self.parent[x_r] = y_r
        elif self.rank[x_r] > self.rank[y_r]:
            self.parent[y_r] = x_r
        else:
            self.parent[x_r] = y_r
            self.rank[y_r] += 1
            
class Solution:
    def countComponents(self, n, edges):
        dsu = DSU(n)
        for x, y in edges:
            dsu.union(x, y)
        return len({dsu.find(x) for x in range(n)})
        
    def detectCycle(self, n, edges):
        dsu = DSU(n)
        for x, y in edges:
            x_r, y_r = dsu.find(x), dsu.find(y)
            if x_r == y_r:
                return True
            dsu.union(x_r, y_r)
        return False

def main():
    sol = Solution()
    n = 4
    edges = [[0,1], [2,3]]
    print(sol.countComponents(n, edges))
    print(sol.detectCycle(n,edges))
    
if __name__ == "__main__":
    main()
