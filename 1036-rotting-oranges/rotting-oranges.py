from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        queue = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 2:
                    queue.append((i, j))

                elif grid[i][j] == 1:
                    fresh += 1

        minutes = 0

        directions = [
            (-1, 0),   # up
            (1, 0),    # down
            (0, -1),   # left
            (0, 1)     # right
        ]

        while queue and fresh > 0:


            for i in range(len(queue)):

                row, col = queue.popleft()

                for dr, dc in directions:

                    new_row = row + dr
                    new_col = col + dc

                    if (0 <= new_row < m and
                        0 <= new_col < n and
                        grid[new_row][new_col] == 1):

                        grid[new_row][new_col] = 2
                        fresh -= 1

                        queue.append((new_row, new_col))

            minutes += 1

        if fresh > 0:
            return -1

        return minutes