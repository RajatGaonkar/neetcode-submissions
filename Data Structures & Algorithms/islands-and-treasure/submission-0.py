class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nc<0 or nr==R or nc==C or (nr, nc) in visit or grid[nr][nc] == -1:
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc)) 
            dist += 1

