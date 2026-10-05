"""
Homework 0 — Python Programming for Artificial Intelligence

Instructions:
1. Complete all sections marked with TODO.
2. Do not rename functions/classes or change function parameters.
3. You may add helper functions if needed.
4. Run this file with:

    python homework.py

Recommended:
    Python >= 3.10
    numpy
"""

import math
import numpy as np


# ============================================================
# Problem 1. Basic Python Programming
# ============================================================

def basic_statistics(numbers):
    """
    Args:
        numbers: a non-empty list of numbers

    Returns:
        total, mean, maximum, minimum

    Restrictions:
        Do not use sum(), max(), or min().
    """
    # TODO
    length = len(numbers)

    total = 0
    maximum = numbers[0]
    minimum = numbers[0]

    for i in range (0,length):
        total += numbers[i]
        if numbers[i]>maximum:
            maximum = numbers[i]
        elif numbers[i]<minimum:
            minimum = numbers[i]
    mean = total / length
    return total, mean, maximum, minimum


# ============================================================
# Problem 2. Conditional Statements
# ============================================================

def get_grade(score):
    """
    Convert a numerical score into a letter grade.

    90-100 -> A
    80-89  -> B
    70-79  -> C
    60-69  -> D
    < 60   -> F

    Invalid score (< 0 or > 100) -> "Invalid"
    """
    # TODO
    if score>=90 and score<=100:
        return 'A'
    elif score>=80 and score<=89:
        return 'B'
    elif score>=70 and score<=79:
        return 'C'
    elif score>=60 and score<=69:
        return 'D'
    elif score>=0 and score<=59:
        return 'F'
    else:
        return 'Invalid'


# ============================================================
# Problem 3. Lists and Loops
# ============================================================

def filter_numbers(numbers, threshold):
    """
    Return all numbers strictly greater than threshold.
    """
    # TODO
    result = []
    length = len(numbers)
    for i in range (0,length):
        if numbers[i] >  threshold:
            result.append(numbers[i])
    return result


def count_even_odd(numbers):
    """
    Returns:
        (number_of_even_numbers, number_of_odd_numbers)
    """
    # TODO
    even_count = 0
    odd_count = 0

    length = len(numbers)
    for i in range(0, length):
        if numbers[i] % 2==0:
            even_count+=1
        elif numbers[i]%2 != 0:
            odd_count+=1

    return even_count, odd_count


# ============================================================
# Problem 4. Dictionary
# ============================================================

def best_state(values):
    """
    Args:
        values: dict mapping state -> value

    Returns:
        the state with the largest value

    Restriction:
        Do not use max(values, key=values.get).
    """
    # TODO
    length = len(values)
    max_value = 0
    index = None
    for key in values.keys():
        if values[key]>max_value:
            max_value = values[key]
            index = key
    return index

def update_value(values, state, new_value):
    """
    Update values[state] if it exists.
    Otherwise create a new state.

    The function modifies the dictionary in place.
    """
    # TODO
    isExist = False
    for key in values.keys():
        if state==key:
            values[key] = new_value
            isExist = True

    if not isExist:
        values[state] = new_value

# ============================================================
# Problem 5. Functions and Distance
# ============================================================

def manhattan_distance(p1, p2):
    """
    Manhattan distance between two 2D points.
    """
    # TODO
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def euclidean_distance(p1, p2):
    """
    Euclidean distance between two 2D points.
    """
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)



# ============================================================
# Problem 6. Introduction to Class
# ============================================================

class Point:
    def __init__(self, x, y):
        # TODO
        self.point_x = x
        self.point_y = y

    def move(self, dx, dy):
        """
        Move the point by (dx, dy).
        """
        # TODO
        self.point_x += dx
        self.point_y += dy
    def distance_to(self, other):
        """
        Calculate Euclidean distance to another Point.
        """
        # TODO
        return math.sqrt((self.point_x - other.point_x) ** 2 + (self.point_y - other.point_y) ** 2)


    def get_position(self):
        """
        Return (x, y).
        """
        # TODO
        return self.point_x , self.point_y


# ============================================================
# Problem 7. Agent Class
# ============================================================

class Agent:
    def __init__(self, x, y):
        """
        Initialize an agent at (x, y).

        self.history should contain the initial position.
        """
        # TODO
        self.Agent_x = x
        self.Agent_y = y
        self.history = [(x,y)]

    def get_position(self):
        """
        Return the current position as (x, y).
        """
        # TODO
        return self.Agent_x , self.Agent_y

    def set_position(self, position):
        """
        Set the agent position and append it to history
        only if the position changes.
        """
        # TODO
        if position != (self.Agent_x, self.Agent_y):
            self.Agent_x, self.Agent_y = position
            self.history.append(position)

    def move(self, action):
        """
        Move without checking obstacles/boundaries.

        UP    -> (x - 1, y)
        DOWN  -> (x + 1, y)
        LEFT  -> (x, y - 1)
        RIGHT -> (x, y + 1)

        Invalid actions leave the agent unchanged.
        """
        # TODO

        x, y = self.Agent_x, self.Agent_y

        if action == 'UP':
            new_pos = (x - 1, y)
        elif action == 'DOWN':
            new_pos = (x + 1, y)
        elif action == 'LEFT':
            new_pos = (x, y - 1)
        elif action == 'RIGHT':
            new_pos = (x, y + 1)
        else:
            return None

        self.set_position(new_pos)

# ============================================================
# Problem 8-10. GridWorld Class
# ============================================================

class GridWorld:
    ACTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]

    def __init__(self, grid):
        """
        Args:
            grid: 2D list
                  0 = free
                  1 = obstacle
        """
        # TODO
        self.grid = grid
        self.height = len(self.grid)
        self.width = len(self.grid[0])
    def get_height(self):
        # TODO
        return self.height

    def get_width(self):
        # TODO
        return self.width

    def is_inside(self, position):
        """
        Return True if position is inside the grid.
        """
        # TODO
        return (position[0] >=0 and position[0] <= self.width) and  (position[1] >=0 and position[1] <= self.height)

    def is_obstacle(self, position):
        """
        Return True if position is an obstacle.

        You may assume this function is only called
        for positions inside the map.
        """
        # TODO
        return self.grid[position[0]][position[1]] == 1

    def is_valid(self, position):
        """
        A valid position:
        1. is inside the grid
        2. is not an obstacle
        """
        # TODO
        return self.is_inside(position) and not self.is_obstacle(position)

    def get_next_state(self, state, action):
        """
        Compute:

            state + action -> next_state

        If the candidate next state is invalid,
        return the original state.
        """
        x, y = state

        if action == "UP":
            candidate = (x - 1, y)

        elif action == "DOWN":
            # TODO
            candidate = (x + 1, y)

        elif action == "LEFT":
            # TODO
            candidate = (x, y - 1)

        elif action == "RIGHT":
            # TODO
            candidate = (x, y + 1)

        else:
            return state

        # TODO:
        # return candidate if valid, otherwise state
        if self.is_valid(candidate):
            return candidate
        else:
            return state

    def get_valid_actions(self, state):
        """
        Return all actions that move the agent
        from state to a different valid state.
        """
        # TODO
        valid_actions = []
        candidate = state
        if state != self.get_next_state(state, 'UP'):
            valid_actions.append('UP')
            state = candidate
        if state != self.get_next_state(state, 'DOWN'):
            valid_actions.append('DOWN')
            state = candidate
        if state != self.get_next_state(state, 'LEFT'):
            valid_actions.append('LEFT')
            state = candidate
        if state != self.get_next_state(state, 'RIGHT'):
            valid_actions.append('RIGHT')
            state = candidate
        return valid_actions


# ============================================================
# Problem 11. NumPy
# ============================================================

def vector_operations(a, b):
    """
    Args:
        a, b: NumPy arrays with the same shape

    Returns:
        addition,
        subtraction,
        elementwise_product,
        dot_product
    """
    # TODO
    addition = a + b
    subtraction = a - b
    elementwise_product = a * b
    dot_product = a @ b

    return addition, subtraction, elementwise_product, dot_product


# ============================================================
# Problem 12. Mini Project
# ============================================================

def run_agent(world, agent, actions):
    """
    Execute a sequence of actions in GridWorld.

    The world decides whether each move is valid.
    The Agent stores its actual movement history.

    Returns:
        final position
    """
    for action in actions:
        current_state = agent.get_position()

        next_state = world.get_next_state(
            current_state,
            action
        )
        # TODO:
        # update agent position
        if next_state != current_state:
            agent.set_position(next_state)

    return agent.get_position()


def reached_goal(agent, goal):
    """
    Return True if the agent is at goal.
    """
    # TODO
    return agent.get_position() == goal


# ============================================================
# Bonus. Greedy Robot
# ============================================================

def greedy_agent(world, start, goal, max_steps=100):
    """
    A simple greedy agent.

    At each step:
    1. get valid actions
    2. compute each next state
    3. choose the unvisited next state with the smallest
       Manhattan distance to the goal
    4. stop when goal is reached or max_steps is exceeded

    Returns:
        path: list of visited positions
    """
    # TODO
    path = [start]
    visited = {start}
    current = start

    for i in range(max_steps):
        if current == goal:
            break

        candidates = []
        for action in world.get_valid_actions(current):
            nxt = world.get_next_state(current, action)
            if nxt not in visited:
                candidates.append(nxt)

        if not candidates:
            break

        current = min(candidates, key=lambda p: manhattan_distance(p, goal))
        visited.add(current)
        path.append(current)


    return path


# ============================================================
# Simple Tests
# ============================================================

def run_basic_tests():
    """
    These tests are provided only as simple examples.
    Passing them does not guarantee full credit.
    """

    # Problem 1: Basic Python Programming
    print("=" * 60)
    print("Problem 1")
    print(basic_statistics([3, 7, 2, 9, 4]))
    print("Expected: (25, 5.0, 9, 2)")

    # Problem 2: Conditional Statements
    print("=" * 60)
    print("Problem 2")
    print(get_grade(95), get_grade(82), get_grade(73))
    print("Expected: A B C")

    # Problem 3: Lists and Loops
    print("=" * 60)
    print("Problem 3")
    numbers = [3, 8, 1, 9, 4, 7, 2, 10]
    print(filter_numbers(numbers, 5))
    print("Expected: [8, 9, 7, 10]")
    print(count_even_odd(numbers))
    print("Expected: (4, 4)")

    # Problem 4: Dictionary
    print("=" * 60)
    print("Problem 4")
    values = {
        "A": 3.0,
        "B": 7.5,
        "C": 2.5,
        "D": 6.0
    }
    print(best_state(values))
    print("Expected: B")

    update_value(values, "A", 10.0)
    update_value(values, "E", 4.0)
    print(values)
    print("Expected: A=10.0 and E=4.0")

    # Problem 5: Functions and Distance
    print("=" * 60)
    print("Problem 5")
    print(manhattan_distance((2, 3), (7, 5)))
    print("Expected: 7")
    print(euclidean_distance((0, 0), (3, 4)))
    print("Expected: 5.0")

    # Problem 6: Introduction to Class (Point)
    print("=" * 60)
    print("Problem 6")
    try:
        p1 = Point(1, 2)
        p2 = Point(4, 6)
        print(p1.get_position())
        p1.move(2, 1)
        print(p1.get_position())
        print(p1.distance_to(p2))
        print("Expected approximately: (1,2), (3,3), 3.1623")
    except Exception as e:
        print("Point class not completed:", e)

    # Problem 7: Agent Class
    print("=" * 60)
    print("Problem 7")
    try:
        agent = Agent(0, 0)
        agent.move("DOWN")
        agent.move("DOWN")
        agent.move("RIGHT")
        print(agent.history)
        print("Expected: [(0, 0), (1, 0), (2, 0), (2, 1)]")
    except Exception as e:
        print("Agent class not completed:", e)

    # Problems 8-10: GridWorld, State Transition, and Valid Actions
    print("=" * 60)
    print("Problem 8-10")
    try:
        grid = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0]
        ]
        world = GridWorld(grid)

        # Problem 8: Build a GridWorld Class
        print(world.get_height(), world.get_width())
        print("Expected: 4 4")

        print(world.is_valid((0, 0)))
        print(world.is_valid((1, 1)))
        print(world.is_valid((10, 10)))
        print("Expected: True False False")

        # Problem 9: State Transition
        print(world.get_next_state((1, 0), "RIGHT"))
        print("Expected: (1, 0)")

        # Problem 10: Valid Actions
        print(world.get_valid_actions((0, 0)))
        print("Expected actions: DOWN and RIGHT")
    except Exception as e:
        print("GridWorld not completed:", e)

    # Problem 11: NumPy
    print("=" * 60)
    print("Problem 11")
    try:
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        print(vector_operations(a, b))
        print("Expected dot product: 32")
    except Exception as e:
        print("NumPy problem not completed:", e)

    # Problem 12: Mini Project — Robot in a GridWorld
    print("=" * 60)
    print("Problem 12")
    try:
        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0]
        ]

        world = GridWorld(grid)
        agent = Agent(0, 0)

        actions = [
            "RIGHT",
            "RIGHT",
            "RIGHT",
            "DOWN",
            "DOWN",
            "RIGHT",
            "DOWN",
            "DOWN"
        ]

        final_position = run_agent(world, agent, actions)

        print("Final position:", final_position)
        print("History:", agent.history)
        print("Reached (4, 4):", reached_goal(agent, (4, 4)))

    except Exception as e:
        print("Mini project not completed:", e)


if __name__ == "__main__":
    run_basic_tests()
