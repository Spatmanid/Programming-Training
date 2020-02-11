# Date 11/02/2020
# @author Spyros Patmanidis
#
#
# Floyd Warshall Algorithm
#
# The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem.
# The problem is to find shortest distances between every pair of vertices in a
# given edge weighted directed Graph.
#
# Complexity analysis
# The time complexity of this algorithm is O(V^3) where V is the number of
# vertices in the graph. The space complexity is O(V^2).

class FloydWarshall:
	def allPairShortestPath(self, distance):
		V = len(distance)
		path = [[-1] * V for _ in range(V)]
		for i in range(V):
			for j in range(V):
				if distance[i][j] != float('inf') and i != j:
					path[i][j] = i
		for k in range(V):
			for i in range(V):
				for j in range(V):
					if distance[i][j] > distance[i][k] + distance[k][j]:
						distance[i][j] = distance[i][k] + distance[k][j]
						path[i][j] = path[k][j]
		for i in range(V):
			if distance[i][i] < 0:
				raise KeyError('Negative Weight Cycle')
		return path
		
	def printPath(self, path, start, end):
		if start < 0 or end < 0 or start >= len(path) or end >= len(path):
			raise KeyError('Illegal Argument')
		stack = [end]
		while True:
			end = path[start][end]
			if end == -1:
				return
			stack.append(end)
			if start == end:
				break
		shortestPath = str(stack.pop())
		while stack:
			shortestPath += '->' + str(stack.pop())
		print(shortestPath)
		return
		
def main():
    graph = [[0, 3, 7, 15],
         [float('inf'), 0, -2, float('inf')],
         [float('inf'), float('inf'), 0, 2],
         [1, float('inf'), float('inf'), 0]]
	fw = FloydWarshall()
	path = fw.allPairShortestPath(graph)
	fw.printPath(path, 3, 1)
    
if __name__ == "__main__":
    main()
