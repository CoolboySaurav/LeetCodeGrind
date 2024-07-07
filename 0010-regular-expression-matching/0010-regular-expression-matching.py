class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        memo = {}
        
        def match(i,j):

             # Check if the result is already in the memoization cache
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base case: if the pattern is exhausted, check if the string is also exhausted
            if j == len(p):
                return i == len(s)
            
            # Check if the first characters match (considering '.' as a wildcard)
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
            # If the next character in the pattern is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Two possibilities: skip 'x*' or use '*' to match one more character
                result = match(i, j + 2) or (first_match and match(i + 1, j))
            else:
                # If no '*' is present, just check the first match and move both pointers
                result = first_match and match(i + 1, j + 1)
            
            # Store the result in the memoization cache
            memo[(i, j)] = result
            return result
        
        # Start the recursive matching from the beginning of the string and pattern
        return match(0, 0)