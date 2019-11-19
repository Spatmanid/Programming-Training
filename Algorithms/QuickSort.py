# 19/11/2019
# @author Spyros Patmanidis
#
#
# Quick Sort
#
# You are given an array of n integers. Use quick sort to sort the array.
#
# Complexity Analysis
# The quick sort algorithm has time complexity of O(n log n) for the 
# average case and O(n^2) for the worst case (when the array is already 
# sorted in the reverse order), and space complexity of O(log n).

from random import randint
class Solution:
  def quickSort(self, A, start, end):
    if start < end:
      mid = self.partition(A, start, end)
      self.quickSort(A, start, mid-1)
      self.quickSort(A, mid+1, end)
      
  def partition(self, A, start, end):
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
      if A[j] < pivot:
        i += 1
        A[i], A[j] = A[j], A[i]
    A[i+1], A[end] = A[end], A[i+1]
    return i + 1
    
  def randomizedQuickSort(self, A, start, end):
    if start < end:
      mid = self.randomizedPartition(A, start, end)
      self.randomizedQuickSort(A, start, mid-1)
      self.randomizedQuickSort(A, mid+1, end)
      
  def randomizedPartition(self, A, start, end):
    pivotIdx = randint(start, end)
    A[pivotIdx], A[end] = A[end], A[pivotIdx]
    return self.partition(A, start, end)
    
def main():
  sol = Solution()
  A = [4,7,3,5,1,0,2]
  sol.quickSort(A, 0, len(A)-1)
  print(A)
  A = [4,7,3,5,1,0,2]
  sol.randomizedQuickSort(A, 0, len(A)-1)
  print(A)
  
if __name__ == "__main__":
  main()
