class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr=[]
        res=[]
        n=len(candidates)
        def combo(i,target):
            if i>=n or target<=0:
                if target==0:
                    res.append(arr[:])
                return 
            if candidates[i]<=target:
                arr.append(candidates[i])
                combo(i,target-candidates[i])
                arr.pop()
            combo(i+1,target)
        combo(0,target)
        return res