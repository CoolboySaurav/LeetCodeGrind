class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def findWays(num, tar):
            n = len(num)

            # Initialize a list 'prev' to store results for the previous element
            prev = [0 for i in range(tar + 1)]

            # Initialize 'prev' based on the first element of 'num'
            if num[0] == 0:
                prev[0] = 2  # Two cases - pick and not pick
            else:
                prev[0] = 1  # One case - not pick

            if num[0] != 0 and num[0] <= tar:
                prev[num[0]] = 1  # One case - pick

            for ind in range(1, n):
                # Initialize a list 'cur' to store results for the current element
                cur = [0 for i in range(tar + 1)]
                for target in range(tar + 1):
                    notTaken = prev[target]

                    taken = 0
                    if num[ind] <= target:
                        taken = prev[target - num[ind]]

                    # Store the result in 'cur' with modulo operation
                    cur[target] = (notTaken + taken)
                prev = cur

            # Return the result for the target sum
            return prev[tar]

        tot=0
        for i in nums:
            tot+=i
        
        if tot<target or ((tot-target)%2):
            return 0
        return findWays(nums,(tot-target)/2)

        