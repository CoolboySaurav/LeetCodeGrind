class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def helper(path, open, close):
            if open == close == n:
                res.append(path)
                return 
            
            if open < n:
                helper(path + "(", open + 1, close)
            if open > close:
                helper(path + ")", open, close + 1)
        
        helper("", 0, 0)
        return res
        
        
        
#         if n == 1:
#             return ["()"]
        
#         res = []
        
#         def generate(left,right,path):
#             if len(path) == n*2:
#                 res.append(path)
#                 return 
            
#             if left < n:
#                 generate(left+1,right,path+'(')
            
#             if right<left:
#                 generate(left, right+1, path+ ')')
                
#         generate(0,0,'')
#         return res
        
        
        
        
        
        