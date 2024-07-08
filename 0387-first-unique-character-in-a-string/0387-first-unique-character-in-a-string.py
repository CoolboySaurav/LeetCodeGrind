class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = -1
        charMap = defaultdict(lambda: [0,0])
        
        for i, v in enumerate(s):
            if charMap[v][1] == 0:
                charMap[v][0] = i
            charMap[v][1] += 1
        
        minInd = float("inf")
        for char, val in charMap.items():
            if val[1] == 1:
                minInd = min(minInd, val[0])
        
        return minInd if minInd != float("inf") else -1
            
