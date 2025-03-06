class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = [-1]
        maxlen = 0

        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            else: # Pop at any cost for closing bracket to check whether closest open bracket makes it valid
                st.pop()
                if not st: # That means we dont have valid string then we need to bring the start of potentially new string to i
                    st.append(i)
                else: # If st is not empty that means we have valid string upto whatever start point is at given index i
                    maxlen = max(maxlen, i - st[-1])
        
        return maxlen