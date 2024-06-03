class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
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

        