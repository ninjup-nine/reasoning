from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, TypeVar, Generic, Dict, Any
from heapq import heappush, heappop
import time
from typing import List, Tuple
import random
import copy

S = TypeVar('S')  # State type
A = TypeVar('A')  # Action type

@dataclass
class SearchNode(Generic[S, A]):
    state: S
    action: Optional[A]  # Action that led to this state (None for root)
    parent: Optional['SearchNode[S, A]']  # Parent node (None for root)
    path_cost: float  # Cost from start to this node
    depth: int  # Depth in the search tree
    count: int = 0  # Unique counter for tie-breaking

    def __lt__(self, other: 'SearchNode[S, A]') -> bool:
        # This is used by heapq for comparing nodes
        return self.count < other.count

    def get_path(self) -> List[A]:
        """Reconstruct path of actions from root to this node."""
        path = []
        current = self
        while current.parent is not None:
            path.append(current.action)
            current = current.parent
        return list(reversed(path))

class Problem(ABC, Generic[S, A]):
    """Abstract base class for defining search problems."""

    @abstractmethod
    def initial_state(self) -> S:
        """Return the initial state."""
        pass

    @abstractmethod
    def is_goal(self, state: S) -> bool:
        """Return True if state is a goal state."""
        pass

    @abstractmethod
    def actions(self, state: S) -> List[A]:
        """Return list of available actions in state."""
        pass

    @abstractmethod
    def result(self, state: S, action: A) -> S:
        """Return the state that results from taking action in state."""
        pass

    @abstractmethod
    def step_cost(self, state: S, action: A, next_state: S) -> float:
        """Return the cost of taking action in state to reach next_state."""
        pass

    def heuristic(self, state: S) -> float:
        """Estimate of cost from state to nearest goal. Default: optimistic 0."""
        return 0.0

class SearchAlgorithm(Generic[S, A]):
    """Base class for search algorithms."""

    def __init__(self, problem: Problem[S, A]):
        self.problem = problem
        self.nodes_generated = 0
        self.nodes_expanded = 0

    def solve(self,
             time_limit: Optional[float] = None,
             node_limit: Optional[int] = None) -> Dict[str, Any]:
        """
        Run search algorithm and return results dictionary containing:
        - 'success': Whether a solution was found
        - 'solution': List of actions if found, None otherwise
        - 'nodes_generated': Total nodes generated
        - 'nodes_expanded': Total nodes expanded
        - 'time': Time taken in seconds
        """
        start_time = time.time()

        initial_node = SearchNode(
            state=self.problem.initial_state(),
            action=None,
            parent=None,
            path_cost=0,
            depth=0
        )

        result = self._search(
            initial_node,
            start_time,
            time_limit,
            node_limit
        )

        end_time = time.time()

        return {
            'success': result is not None,
            'solution': result.get_path() if result else None,
            'nodes_generated': self.nodes_generated,
            'nodes_expanded': self.nodes_expanded,
            'time': end_time - start_time
        }

    @abstractmethod
    def _search(self,
                initial_node: SearchNode[S, A],
                start_time: float,
                time_limit: Optional[float],
                node_limit: Optional[int]) -> Optional[SearchNode[S, A]]:
        """Implementation of the actual search algorithm."""
        pass

class AStarSearch(SearchAlgorithm[S, A]):
    """A* search algorithm implementation."""

    def _search(self,
                initial_node: SearchNode[S, A],
                start_time: float,
                time_limit: Optional[float],
                node_limit: Optional[int]) -> Optional[SearchNode[S, A]]:

        # Add counter for unique node IDs
        node_counter = 0
        initial_node.count = node_counter

        frontier = []  # Priority queue
        heappush(frontier, (0, initial_node))  # Priority = f(n) = g(n) + h(n)

        explored = set()  # Set of explored states

        self.nodes_generated = 1
        self.nodes_expanded = 0

        while frontier:
            if time_limit and (time.time() - start_time) >= time_limit:
                return None
            if node_limit and self.nodes_generated >= node_limit:
                return None

            # Get node with lowest f-value
            f, node = heappop(frontier)

            if self.problem.is_goal(node.state):
                return node

            state_tuple = tuple(tuple(row) for row in node.state)
            if state_tuple not in explored:
                explored.add(state_tuple)
                self.nodes_expanded += 1

                for action in self.problem.actions(node.state):
                    next_state = self.problem.result(node.state, action)
                    next_state_tuple = tuple(tuple(row) for row in next_state)

                    if next_state_tuple not in explored:
                        step_cost = self.problem.step_cost(
                            node.state, action, next_state
                        )

                        node_counter += 1  # Increment counter for new node
                        child = SearchNode(
                            state=next_state,
                            action=action,
                            parent=node,
                            path_cost=node.path_cost + step_cost,
                            depth=node.depth + 1,
                            count=node_counter  # Assign unique counter
                        )

                        f = child.path_cost + self.problem.heuristic(next_state)
                        heappush(frontier, (f, child))
                        self.nodes_generated += 1

        return None  # No solution found

# Example Usage:
class SlidingPuzzle(Problem[List[List[int]], tuple[int, int, int, int]]):
    """
    8-puzzle problem implementation.
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

    def actions(self, state: List[List[int]]) -> List[tuple[int, int, int, int]]:
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
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_i, new_j = empty_pos[0] + di, empty_pos[1] + dj
            if 0 <= new_i < self.size and 0 <= new_j < self.size:
                moves.append((empty_pos[0], empty_pos[1], new_i, new_j))
        return moves

    def result(self, state: List[List[int]],
               action: tuple[int, int, int, int]) -> List[List[int]]:
        # Create new state and swap tiles
        new_state = [row[:] for row in state]
        r1, c1, r2, c2 = action
        new_state[r1][c1], new_state[r2][c2] = new_state[r2][c2], new_state[r1][c1]
        return new_state

    def step_cost(self, state: List[List[int]],
                 action: tuple[int, int, int, int],
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

class SlidingPuzzleGenerator:
    def __init__(self, size: int = 3):
        self.size = size
        self.goal_state = [
            [i * self.size + j for j in range(self.size)]
            for i in range(self.size)
        ]

    def generate(self, num_moves: int = 100) -> List[List[int]]:
        """Generate a random puzzle by walking backwards from goal state"""
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
        """Generate multiple unique puzzles"""
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
        """Find the empty tile (0) position"""
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 0:
                    return (i, j)
        raise ValueError("No empty tile found")

    def _get_valid_moves(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Get valid moves as (di, dj) tuples"""
        moves = []
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_i, new_j = pos[0] + di, pos[1] + dj
            if 0 <= new_i < self.size and 0 <= new_j < self.size:
                moves.append((di, dj))
        return moves

    def _make_move(self, state: List[List[int]], empty_pos: Tuple[int, int],
                   move: Tuple[int, int]) -> None:
        """Make a move by swapping tiles"""
        i, j = empty_pos
        di, dj = move
        state[i][j], state[i+di][j+dj] = state[i+di][j+dj], state[i][j]

    def is_solvable(self, state: List[List[int]]) -> bool:
        """
        Check if puzzle is solvable using inversion count.
        For n×n boards:
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
        """Pretty print a puzzle"""
        max_width = len(str(self.size * self.size - 1))
        for row in puzzle:
            print(' '.join(str(x).rjust(max_width) for x in row))

# Example usage:
if __name__ == "__main__":
    # Create a generator for 3x3 puzzles
    generator = SlidingPuzzleGenerator(3)

    # Generate a single puzzle
    puzzle = generator.generate(20)
    print("Generated 3x3 puzzle:")
    generator.print_puzzle(puzzle)
    print(f"Solvable: {generator.is_solvable(puzzle)}")

    # Solve the puzzle using A* search
    if generator.is_solvable(puzzle):
        problem = SlidingPuzzle(puzzle)
        solver = AStarSearch(problem)
        result = solver.solve(time_limit=30)  # 30 second time limit

        if result['success']:
            print("\nSolution found!")
            print(f"Steps: {len(result['solution'])}")
            print(f"Nodes generated: {result['nodes_generated']}")
            print(f"Nodes expanded: {result['nodes_expanded']}")
            print(f"Time taken: {result['time']:.2f} seconds")

            # Demonstrate the solution
            print("\nSolution sequence:")
            current_state = puzzle
            generator.print_puzzle(current_state)
            for action in result['solution']:
                print("\n↓ Move:", action)
                current_state = problem.result(current_state, action)
                generator.print_puzzle(current_state)
        else:
            print("\nNo solution found within time limit")
    else:
        print("\nPuzzle is not solvable")
