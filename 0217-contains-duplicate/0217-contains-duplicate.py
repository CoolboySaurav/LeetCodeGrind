from collections import defaultdict
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash1 = defaultdict(int)
        
        for i in nums:
            if i in hash1:
                return True
            hash1[i]=1
        
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         hash1={}
#         for num in nums:
#             if num not in hash1:
#                 hash1[num]=1
#                 continue
#             hash1[num]+=1
#         max_key = max(hash1, key=lambda k: hash1[k])
#         max_value = hash1[max_key]
#         if max_value>1:
#             return True
#         else:
#             return False

        