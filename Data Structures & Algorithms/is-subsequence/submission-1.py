class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps, pt = 0, 0
        while ps<len(s) and pt<len(t):
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        if ps == len(s):
            return True
        return False