class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(cur))
            for j in xrange(i,len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    cur.append(w)
                    backtrack(j+1)
                    cur.pop()
        cur = []
        res =[]
        backtrack(0)
        return res