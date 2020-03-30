# Date 30/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/min-stack/
#
############### Min Stack ###############
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#    push(x) -- Push element x onto stack.
#    pop() -- Removes the element on top of the stack.
#    top() -- Get the top element.
#    getMin() -- Retrieve the minimum element in the stack.
#
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minValues = []

    def push(self, x: int) -> None:
        if not self.stack or x <= self.minValues[-1]:
            self.minValues.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        if self.minValues[-1] == self.stack[-1]:
            self.minValues.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValues[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
