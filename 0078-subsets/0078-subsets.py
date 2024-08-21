class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(ind, path):
            if ind >= len(nums):
                return res.append(path)
            # pick
            helper(ind + 1, path + [nums[ind]])
            # not Pick
            helper(ind + 1, path)
        helper(0, [])
        return res
        