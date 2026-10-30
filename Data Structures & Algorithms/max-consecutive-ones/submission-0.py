class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curmax = 0
        s = 0
        for n in nums:
            if n == 0:
                curmax = max(s, curmax)
                s = 0
            else:
                s += n
        return max(curmax, s)