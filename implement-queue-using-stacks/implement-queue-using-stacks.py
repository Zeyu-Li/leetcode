class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # flip stack once
        while self.s1:
            self.s2.append(self.s1.pop())
            
        # add element
        self.s1.append(x)
        
        # flip it back on itself with the x at the bottom
        while self.s2:
            self.s1.append(self.s2.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s1.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s1[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) + len(self.s2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()