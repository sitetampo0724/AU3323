from pacman.game import Directions
from pacman.util import raiseNotDefined
import util
from heuristics import nullHeuristic, manhattanHeuristic2, yourHeuristic
import external_lib


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem, max_depth=-1):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start position:", problem.getStartState())
    print("Are we reaching a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    print("The position of traps", problem.traps)
    """
    path = util.Path([problem.getStartState()], [], 0)
    if problem.isGoalState(problem.getStartState()):
        return []

    fringe = util.Stack()  # We use stack for DFS
    fringe.push(path)

    while not fringe.isEmpty():
        current_path = fringe.pop()
        current_loc = current_path.locations[-1]
        if problem.isGoalState(current_loc):
            return current_path.actions
        else:
            successors = problem.getSuccessors(current_loc)
            for successor in successors:
                next_loc = successor[0]
                next_action = successor[1]
                next_cost = successor[2]
                if next_loc not in current_path.locations:
                    locations = current_path.locations[:]
                    locations.append(next_loc)
                    all_actions = current_path.actions[:]
                    all_actions.append(next_action)
                    next_cost = current_path.cost + next_cost
                    path = util.Path(locations, all_actions, next_cost)
                    fringe.push(path)
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []

    fringe = util.Queue()  # We use queue for BFS
    fringe.push(util.Path([start], [], 0))

    visited = set()  # Graph search: never expand the same state twice
    visited.add(start)

    while not fringe.isEmpty():
        current_path = fringe.pop()
        current_loc = current_path.locations[-1]
        if problem.isGoalState(current_loc):
            return current_path.actions
        else:
            successors = problem.getSuccessors(current_loc)
            for successor in successors:
                next_loc = successor[0]
                next_action = successor[1]
                next_cost = successor[2]
                if next_loc not in visited:
                    visited.add(next_loc)
                    locations = current_path.locations[:]
                    locations.append(next_loc)
                    all_actions = current_path.actions[:]
                    all_actions.append(next_action)
                    new_cost = current_path.cost + next_cost
                    path = util.Path(locations, all_actions, new_cost)
                    fringe.push(path)
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []

    fringe = util.PriorityQueue()  # We use priority queue (ordered by cost) for UCS
    fringe.push(util.Path([start], [], 0), 0)

    visited = set()  # A state is settled once popped with its minimum cost
    while not fringe.isEmpty():
        current_path = fringe.pop()
        current_loc = current_path.locations[-1]
        if current_loc in visited:
            continue
        visited.add(current_loc)
        if problem.isGoalState(current_loc):
            return current_path.actions
        else:
            successors = problem.getSuccessors(current_loc)
            for successor in successors:
                next_loc = successor[0]
                next_action = successor[1]
                next_cost = successor[2]
                if next_loc not in visited:
                    locations = current_path.locations[:]
                    locations.append(next_loc)
                    all_actions = current_path.actions[:]
                    all_actions.append(next_action)
                    new_cost = current_path.cost + next_cost
                    path = util.Path(locations, all_actions, new_cost)
                    fringe.push(path, new_cost)
    return []
    

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []

    fringe = util.PriorityQueue()  # We use priority queue (ordered by cost + heuristic) for A*
    fringe.push(util.Path([start], [], 0), heuristic(start, problem))

    visited = set()  # A state is settled once popped with its minimum f-cost
    while not fringe.isEmpty():
        current_path = fringe.pop()
        current_loc = current_path.locations[-1]
        if current_loc in visited:
            continue
        visited.add(current_loc)
        if problem.isGoalState(current_loc):
            return current_path.actions
        else:
            successors = problem.getSuccessors(current_loc)
            for successor in successors:
                next_loc = successor[0]
                next_action = successor[1]
                next_cost = successor[2]
                if next_loc not in visited:
                    locations = current_path.locations[:]
                    locations.append(next_loc)
                    all_actions = current_path.actions[:]
                    all_actions.append(next_action)
                    new_cost = current_path.cost + next_cost
                    path = util.Path(locations, all_actions, new_cost)
                    fringe.push(path, new_cost + heuristic(next_loc, problem))
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
