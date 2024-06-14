class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        if k==0:
            return res
        heap=[]
        for i,l in enumerate(points):
            p=(l[0]**2)+(l[1]**2)
            heap.append([p,l[0],l[1]])
        heapq.heapify(heap)
        while k>0:
            p,x,y=heapq.heappop(heap)
            res.append([x,y])
            k-=1
        return res



    #heapify the subtree rooted with node i(Heapify is linear time algo)
    def heapify(self,heap,N,i):
        smallest=i
        l=2*i+1
        r=2*+2
        if l<N and heap[l]<heap[i]:
            smallest=l
        if r<N and heap[r]<heap[smallest]:
            smallest=r
        if smallest!=i:
            heap[i],heap[smallest]=heap[smallest],heap[i]
            temp=heap[l]
            self.heapify(heap,N,smallest)
    
    #Function to build a Min-heap from the given array
    def buildheap(self,heap,N):
        start= N // 2 -1
        for i in range(start,-1,-1):
            self.heapify(heap,N,i)
        