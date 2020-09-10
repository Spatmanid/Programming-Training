# 19/11/2019
# @author Spyros Patmanidis
#
#
# Breadth First Search - BFS
#
# Implement the BFS algorithm for a graph. This implementations uses
# adjacency list representation of graphs.
#
# Note that this implementation traverses all the vertices of the graph.
#
# Complexity Analysis
# This algorithm has time complexity of O(V + E) where V is the number 
# of vertices in the graph and E is the number of edges in the graph. 
# The space complexity is O(V).

from collections import defaultdict, deque
class Solution:
  def __init__(self):
    self.graph = defaultdict(list)
    self.vertices = set()
    
  def createGraph(self, edges):
    for u, v in edges:
      self.graph[u].append(v)
      self.vertices.add(u)
      self.vertices.add(v)

  def BFS(self):
    def bfs_util(node):
      visited.add(node)
      queue = collections.deque([node])
      while queue:
        node = queue.popleft()
        order.append(node)
        for nei in self.graph[node]:
          if nei not in visited:
            visited.add(nei)
            queue.append(nei)
    
    visited = set()
    order = []
    for v in self.vertices:
      if v not in visited:
        bfs_util(v)
    print('->'.join(map(str, order)))
      
def main():
  edges = [ [0,1], [0,2], [0,4], [1,3], [2,3], [5,6]]
  sol = Solution()
  sol.createGraph(edges)
  sol.BFS()
  
if __name__ == "__main__":
  main()
