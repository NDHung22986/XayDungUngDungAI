import time
import tkinter as tk
from tkinter import messagebox
from astar import AStarSolver
from bfs import BFSSolver
from dfs import DFSSolver
from greedy import GreedySolver
from grid_model import GridModel

ROWS = 20
COLS = 20
CELL_SIZE = 25


class PathfindingApp:

  def __init__(self, root):
    self.root = root
    self.root.title(
        "Mô phỏng Tìm kiếm - Nguyễn Đình Hùng (K24DTCN397) & Lương Công Phi"
        " (K24DTCN404)"
    )

    self.model = GridModel(ROWS, COLS)

    # Khung điều khiển
    control_frame = tk.Frame(root, padx=10, pady=10)
    control_frame.pack(side=tk.TOP, fill=tk.X)

    tk.Label(
        control_frame,
        text="SV: Nguyễn Đình Hùng (K24DTCN397) - Lương Công Phi"
        " (K24DTCN404)",
        font=("Arial", 10, "bold"),
        fg="blue",
    ).pack(anchor="w", pady=5)

    btn_frame = tk.Frame(control_frame)
    btn_frame.pack(fill=tk.X, pady=5)

    tk.Button(
        btn_frame,
        text="BFS",
        command=lambda: self.run_solver("BFS"),
        bg="#4CAF50",
        fg="white",
    ).pack(side=tk.LEFT, padx=2)
    tk.Button(
        btn_frame,
        text="DFS",
        command=lambda: self.run_solver("DFS"),
        bg="#2196F3",
        fg="white",
    ).pack(side=tk.LEFT, padx=2)
    tk.Button(
        btn_frame,
        text="Greedy",
        command=lambda: self.run_solver("Greedy"),
        bg="#FF9800",
        fg="white",
    ).pack(side=tk.LEFT, padx=2)
    tk.Button(
        btn_frame,
        text="A*",
        command=lambda: self.run_solver("A*"),
        bg="#9C27B0",
        fg="white",
    ).pack(side=tk.LEFT, padx=2)
    tk.Button(
        btn_frame, text="Xóa Đường", command=self.clear_path, bg="#607D8B", fg="white"
    ).pack(side=tk.LEFT, padx=2)
    tk.Button(
        btn_frame, text="Reset", command=self.reset_grid, bg="#F44336", fg="white"
    ).pack(side=tk.LEFT, padx=2)

    self.canvas = tk.Canvas(
        root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="white"
    )
    self.canvas.pack(pady=10)
    self.canvas.bind("<B1-Motion>", self.paint)
    self.canvas.bind("<Button-1>", self.paint)

    self.draw_grid()

  def draw_grid(self):
    self.canvas.delete("all")
    for r in range(ROWS):
      for c in range(COLS):
        x1, y1 = c * CELL_SIZE, r * CELL_SIZE
        x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
        val = self.model.grid[r][c]
        color = "white"
        if val == 1:
          color = "black"
        elif val == 2:
          color = "green"
        elif val == 3:
          color = "red"
        elif val == 4:
          color = "#B3E5FC"
        elif val == 5:
          color = "#FFEB3B"
        self.canvas.create_rectangle(
            x1, y1, x2, y2, fill=color, outline="#D3D3D3"
        )

  def paint(self, event):
    c, r = event.x // CELL_SIZE, event.y // CELL_SIZE
    if 0 <= r < ROWS and 0 <= c < COLS:
      if self.model.grid[r][c] not in [2, 3]:
        self.model.grid[r][c] = 1
        self.draw_grid()

  def clear_path(self):
    for r in range(ROWS):
      for c in range(COLS):
        if self.model.grid[r][c] in [4, 5]:
          self.model.grid[r][c] = 0
    self.draw_grid()

  def reset_grid(self):
    self.model = GridModel(ROWS, COLS)
    self.draw_grid()

  def reconstruct_path(self, came_from, current):
    path = [current]
    while current in came_from:
      current = came_from[current]
      path.append(current)
    path.reverse()
    for r, c in path:
      if self.model.grid[r][c] not in [2, 3]:
        self.model.grid[r][c] = 5
      self.draw_grid()
      self.root.update()
      time.sleep(0.02)

  def run_solver(self, name):
    self.clear_path()
    if name == "BFS":
      solver = BFSSolver(self.model)
    elif name == "DFS":
      solver = DFSSolver(self.model)
    elif name == "Greedy":
      solver = GreedySolver(self.model)
    else:
      solver = AStarSolver(self.model)

    found, came_from = solver.search()
    if found:
      self.reconstruct_path(came_from, self.model.end_pos)
    else:
      messagebox.showinfo("Thông báo", "Không tìm thấy đường đi!")