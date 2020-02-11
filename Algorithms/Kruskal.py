# Date 11/02/2020
# @author Spyros Patmanidis
#
#
# Kruskal's Algorithm
#
# Given a connected and undirected graph, a spanning tree of that graph is a subgraph 
# that is a tree and connects all the vertices together. A single graph can have many 
# different spanning trees. A minimum spanning tree (MST) or minimum weight spanning 
# tree for a weighted, connected and undirected graph is a spanning tree with weight 
# less than or equal to the weight of every other spanning tree. The weight of a 
# spanning tree is the sum of weights given to each edge of the spanning tree.
#
#    1. Sort all the edges in non-decreasing order of their weight.
#    2. Pick the smallest edge. Check if it forms a cycle (Union-Find) 
#       with the spanning tree formed so far. If cycle is not formed, 
#       include this edge. Else, discard it.
#    3. Repeat step 2 until there are (𝑉−1) edges in the spanning tree.
#
# Complexity analysis
# The time complexity of this algorithm is O(E logE) or O(E logV), where V is the number of
# vertices in the graph and E the number of edges. Sorting of edges takes O(E log E) time. 
# After sorting, we iterate through all edges and apply find-union algorithm. The find and 
# union operations can take atmost O(logV) time. So overall complexity is O(E logE + E logV) 
# time. The value of E can be atmost O(V^2), so O(logV) and O(logE) are same. Therefore, 
# overall time complexity is O(E logE) or O(E logV).
# The space complexity is O(E + V).

class Kruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.parent = [v for v in range(vertices)]
        self.rank = [0] * vertices
        
    def createGraph(self, edges):
        for u, v, w in edges:
            self.addEdge(u, v, w)
    
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
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
            
    def kruskalMST(self):
        result = []
        i = e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(u)
            y = self.find(v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.unionByRank(x, y)
        return result
        
    def printResult(self, result):
        print("Following are the edges in the constructed MST")
        for u, v, w  in result: 
            print(f"{str(u)} -- {str(v)} == {str(w)}") 
        return
        
def main():
    edges = [[0,1,10], [0,2,6], [0,3,5], [1,3,15], [2,3,4]]
    kr = Kruskal(4)
    kr.createGraph(edges)
    result = kr.kruskalMST()
    kr.printResult(result)
    
if __name__ == "__main__":
    main()
