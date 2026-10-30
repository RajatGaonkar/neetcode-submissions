class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1m, s2m = {}, {}
        for i in range(len(s1)):
            s1m[s1[i]] = 1 + s1m.get(s1[i], 0)
            s2m[s2[i]] = 1 + s2m.get(s2[i], 0)
        if s1m == s2m:
            return True

        for j in range(len(s1), len(s2)):
            s2m[s2[j]] = 1 + s2m.get(s2[j], 0)
            o = j - len(s1)
            s2m[s2[o]] -= 1
            if s2m[s2[o]] == 0:
                del s2m[s2[o]]

            if s2m == s1m:
                return True
        return False