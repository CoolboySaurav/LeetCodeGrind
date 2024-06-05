class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        path = []

        for i in range(len(position)):
          path.append([position[i],speed[i]])

        path.sort(key= lambda x:x[0])

        stack = []

        for i in range(len(position)-1,-1,-1):
            p = float((target - path[i][0]) / path[i][1])
            if not stack or p > stack[-1]:
                stack.append(p)

        return len(stack)  