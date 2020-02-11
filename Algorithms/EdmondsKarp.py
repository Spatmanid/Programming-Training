# Date 11/02/2020
# @author Spyros Patmanidis
#
#
# Edmonds Karp Algorithm
#
# The Ford–Fulkerson method or Ford–Fulkerson algorithm (FFA) is a greedy 
# algorithm that computes the maximum flow in a flow network. It is sometimes 
# called a "method" instead of an "algorithm" as the approach to finding 
# augmenting paths in a residual graph is not fully specified or it is specified 
# in several implementations with different running times. It was published in 1956 
# by L. R. Ford, Jr. and D. R. Fulkerson. The name "Ford–Fulkerson" is often also 
# used for the Edmonds–Karp algorithm, which is a fully defined implementation of the 
# Ford–Fulkerson method.
#
# The idea behind the algorithm is as follows: as long as there is a path from the 
# source (start node) to the sink (end node), with available capacity on all edges 
# in the path, we send flow along one of the paths. Then we find another path, and 
# so on. A path with available capacity is called an augmenting path.
#
# Time Complexity
# A variation of the Ford–Fulkerson algorithm with guaranteed termination and a runtime 
# independent of the maximum flow value is the Edmonds–Karp algorithm, which runs in O(E^2)
# time, where E is the number of edges in the graph.

from collections import defaultdict, deque
class EdmondKarp:
    def __init__(self):
        self.graph = defaultdict(dict)
        
    def createGraph(self, edges):
        for u, v, w in edges:
            self.addEdge(u, v, w)
    
    def addEdge(self, u, v, w):
        self.graph[u][v] = int(w)
        self.graph[v][u] = 0
        
    def edmondKarp(self, edges, start, end):
        self.createGraph(edges)
        maxFlow = 0
        augPaths = []
        while True:
            queue = deque([start])
            parent = dict()
            visited = set()
            res = []
            while queue:
                u = queue.popleft()
                visited.add(u)
                for v in self.graph[u]:
                    if v == end and self.graph[u][v] > 0:
                        visited.add(v)
                        parent[v] = u
                        flow = float('inf')
                        tmp = end
                        while tmp != start:
                            flow = min(flow, self.graph[parent[tmp]][tmp])
                            res.append(tmp)
                            tmp = parent[tmp]
                        res.append(tmp)
                        augPaths.append(res[::-1])
                        maxFlow += flow
                        for i in range(len(res)-1):
                            self.graph[res[i+1]][res[i]] -= flow
                            self.graph[res[i]][res[i+1]] += flow
                        break
                    if v not in visited and self.graph[u][v] > 0:
                        visited.add(v)
                        queue.append(v)
                        parent[v] = u
                if end in visited:
                    break
            if end not in visited:
                break       
        return list(augPaths), maxFlow
		
def main():
	ek = EdmondKarp()
    edges = [['a','b','3'], ['a','d','3'], ['b','c','4'], ['c','a','3'], ['c','d','1'], ['c','e','2'],
         ['d','e','2'], ['d','f','6'], ['e','b','1'], ['e','g','1'], ['f','g','9']]
	augPaths, maxFlow = ek.edmondKarp(edges, 'a','g')
    print(augPaths)
    print(maxFlow)
    
if __name__ == "__main__":
    main()
