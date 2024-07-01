class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        
        
        heap = []
        
        maper = collections.Counter(s)
        
        for k, v in maper.items():
            heapq.heappush(heap, (-v,k))
        
        res = ""
        
        while len(heap) > 1:
            freq1, char1 = heapq.heappop(heap)
            freq2, char2 = heapq.heappop(heap)
            res += char1 + char2
            if -freq1 > 1:
                heapq.heappush(heap, (freq1 + 1, char1))
            if -freq2 > 1:
                heapq.heappush(heap, (freq2 + 1, char2))
        
        if heap:
            freq, char = heapq.heappop(heap)
            if -freq > 1:
                return ""
            res += char
        return res
        