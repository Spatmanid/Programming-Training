# Date 19/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/rotate-image/
#
############### Rotate Image ###############
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Note:
#     You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate 
# another 2D matrix and do the rotation.
#
# Example 1:
# Given input matrix = 
# [
#  [1,2,3],
#  [4,5,6],
#  [7,8,9]
# ],
# rotate the input matrix in-place such that it becomes:
# [
#  [7,4,1],
#  [8,5,2],
#  [9,6,3]
# ]
#
# Example 2:
# Given input matrix =
# [
#  [ 5, 1, 9,11],
#  [ 2, 4, 8,10],
#  [13, 3, 6, 7],
#  [15,14,12,16]
# ], 
# rotate the input matrix in-place such that it becomes:
# [
#  [15,13, 2, 5],
#  [14, 3, 4, 1],
#  [12, 6, 8, 9],
#  [16, 7,10,11]
# ]
#
# Complexity Analysis
# Time Complexity: O(n^2).
# Space Complexity: O(1).

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()
        print(matrix)                
            
def main():
    sol = Solution()
    matrix = [[ 1, 2, 3], [ 4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix)
    matrix = [[ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16]]
    sol.rotate(matrix)
    
if __name__ == "__main__":
    main()
