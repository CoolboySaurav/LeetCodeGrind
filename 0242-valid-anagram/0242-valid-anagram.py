from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count = [0]*26
        
        for i in xrange(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
            
        for i in count:
            if i != 0:
                return False
            
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(s) != len(t):
#             return False

#         char_map = [0] * 26

#         for i in range(len(s)):
#             char_map[ord(s[i]) - ord('a')] += 1
#             char_map[ord(t[i]) - ord('a')] -= 1

#         return all(count == 0 for count in char_map)
        