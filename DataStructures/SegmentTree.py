# Date 11/02/2020
# @author Spyros Patmanidis
#
#
# Segment Tree
#
# A segment tree is a tree data structure for storing intervals, or segments. 
# It allows for faster querying (e.g sum or min) in these intervals. Lazy 
# propagation is useful when there are high number of updates in the input array.
#
# Time Complexity
# Time complexity to create segment tree is O(n) since new array will be at max 4n size.
# Space complexity to create segment tree is O(n) since new array will be at max 4n size. 
# Time complexity to search in segment tree is O(log𝑛) since you would at max travel 4 depths. 
# Time complexity to update in segment tree is O(log𝑛).
# Time complexity to update range in segment tree is O(𝑟𝑎𝑛𝑔𝑒).

import math
class sumSegmentTree:
    def __init__(self, arr):
        N = self.nextPowerOf2(len(arr))
        self.segmentTree = [0] * (2 * N - 1)
        self.constructTree(arr, 0, len(arr)-1, 0)
    
    def nextPowerOf2(self, x):
        return 1 if x == 0 else 2**math.ceil(math.log2(x))

    def constructTree(self, arr, low, high, pos):
        if low == high:
            self.segmentTree[pos] = arr[low]
            return
        mid = (low + high) // 2
        self.constructTree(arr, low, mid, 2*pos+1)
        self.constructTree(arr, mid+1, high, 2*pos+2)
        self.segmentTree[pos] = self.segmentTree[2*pos+1] + self.segmentTree[2*pos+2]
        
    def sumQuery(self, qlow, qhigh, low, high, pos):
        if qlow <= low and qhigh >= high:
            return self.segmentTree[pos]
        if qlow > high or qhigh < low:
            return 0
        mid = (low + high) // 2
        return self.sumQuery(qlow, qhigh, low, mid, 2*pos+1) + self.sumQuery(qlow, qhigh, mid+1, high, 2*pos+2)
    
class minSegmentTree:
    def __init__(self, arr):
        N = self.nextPowerOf2(len(arr))
        self.segmentTree = [float('inf')] * (2 * N - 1)
        self.constructTree(arr, 0, len(arr)-1, 0)
    
    def nextPowerOf2(self, x):
        return 1 if x == 0 else 2**math.ceil(math.log2(x))

    def constructTree(self, arr, low, high, pos):
        if low == high:
            self.segmentTree[pos] = arr[low]
            return
        mid = (low + high) // 2
        self.constructTree(arr, low, mid, 2*pos+1)
        self.constructTree(arr, mid+1, high, 2*pos+2)
        self.segmentTree[pos] = min(self.segmentTree[2*pos+1], self.segmentTree[2*pos+2])
        
    def minQuery(self, qlow, qhigh, low, high, pos):
        if qlow <= low and qhigh >= high:
            return self.segmentTree[pos]
        if qlow > high or qhigh < low:
            return float('inf')
        mid = (low + high) // 2
        return min(self.minQuery(qlow, qhigh, low, mid, 2*pos+1),
                   self.minQuery(qlow, qhigh, mid+1, high, 2*pos+2))
    
class maxSegmentTree:
    def __init__(self, arr):
        N = self.nextPowerOf2(len(arr))
        self.segmentTree = [float('-inf')] * (2 * N - 1)
        self.constructTree(arr, 0, len(arr)-1, 0)
    
    def nextPowerOf2(self, x):
        return 1 if x == 0 else 2**math.ceil(math.log2(x))

    def constructTree(self, arr, low, high, pos):
        if low == high:
            self.segmentTree[pos] = arr[low]
            return
        mid = (low + high) // 2
        self.constructTree(arr, low, mid, 2*pos+1)
        self.constructTree(arr, mid+1, high, 2*pos+2)
        self.segmentTree[pos] = max(self.segmentTree[2*pos+1], self.segmentTree[2*pos+2])
        
    def maxQuery(self, qlow, qhigh, low, high, pos):
        if qlow <= low and qhigh >= high:
            return self.segmentTree[pos]
        if qlow > high or qhigh < low:
            return float('-inf')
        mid = (low + high) // 2
        return max(self.maxQuery(qlow, qhigh, low, mid, 2*pos+1),
                   self.maxQuery(qlow, qhigh, mid+1, high, 2*pos+2))
