class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_occurance = {c : i for i, c in enumerate(s)}
        
        seen = set()
        st = []
        
        for i, c in enumerate(s):
            if c not in seen:
                
                while st and st[-1] > c and last_occurance[st[-1]] > i:
                    seen.remove(st.pop())
                st.append(c)
                seen.add(c)
        
        return "".join(st)