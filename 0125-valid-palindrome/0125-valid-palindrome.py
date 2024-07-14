class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r  = 0, len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
        
        
        
        
        
        
        
        
        
        
        s1 = ''.join(char.lower() for char in s if char.isalnum())
        s1=list(s1)
        l=0
        r=len(s1)-1
        while l<r:
            if s1[l]==s1[r]:
                l+=1
                r-=1
            else:
                return False
        return True

        