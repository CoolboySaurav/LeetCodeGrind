class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []
        mod = int(1e9 + 7)
        
        # Calculate the left limits
        for i in range(n):
            # Maintain the stack such that it contains indices in increasing order of values
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            # If stack is empty, it means all previous elements are greater, else find the distance
            left[i] = i if not stack else i - stack[-1] - 1
            stack.append(i)
        
        # Clear the stack for re-use
        stack = []
        
        # Calculate the right limits
        for i in range(n-1, -1, -1):
            # Maintain the stack such that it contains indices in increasing order of values
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            # If stack is empty, it means all next elements are greater, else find the distance
            right[i] = (n - i - 1) if not stack else stack[-1] - i - 1
            stack.append(i)
        
        # Calculate the result
        res = 0
        for i in range(n):
            res += arr[i] * (left[i] + 1) * (right[i] + 1)
            res %= mod
        
        return res