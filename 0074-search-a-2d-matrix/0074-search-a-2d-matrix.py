class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l1,r1=0,len(matrix)-1
        def binarySearch(nums, target):
            n = len(nums) # size of the array
            low, high = 0, n - 1

            # Perform the steps:
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return True
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        while l1<=r1:
            m1=l1+(r1-l1)//2
            if matrix[m1][0]>target:
                r1=m1-1

            elif matrix[m1][0]<target:
                if binarySearch(matrix[m1],target):
                    return True
                else:
                    l1=m1+1
            elif matrix[m1][0]==target:
                return True
        return False
        