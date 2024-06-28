class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        charMap = defaultdict(int)
        
        
        for i, c in enumerate(s):
            charMap[c] = i
        
        res = []
        size = end = 0
        
        for i, c in enumerate(s):
            size += 1
            end = max( end, charMap[c])
            
            if i == end:
                res.append(size)
                size = 0
        
        return res