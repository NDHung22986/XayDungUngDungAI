class DFSSolver:

  def __init__(self, model):
    self.model = model

  def search(self):
    start = self.model.start_pos
    end = self.model.end_pos

    stack = [start]
    visited = {start}
    came_from = {}
    found = False

    while stack:
      current = stack.pop()
      if current == end:
        found = True
        break
      for nxt in self.model.get_neighbors(current):
        if nxt not in visited:
          visited.add(nxt)
          came_from[nxt] = current
          stack.append(nxt)
    return found, came_from