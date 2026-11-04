import heapq


class GreedySolver:

  def __init__(self, model):
    self.model = model

  def search(self):
    start = self.model.start_pos
    end = self.model.end_pos

    pq = []
    count = 0
    heapq.heappush(pq, (self.model.heuristic(start, end), count, start))
    visited = {start}
    came_from = {}
    found = False

    while pq:
      _, _, current = heapq.heappop(pq)
      if current == end:
        found = True
        break

      for nxt in self.model.get_neighbors(current):
        if nxt not in visited:
          visited.add(nxt)
          came_from[nxt] = current
          h = self.model.heuristic(nxt, end)
          count += 1
          heapq.heappush(pq, (h, count, nxt))
    return found, came_from