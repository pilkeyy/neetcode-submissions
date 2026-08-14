class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))

        while q:
            cr, cc, ct = q.popleft()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == 1
                    and not (nr, nc) in visited
                ):
                    q.append((nr, nc, ct + 1))
                    visited.add((nr, nc))
                    grid[nr][nc] = 2
            minutes = ct
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return minutes
