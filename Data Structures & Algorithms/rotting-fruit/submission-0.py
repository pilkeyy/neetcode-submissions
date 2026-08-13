class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        minutes = 0

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
        while q:
            cr, cc, curr_t = q.popleft()
            minutes = curr_t
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and not (nr, nc) in visited
                    and grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2
                    q.append((nr, nc, curr_t + 1))
                    visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                print(grid[r][c])
                if grid[r][c] == 1:
                    return -1
        return minutes
