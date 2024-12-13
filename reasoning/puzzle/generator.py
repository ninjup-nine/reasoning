
from typing import List, Tuple
import random
import copy

class SlidingPuzzleGenerator:
    """Generates a random sliding puzzle."""

    def __init__(self, size: int = 3):
        self.size = size
        self.goal_state = [
            [i * self.size + j for j in range(self.size)]
            for i in range(self.size)
        ]

    def generate(self, num_moves: int = 100) -> List[List[int]]:
        """Generate a random puzzle by walking backwards from goal state."""
        current = copy.deepcopy(self.goal_state)
        prev_move = None  # Track previous move to avoid undoing it
        for _ in range(num_moves):
            # Get valid moves
            empty_pos = self._find_empty(current)
            moves = self._get_valid_moves(empty_pos)
            # Remove the reverse of the previous move to avoid undoing it
            if prev_move:
                reverse_move = (-prev_move[0], -prev_move[1])
                if reverse_move in moves:
                    moves.remove(reverse_move)
            # Make random move
            if moves:
                move = random.choice(moves)
                self._make_move(current, empty_pos, move)
                prev_move = move
        return current

    def generate_multiple(self, count: int, min_moves: int = 10,
                          max_moves: int = 100) -> List[List[List[int]]]:
        """Generate multiple unique puzzles."""
        puzzles = []
        seen = set()
        while len(puzzles) < count:
            moves = random.randint(min_moves, max_moves)
            puzzle = self.generate(moves)
            puzzle_tuple = tuple(tuple(row) for row in puzzle)
            if puzzle_tuple not in seen and self.is_solvable(puzzle):
                puzzles.append(puzzle)
                seen.add(puzzle_tuple)
        return puzzles

    def _find_empty(self, state: List[List[int]]) -> Tuple[int, int]:
        """Find the empty tile (0) position."""
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 0:
                    return (i, j)
        raise ValueError("No empty tile found")

    def _get_valid_moves(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Get valid moves as (di, dj) tuples."""
        moves = []
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_i, new_j = pos[0] + di, pos[1] + dj
            if 0 <= new_i < self.size and 0 <= new_j < self.size:
                moves.append((di, dj))
        return moves

    def _make_move(self, state: List[List[int]], empty_pos: Tuple[int, int],
                   move: Tuple[int, int]) -> None:
        """Make a move by swapping tiles."""
        i, j = empty_pos
        di, dj = move
        state[i][j], state[i+di][j+dj] = state[i+di][j+dj], state[i][j]

    def is_solvable(self, state: List[List[int]]) -> bool:
        """
        Check if puzzle is solvable using inversion count.
        For nxn boards:
        - If n is odd, puzzle is solvable if inversion count is even
        - If n is even, puzzle is solvable if:
          * blank on even row from bottom + odd inversions, or
          * blank on odd row from bottom + even inversions
        """
        # Flatten the puzzle and remove empty tile
        flat = [num for row in state for num in row if num != 0]
        # Count inversions
        inversions = 0
        for i in range(len(flat)):
            for j in range(i + 1, len(flat)):
                if flat[i] > flat[j]:
                    inversions += 1
        # Find empty tile row from bottom
        empty_row = self.size - (self._find_empty(state)[0] + 1)
        # Apply solvability rules
        if self.size % 2 == 1:
            return inversions % 2 == 0
        else:
            if empty_row % 2 == 0:
                return inversions % 2 == 1
            else:
                return inversions % 2 == 0

    def print_puzzle(self, puzzle: List[List[int]]) -> None:
        """Pretty print a puzzle."""
        max_width = len(str(self.size * self.size - 1))
        for row in puzzle:
            print(' '.join(str(x).rjust(max_width) for x in row))
