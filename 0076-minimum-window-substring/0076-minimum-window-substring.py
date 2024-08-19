class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = -1 
        minLen = float(1e8)
        count = 0
        l = r = 0
        
        char = defaultdict(int)
        
        for i in t:
            char[i] += 1
            
        while r < len(s):
            if char[s[r]] > 0:
                count += 1
            char[s[r]] -= 1
            
            while count == len(t):
                if (r - l + 1) < minLen:
                    minLen = r - l + 1 
                    start = l
                char[s[l]] += 1
                if char[s[l]] > 0:
                    count -= 1
                l += 1
            r += 1
        
        return "" if start == -1 else s[start: start + minLen]