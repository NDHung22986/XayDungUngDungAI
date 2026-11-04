import queue


class BFSSolver:

  def __init__(self, model):
    self.model = model

  def search(self):
    start = self.model.start_pos
    end = self.model.end_pos

    q = queue.Queue()
    q.put(start)
    visited = {start}
    came_from = {}
    found = False

    while not q.empty():
      current = q.get()
      if current == end:
        found = True
        break
      for nxt in self.model.get_neighbors(current):
        if nxt not in visited:
          visited.add(nxt)
          came_from[nxt] = current
          q.put(nxt)
    return found, came_from