class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ords = {}
        for i, st in enumerate(strs):
            tot = [0]*26
            for s in st:
                tot[ord(s)-ord("a")] += 1 
            tot = tuple(tot)
            if tot in ords:
                ords[tot].append(st)
            else:
                ords[tot] = [st]
        return list(ords.values())