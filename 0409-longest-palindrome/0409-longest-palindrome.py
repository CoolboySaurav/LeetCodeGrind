class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char = set()
        countEven = 0
              
        for i in s:
            if i in char:
                char.remove(i)
                countEven += 2
            else:
                char.add(i)
        
        return countEven if not char else countEven + 1