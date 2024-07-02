class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Binary Search Approach ( Slower but important approach to remember)
        
        def binarySearch(nums, start, target):
            l, r = start, len(nums) - 1
            
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False
        
        nums.sort()
        count = 0
        answer = set()
        
        for i in xrange(len(nums)):
            if binarySearch(nums, i + 1, nums[i] + k):
                answer.add((nums[i], nums[i] + k))
        
        return len(answer)
        
        
        # HashMap Solution
        numbers = collections.Counter(nums)
        count = 0
        
        if k == 0:
            for key, val in numbers.items():
                if val > 1:
                    count += 1
            return count
    
        for key, val in numbers.items():
            if key + k in numbers:
                count += 1
        
        return count