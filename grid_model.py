class GridModel:

  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
    self.start_pos = (2, 2)
    self.end_pos = (17, 17)
    self.grid[self.start_pos[0]][self.start_pos[1]] = 2
    self.grid[self.end_pos[0]][self.end_pos[1]] = 3

  def get_neighbors(self, node):
    r, c = node
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nr, nc = r + dr, c + dc
      if 0 <= nr < self.rows and 0 <= nc < self.cols:
        if self.grid[nr][nc] != 1:  # Không phải tường
          neighbors.append((nr, nc))
    return neighbors

  def heuristic(self, a, b):
    # Khoảng cách Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])