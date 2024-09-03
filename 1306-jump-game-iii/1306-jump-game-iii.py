class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        if start < 0 or start >= n:
            return False
        if not arr[start]:
            return True
        
        visit = set()
        q = deque([(start)])
        visit.add(start)
        
        while q:
            L = len(q)
            
            for i in range(L):
                index = q.popleft()
                if arr[index] == 0:
                    return True
                front, back = index + arr[index], index - arr[index]
                
                if 0 <= front < n and front not in visit:
                    q.append(front)
                    visit.add(front)
                if 0 <= back < n and back not in visit:
                    q.append(back)
                    visit.add(back)
                
                    
        return False