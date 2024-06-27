class Solution(object):
    
    def __init__(self):
        self.result = []
    
    
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        st = list(s)
        n = len(st)
        
        def solve(ind,path, count):
            if count > 4:
                return 
            
            if ind == n:
                if count==4:
                    self.result.append(path[:-1]) # Remove last dot
                return 
            
            for i in range(1,4): # IP segments are at most 3 digits
                if ind + i > len(s):
                    break
                segment = s[ind:ind+i]
                
                # Check if the segment is valid or not
                if (segment.startswith('0') and len(segment) >1) or  (i == 3 and int(segment) > 255):
                    continue
                solve(ind + i, path + segment + ".", count + 1)
                
        solve(0,"",0)
        
        return self.result
                