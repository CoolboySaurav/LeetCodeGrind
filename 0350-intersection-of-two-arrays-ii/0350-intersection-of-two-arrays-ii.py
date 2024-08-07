class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        numMap = Counter(nums1)
        result = []
        for num in nums2:
            if num in numMap:
                result.append(num)
                numMap[num] -= 1
                if not numMap[num]:
                    numMap.pop(num)
        return result
            