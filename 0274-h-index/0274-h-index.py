class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        max1,res,L=0,0,len(citations)
        for i in citations:
            max1=max(max1,i)
        count=[0]*(max1+1)
        for i in range(len(citations)):
            count[citations[i]]+=1
        for i in range(len(count)-2,-1,-1):
            count[i]+=count[i+1]
        for i in range(len(count)-1,-1,-1):
            if count[i]>=i:
                break
        return i
