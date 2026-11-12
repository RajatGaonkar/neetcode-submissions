class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c:[] for c in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)
        visit, cycle = set(), set()
        output = []
        
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True

            cycle.add(c)
            for p in preMap[c]:
                if not dfs(p):
                    return False
            visit.add(c)
            output.append(c)
            cycle.remove(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
