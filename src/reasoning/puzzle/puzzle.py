from typing import List, Tuple
from reasoning.search.problem import Problem
import copy

class SlidingPuzzle(Problem[List[List[int]], Tuple[int, int, int, int]]):
    """
    Sliding puzzle problem implementation.
    State: 2D list representing tile positions (0 = empty)
    Action: tuple(row1, col1, row2, col2) representing tile swap
    """

    def __init__(self, initial: List[List[int]]):
        # Validate puzzle is square and contains valid numbers
        size = len(initial)
        if not all(len(row) == size for row in initial):
            raise IndexError("Puzzle must be square")
            
        # Check for valid numbers (0 to size^2-1, each appearing once)
        flat = [num for row in initial for num in row]
        if sorted(flat) != list(range(size * size)):
            raise AssertionError("Invalid puzzle state: must contain numbers 0 to size^2-1 exactly once")
            
        # Deep copy the initial state
        self.initial = copy.deepcopy(initial)
        self.size = size

    def initial_state(self) -> List[List[int]]:
        return copy.deepcopy(self.initial)

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

    def result(self, state: List[List[int]], action: Tuple[int, int, int, int]) -> List[List[int]]:
        """
        Returns the new state after applying the action.
        Action is (row1, col1, row2, col2) representing swapping tiles at these positions.
        """
        # Create new state with deep copy
        new_state = copy.deepcopy(state)
        r1, c1, r2, c2 = action
        # Swap tiles
        new_state[r1][c1], new_state[r2][c2] = new_state[r2][c2], new_state[r1][c1]
        return new_state

    def step_cost(self, state: List[List[int]],
                  action: Tuple[int, int, int, int],
                  next_state: List[List[int]]) -> float:
        return 1.0

    def heuristic(self, state: List[List[int]]) -> float:
        """
        Manhattan distance heuristic - calculates distance of empty tile (0) 
        from its goal position at (0,0)
        """
        # Find empty tile position
        empty_pos = None
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 0:
                    empty_pos = (i, j)
                    break
            if empty_pos:
                break
            
        # Calculate Manhattan distance from empty tile to (0,0)
        distance = abs(empty_pos[0] - 0) + abs(empty_pos[1] - 0)
        return float(distance)
