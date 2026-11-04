import heapq


class AStarSolver:

  def __init__(self, model):
    self.model = model

  def search(self):
    start = self.model.start_pos
    end = self.model.end_pos

    pq = []
    count = 0
    heapq.heappush(pq, (self.model.heuristic(start, end), count, start))
    g_score = {start: 0}
    came_from = {}
    found = False

    while pq:
      _, _, current = heapq.heappop(pq)
      if current == end:
        found = True
        break

      for nxt in self.model.get_neighbors(current):
        temp_g = g_score[current] + 1
        if nxt not in g_score or temp_g < g_score[nxt]:
          g_score[nxt] = temp_g
          came_from[nxt] = current
          h = self.model.heuristic(nxt, end)
          f = temp_g + h
          count += 1
          heapq.heappush(pq, (f, count, nxt))
    return found, came_from