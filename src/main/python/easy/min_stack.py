# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

# author li.hzh

class MinStack:

    _data = []

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._data.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self._data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._data[len(self._data) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        min = self._data[0]
        for i in range(1, len(self._data)):
            if self._data[i] < min:
                min = self._data[i]
        return min

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-1)
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)
