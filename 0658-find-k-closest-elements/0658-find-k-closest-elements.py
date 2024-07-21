class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l, r = 0, len(arr) - k
        while l < r:
            mid = (l + r) // 2
            upperBound = arr[mid + k]
            if x - arr[mid] <= upperBound - x:
                r = mid
            else:
                l = mid + 1
        return arr[l : r + k]


    # Heap Solution
        # diff=[]
        # ### time complexity of O(n) 
        # for i in arr:
        #     diff.append([abs(x-i),i])
        # ### time complexity of O(n)
        # heapq.heapify(diff)
        # # print(diff)
        # res=[]
        # ### time complexity of O(klogn)
        # while k>0:
        #     x,y=heapq.heappop(diff)
        #     res.append(y)
        #     k-=1
        # ### time complexity of O(nlogn)    
        # res.sort()
        # return res
    #Easy difference window solution
        diff=list(map( lambda n: abs(n-x),arr))
        abs_sum=sum_min=sum(diff[0:k])
        min_i=0
        for i in range(1,len(arr)-k+1):
            abs_sum=abs_sum-diff[i-1]+diff[i+k-1]
            if abs_sum<sum_min:
                sum_min=abs_sum
                min_i=i
        return arr[min_i:min_i+k]
