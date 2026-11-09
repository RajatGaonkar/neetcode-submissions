class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr>=R or nc>=C or nr<0 or nc<0 or grid[nr][nc] == "0":
                        continue 
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
            
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        return res