class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a1=[0]*26
        for m in magazine:
            i=ord(m)-ord('a')
            a1[i]+=1
        for n in ransomNote:
            i=ord(n)-ord('a')
            a1[i]-=1
            if a1[i]<0:
                return False
        return True