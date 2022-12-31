from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        non_obstacles = path_counter = 0

        for row in range(0, rows):
            for col in range(0, cols):
                if grid[row][col] == 1:
                    start_row, start_col = row, col

                if grid[row][col] >= 0:
                    non_obstacles += 1

        def helper(row, col):
            nonlocal path_counter, non_obstacles

            if grid[row][col] == 2 and non_obstacles == 1:
                path_counter += 1
                return

            temp, grid[row][col] = grid[row][col], -2
            non_obstacles -= 1

            for row_offset, col_offset in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                neigh_row, neigh_col = row + row_offset, col + col_offset
                if neigh_row < 0 or neigh_row >= rows or neigh_col < 0 or neigh_col >= cols or grid[neigh_row][neigh_col] < 0:
                    continue
                helper(neigh_row, neigh_col)

            grid[row][col] = temp
            non_obstacles += 1

        helper(start_row, start_col)
        return path_counter
