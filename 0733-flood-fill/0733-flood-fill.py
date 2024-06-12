class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc]==color:
            return image
        m,n=len(image),len(image[0])
        direction=[[0,-1],[0,1],[1,0],[-1,0]]
        q=deque()
        q.append([sr,sc])
        ogColor=image[sr][sc]
        image[sr][sc]=color
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in direction:
                    row,col=r+dr,c+dc
                    if 0<=row<m and 0<=col<n and image[row][col]==ogColor:
                        image[row][col]=color
                        q.append([row,col])
        return image 
