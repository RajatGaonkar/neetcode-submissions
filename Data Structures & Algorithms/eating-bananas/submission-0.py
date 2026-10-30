class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            m = (l+r)//2
            nh = 0
            for p in piles:
                nh += math.ceil(float(p) / m)
            if nh <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res