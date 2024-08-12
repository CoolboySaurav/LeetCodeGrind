class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def helper(open, close, path):
            #Base Case
            if len(path) == 2*n:
                if open == close:
                    result.append(path)
                    return 
            
            if open < n:
                helper(open + 1, close, path + "(")
            
            if open > close:
                helper(open, close + 1, path + ")")
        helper(0,0,"")
        return result