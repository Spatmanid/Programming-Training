# 19/11/2019
# @author Spyros Patmanidis
#
#
# Insertion Sort
#
# You are given an array of n integers. Use insertion sort to sort the array.
#
# Complexity Analysis
# The insertion sort algorithm has time complexity of O(n^2) and space 
# complexity of O(1).

class Solution:
  def insertionSort(self, A):
    for i in range(1, len(A)):
      key = A[i]
      j = i - 1
      while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j -= 1
      A[j+1] = key
      
def main():
  sol = Solution()
  A = [4,7,3,5,1,0,2]
  sol.insertionSort(A)
  print(A)
  
if __name__ == "__main__":
  main()
