class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island_count = 0

        def dfs(start_r, start_c):
            if (
                rows <= start_r
                or start_r < 0
                or cols <= start_c
                or start_c < 0
                or (start_r, start_c) in visited
                or grid[start_r][start_c] != "1"
            ):
                return
            visited.add((start_r, start_c))

            dfs(start_r + 1, start_c)
            dfs(start_r - 1, start_c)
            dfs(start_r, start_c + 1)
            dfs(start_r, start_c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not (r, c) in visited:
                    island_count += 1
                    dfs(r, c)
        return island_count
