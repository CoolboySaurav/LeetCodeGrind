class MinStack:

    def __init__(self):
        self.st = []
        self.minEle = float("inf")

    def push(self, val: int) -> None:
        if not self.st:
            self.minEle = val
        else:
            self.minEle = min(self.minEle, val)
        self.st.append(val)

    def pop(self) -> None:
        el = self.st[-1]
        self.st.pop()
        
        if self.minEle == el and self.st: 
            self.minEle = min(self.st)

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minEle


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()