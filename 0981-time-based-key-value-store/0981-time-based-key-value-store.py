class TimeMap(object):

    def __init__(self):
        self.timeMap=defaultdict(list)  
        self.timeValue=defaultdict()  

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.timeMap[key].append(timestamp)
        self.timeValue[timestamp]=value
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        arr=self.timeMap[key]
        if not arr or timestamp<arr[0]:
            return ""
        elif timestamp>arr[-1]:
            return self.timeValue[arr[-1]]
        ans=l=0
        r=len(arr)-1
        while l<=r:
            m=(l+r)//2
            if arr[m]==timestamp:
                return self.timeValue[arr[m]]
            if arr[m]>=timestamp:
                ans=m-1
                r=m-1
            else:
                l=m+1
        return self.timeValue[arr[ans]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)