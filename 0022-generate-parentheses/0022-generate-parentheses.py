class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]
        
        res = []
        
        def generate(left,right,path):
            if len(path) == n*2:
                res.append(path)
                return 
            
            if left < n:
                generate(left+1,right,path+'(')
            
            if right<left:
                generate(left, right+1, path+ ')')
                
        generate(0,0,'')
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if n==1:
#             return ["()"]
#         res=[]
#         def generate(countOpen,countClose,path):
#             if countOpen==countClose==n:
#                 res.append(path)
#                 return
#             if countOpen<=n and countClose<n and countOpen>countClose:
#                 generate(countOpen+1,countClose,path+"(")
#                 generate(countOpen,countClose+1,path+")")    
#             elif countOpen<=n and countClose<n and countOpen<=countClose:
#                 generate(countOpen+1,countClose,path+"(")
        
#         generate(0,0,"")
#         return res