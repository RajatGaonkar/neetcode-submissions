class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, cur):
            if i == len(nums):
                return cur == target
            if (i, cur) in dp:
                return dp[(i, cur)]
            dp[(i, cur)] = dfs(i+1, cur+nums[i]) + dfs(i+1, cur-nums[i])
            return dp[(i, cur)]
        return dfs(0, 0)