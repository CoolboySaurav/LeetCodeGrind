class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def find(p):
            if p == 0:
                return 0
            
            l = r = 0
            count = 0
            char = defaultdict(int)

            while r < len(nums):
                char[nums[r]] += 1

                while len(char) > p:
                    char[nums[l]] -= 1
                    if char[nums[l]] == 0:
                        del char[nums[l]]
                    l += 1

                count += (r - l + 1)
                r += 1
                
            return count

        return find(k) - find(k-1)