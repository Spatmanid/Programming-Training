# Date 19/11/2019
# @author Spyros Patmanidis
#
#
# Binary Search Algorithm
#
# You are given a sorted array of integers. Find the index of the target element.
# If the target is not contained in the array return -1.
#
# Complexity analysis
# The time complexity of this algorithm is O(log n) where n is the number of
# elements in the array. The space complexity is O(1) for the iterative implementation
# and O(log n) for the recursive implementation (because of the recursion stack).

class Solution:
    def binarySearchIter(self, A, start, end, target):
        while start <= end:
            mid = (start + end) // 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
        
    def binarySearchRec(self, A, start, end, target):
        if start <= end:
            mid = (start + end) // 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                return self.binarySearchRec(A, start, mid-1, target)
            else:
                return self.binarySearchRec(A, mid+1, end, target)
        return -1
        
def main():
    sol = Solution()
    A = [1,3,4,6,9,14,20,31]
    target = 20
    print(sol.binarySearchIter(A, 0, len(A)-1, target))
    print(sol.binarySearchRec(A, 0, len(A)-1, target))
    target = 7
    print(sol.binarySearchIter(A, 0, len(A)-1, target))
    print(sol.binarySearchRec(A, 0, len(A)-1, target))
    
if __name__ == "__main__":
    main()

