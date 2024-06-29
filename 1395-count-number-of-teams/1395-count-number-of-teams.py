class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        count = 0
        
        
        for i in xrange(n):
            leftSmaller = leftLarger = rightSmaller = rightLarger = 0
            
            for j in xrange(i):
                if rating[j] < rating[i]:
                    leftSmaller += 1
                else:
                    leftLarger += 1
            
            for k in xrange(i+1,n):
                if rating[k] < rating[i]:
                    rightSmaller += 1
                else:rightLarger += 1
            
            count += leftSmaller*rightLarger + leftLarger*rightSmaller
        
        
        return count