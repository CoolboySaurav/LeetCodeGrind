class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        result = [-1]*n
        stack = []
        indexMap = {v : i for i, v in enumerate(nums1)}
        
        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]
            
            while stack and stack[-1] < num:
                stack.pop()
            if num in indexMap and stack:
                index = indexMap[num]
                result[index] = stack[-1]
            stack.append(num)
        
        return result