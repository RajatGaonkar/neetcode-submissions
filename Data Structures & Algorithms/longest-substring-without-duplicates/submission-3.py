class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        sett = set()
        n = len(s)
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            w = (r-l)+1
            res = max(res, w)
            sett.add(s[r])
        return res