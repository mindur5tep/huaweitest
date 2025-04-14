def func():

    n = int(input().strip())
    # Parse the grid
    grid = []
    for i in range(1, n+1):
        grid.append(list(map(int, input().strip().split())))
    
    # Edge case for single cell
    if n == 1:
        print(max(0, grid[0][0]))  # Only collect if it's positive
        return

    # Initialize the DP array
    dp = [[[-float('inf')] * n for _ in range(n)] for _ in range(2 * n - 1)]
    dp[0][0][0] = grid[0][0] if grid[0][0] != -1 else -float('inf')
    
    # DP computation
    for k in range(1, 2 * n - 1):
        for x1 in range(max(0, k - (n - 1)), min(n, k + 1)):
            for x2 in range(max(0, k - (n - 1)), min(n, k + 1)):
                y1, y2 = k - x1, k - x2
                
                if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                    continue

                fruit = grid[x1][y1] + (grid[x2][y2] if x1 != x2 or y1 != y2 else 0)
                
                best = -float('inf')
                for dx1, dy1 in [(1, 0), (0, 1)]:
                    nx1, ny1 = x1 - dx1, y1 - dy1
                    for dx2, dy2 in [(1, 0), (0, 1)]:
                        nx2, ny2 = x2 - dx2, y2 - dy2
                        if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
                            best = max(best, dp[k - 1][nx1][nx2])
                
                dp[k][x1][x2] = best + fruit if best != -float('inf') else -float('inf')
    
    # Final answer
    result = max(0, dp[2 * n - 2][n - 1][n - 1])
    print(result)

if __name__ == "__main__":
    func()
