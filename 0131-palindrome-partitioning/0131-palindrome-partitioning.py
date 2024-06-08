class Solution(object):
# Check palindrome string or not 
    def palindrom(self,st,start,end):
        if end==start:
            return True
        while start<=end:
            if st[start]!=st[end]:
                return False
            start+=1
            end-=1
        return True
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]
        
        def partition(ind,st,path,res):
            if ind==len(st):
                res.append(path)
                return 
            for i in range(ind,len(st)):
                if self.palindrom(st,ind,i):
                    #path.append(st[ind:i+1])
                    partition(i+1,st,path+[st[ind:i+1]],res)
                    #path.pop()

        partition(0,s,[],res)
        return res


