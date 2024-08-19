from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        
        for i in range(len(nums)):
            # Remove elements from the deque that are out of the current window
            if q and q[0] < i - k + 1:
                q.popleft()
            
            # Remove elements from the deque that are less than the current element
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            # Add the current element index to the deque
            q.append(i)
            
            # Append the maximum element of the current window to the result
            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res
