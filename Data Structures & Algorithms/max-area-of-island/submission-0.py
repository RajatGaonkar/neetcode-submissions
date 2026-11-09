class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visit = set()
        res = 0

        def dfs(r, c):
            if r<0 or r==R or c<0 or c==C or grid[r][c]==0 or (r, c) in visit:
                return 0
            visit.add((r, c))
            return (1 + dfs(r+1, c) + 
                        dfs(r-1, c) +
                        dfs(r, c+1) +
                        dfs(r, c-1))
        for r in range(R):
            for c in range(C):
                res = max(res, dfs(r, c))
        return res