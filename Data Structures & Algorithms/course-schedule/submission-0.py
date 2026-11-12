class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()

        def dfs(c):
            if c in visit:
                return False
            if preMap[c] == []:
                return True

            visit.add(c)
            for p in preMap[c]:
                if not dfs(p):
                    return False
            visit.remove(c)
            preMap[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True