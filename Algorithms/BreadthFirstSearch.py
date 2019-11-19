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
    visited = set()
    queue = deque()
    stack = []
    for source in self.vertices:
      if source not in visited:
        queue.append(source)
        visited.add(source)
        while queue:
          cur = queue.popleft()
          stack.append(cur)
          for node in self.graph[cur]:
            if node not in visited:
              queue.append(node)
              visited.add(node)
    print('->'.join(map(str,stack)))
      
def main():
  edges = [ [0,1], [0,2], [0,4], [1,3], [2,3], [5,6]]
  sol = Solution()
  sol.createGraph(edges)
  sol.BFS()
  
if __name__ == "__main__":
  main()
