class MinStack(object):
        def __init__(self):
            self.stack=[]    
            self.minele=0
        def push(self, val):
            """
            :type val: int
            :rtype: None
            """
            if not self.stack:
                self.minele=val
            self.stack.append(val)
            self.minele=min(self.minele,val)
            
#1 2   
#2 1
        def pop(self):
            """
            :rtype: None
            """
            if self.stack:
                self.stack.pop()
                self.minele=self.top()
                for i in self.stack:
                    self.minele=min(self.minele,i)

        def top(self):
            """
            :rtype: int
            """
            if self.stack:
                return self.stack[-1]
            

        def getMin(self):
            """
            :rtype: int
            """
            return self.minele
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()