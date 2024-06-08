class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """      
        n=len(candidates)
        res=[]
        candidates.sort()
        self.combo(0,target,[],candidates,res)
        return res 
    
    
    def combo(self,i,target,ds,arr,res):
        if target==0:
            res.append(ds)
            return

        for j in xrange(i,len(arr)):
            if j>i and arr[j]==arr[j-1]:
                continue
            if arr[j]>target:
                break
            self.combo(j+1,target-arr[j],ds+[arr[j]],arr,res)
            
