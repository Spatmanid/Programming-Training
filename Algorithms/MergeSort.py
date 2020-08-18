# 19/11/2019
# @author Spyros Patmanidis
#
#
# Merge Sort
#
# You are given an array of n integers. Use merge sort to sort the array.
#
# Complexity Analysis
# The default merge sort algorithm has time complexity of O(n log n) and space 
# complexity of O(n).

class Solution:
  def mergeSort(self, A, start, end):
    if start < end:
      mid = (start + end) // 2
      self.mergeSort(A, start, mid)
      self.mergeSort(A, mid+1, end)
      self.merge(A, start, mid, end)
    
  def merge(self, A, start, mid, end):
    L = list(A[start:mid+1])
    R = list(A[mid+1:end+1])
    i = j = 0
    k = start
    while i < len(L) and j < len(R):
      if L[i] <= R[j]:
        A[k] = L[i]
          i += 1
      else:
        A[k] = R[j]
          j += 1
      k += 1  
    while i < len(L):
      A[k] = L[i]
      i += 1
      k += 1
    while j < len(R):
      A[k] = R[j]
      j += 1
      k += 1
    
def main():
  sol = Solution()
  A = [4,7,3,5,1,0,2]
  sol.mergeSort(A, 0, len(A) - 1)
  print(A)
  
if __name__ == "__main__":
  main()
