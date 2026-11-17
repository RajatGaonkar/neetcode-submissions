class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)-1, -1, -1):
            ndp = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                ndp.add(t+nums[i])
                ndp.add(t)
            dp = ndp
        return True if target in dp else False
            