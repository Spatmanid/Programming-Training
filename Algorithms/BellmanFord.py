# Date 11/02/2020
# @author Spyros Patmanidis
#
#
# Bellman Ford Algorithm
#
# Given a graph and a source vertex src in graph, find shortest paths 
# from source to all vertices in the given graph. The graph may contain 
# negative weight edges.
#
# Complexity analysis
# The time complexity of this algorithm is O(VE) where V is the number of
# vertices and E is the number of edges in the graph.

import collections
class BellmanFord:
    def bellmanFord(self, edges, start):
        V = set()
        for u, v, _ in edges:
            V.add(u)
            V.add(v)
        Map = collections.defaultdict(list)
        for v in V:
            Map[v] = [float('inf'), None]
        Map[start] = [0, None]
        for i in range(len(V) - 1):
            for u, v, w in edges:
                if Map[v][0] > Map[u][0] + w:
                    Map[v][0] = Map[u][0] + w
                    Map[v][1] = u
        nwc = False             # flag for negative weight cycle check
        for u, v, w in edges:
            if Map[v][0] > Map[u][0] + w:
                nwc = True
                break
        if nwc:
            print('Negative Weight Cycle')
        else:
            for v in V:
                print(self.route(Map, start, v))
        return
            
            
    def route(self, Map, start, end):
        r = ''
        while Map[end][1] != None:
            r = '->' + str(end) + r
            end = Map[end][1]
        r = str(start) + r         
        return r
        
def main():
    edges = [[4,3,1], [3,4,2], [2,4,4], [0,2,5], [1,2,-3], [0,3,8], [0,1,4]]
    bf = BellmanFord()
    bf.bellmanFord(edges, 0)
    edges = [[0,1,1], [1,2,3], [2,3,2], [3,1,-6]]
    bf.bellmanFord(edges, 0)
    
if __name__ == "__main__":
    main()
