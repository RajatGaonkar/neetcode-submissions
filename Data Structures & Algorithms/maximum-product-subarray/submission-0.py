class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax, cmin = 1, 1
        res = nums[0]

        for n in nums:
            pmax, pmin = cmax, cmin

            cmax = max(n, pmax*n, pmin*n)
            cmin = min(n, pmax*n, pmin*n)

            res = max(res, cmax)
        return res