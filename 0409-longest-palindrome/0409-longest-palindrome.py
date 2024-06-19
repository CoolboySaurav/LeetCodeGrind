class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char = set()
        countEven = 0
        
        
        for i in s:
            if i in char:
                char.remove(i)
                countEven += 2
            else:
                char.add(i)
        
        return countEven if not char else countEven + 1
        
        
        
        
        
#         hash1={}
#         for i in s:
#             if i in hash1:
#                 hash1[i]+=1
#             else:
#                 hash1[i]=1
#         count=0
#         count1=-1
#         count2=-1
# # bananas => b:1,a:3,n:2,s:1
# #naaan

#         for i,j in hash1.items():
#             if j%2==0:
#                 count+=j
#             elif j==1:
#                 count1+=1
#             elif j%2!=0 and j>2:
#                 count+=j-1
#                 count2+=1
#         if count1!=-1:
#             count+=1
#         elif count2!=-1 and count2==0 :
#             count+=1
#         elif count2>0:
#             count+=1
#         return count
