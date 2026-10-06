import external_lib


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic2(position, problem, info={}):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return  abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])  

    
def yourHeuristic(position, problem, info={}):
    """
    Exact remaining-cost heuristic for a PositionSearchProblem with traps.

    On the first call, run one reverse Dijkstra from problem.goal over the
    grid (using problem.walls / problem.traps directly, so that the search's
    _expanded counter is not polluted) under the same cost model as
    PositionSearchProblem.getSuccessors: entering a trap cell costs
    TRAP_MUL, any other cell costs 1. The result dist[cell] is the true
    optimal cost from cell to the goal, so h(position) = dist[position] is
    admissible (it never overestimates) and consistent (it satisfies the
    triangle inequality by definition of shortest paths). The table is
    cached on the problem object since the heuristic is called many times
    per search.
    """
    dist = getattr(problem, '_yourHeuristicDist', None)
    if dist is None:
        import heapq
        from pacman.searchAgents import TRAP_MUL  # lazy import: avoids a circular import at module load

        walls = problem.walls
        traps = problem.traps
        goal = problem.goal

        dist = {goal: 0}
        pq = [(0, goal)]
        while pq:
            d, (x, y) = heapq.heappop(pq)
            if d > dist.get((x, y), float('inf')):
                continue
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy
                if walls[nx][ny]:
                    continue
                step = TRAP_MUL if (nx, ny) in traps else 1
                nd = d + step
                if nd < dist.get((nx, ny), float('inf')):
                    dist[(nx, ny)] = nd
                    heapq.heappush(pq, (nd, (nx, ny)))

        problem._yourHeuristicDist = dist

    return dist.get(position, 0)
