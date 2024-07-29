class RandomizedSet(object):

    def __init__(self):
        self.values=[]
        self.map={}
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        else:
            self.values.append(val)
            index=len(self.values)-1
            self.map[val]=index 
            return True       

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            i=self.map[val]
            last_val=self.values[-1]
            self.values[i],self.values[-1]=self.values[-1], self.values[i]
            self.map[last_val]=i
            self.values.pop()
            del self.map[val]
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.values
        )
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()