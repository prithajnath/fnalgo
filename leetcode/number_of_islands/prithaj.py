from typing import List

# Leetcode class
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def neighbors(x, y, R, C):
            moveset = set()
            moves = [
                lambda x, y: (x + 1, y),
                lambda x, y: (x - 1, y),
                lambda x, y: (x, y + 1),
                lambda x, y: (x, y - 1),
            ]

            for move in moves:
                x1, y1 = move(x, y)

                if x1 >= 0 and x1 < R and y1 >= 0 and y1 < C:
                    moveset.add((x1, y1))
            return moveset

        def dfs(s, g, R, C, seen=set()):
            seen.add(s)
            x, y = s
            path = [(x, y)]
            for neighbor in neighbors(x, y, R, C):
                if neighbor in seen:
                    continue
                x1, y1 = neighbor
                if g[x1][y1] == "1":
                    path = path + dfs((x1, y1), g, R, C, seen=seen)
            return path

        R = len(grid)
        C = len(grid[0])

        visited = set()
        connected_components = []
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    if (r, c) in visited:
                        continue
                    else:
                        connected_components.append(
                            dfs((r, c), grid, R, C, seen=visited)
                        )
        print(connected_components)
        return len(connected_components)