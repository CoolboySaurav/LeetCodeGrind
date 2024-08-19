class TimeMap:

    def __init__(self):
        self.keyTime = defaultdict(list)
        self.timeVal = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyTime[key].append(timestamp)
        self.timeVal[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        arr = self.keyTime[key]
        if not arr or timestamp < arr[0]:
            return ""
        elif timestamp > arr[-1]:
            return self.timeVal[arr[-1]]
        l, r = 0, len(arr) - 1
        ans = r
        
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == timestamp:
                return self.timeVal[arr[mid]]
            elif arr[mid] <= timestamp:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return self.timeVal[arr[ans]]
        
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)