
from typing import List, Tuple
from reasoning.search.problem import Problem

class SlidingPuzzle(Problem[List[List[int]], Tuple[int, int, int, int]]):
    """
    Sliding puzzle problem implementation.
    State: 2D list representing tile positions (0 = empty)
    Action: tuple(row1, col1, row2, col2) representing tile swap
    """

    def __init__(self, initial: List[List[int]]):
        self.initial = initial
        self.size = len(initial)

    def initial_state(self) -> List[List[int]]:
        return [row[:] for row in self.initial]

    def is_goal(self, state: List[List[int]]) -> bool:
        # Check if tiles are in order
        n = 0
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] != n:
                    return False
                n = (n + 1) % (self.size * self.size)
        return True

    def actions(self, state: List[List[int]]) -> List[Tuple[int, int, int, int]]:
        # Find empty tile (0)
        empty_pos = None
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 0:
                    empty_pos = (i, j)
                    break
            if empty_pos:
                break
        # Generate possible moves (up, down, left, right)
        moves = []
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_i, new_j = empty_pos[0] + di, empty_pos[1] + dj
            if 0 <= new_i < self.size and 0 <= new_j < self.size:
                moves.append((empty_pos[0], empty_pos[1], new_i, new_j))
        return moves

    def result(self, state: List[List[int]],
               action: Tuple[int, int, int, int]) -> List[List[int]]:
        # Create new state and swap tiles
        new_state = [row[:] for row in state]
        r1, c1, r2, c2 = action
        new_state[r1][c1], new_state[r2][c2] = new_state[r2][c2], new_state[r1][c1]
        return new_state

    def step_cost(self, state: List[List[int]],
                  action: Tuple[int, int, int, int],
                  next_state: List[List[int]]) -> float:
        return 1.0

    def heuristic(self, state: List[List[int]]) -> float:
        # Manhattan distance heuristic
        distance = 0
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] != 0:  # Skip empty tile
                    goal_i = state[i][j] // self.size
                    goal_j = state[i][j] % self.size
                    distance += abs(goal_i - i) + abs(goal_j - j)
        return float(distance)
