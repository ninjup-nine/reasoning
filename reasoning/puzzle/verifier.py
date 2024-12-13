
from typing import List, Tuple
from reasoning.search.problem import Verifier


class SlidingPuzzleVerifier(Verifier[List[List[int]], Tuple[int, int, int, int]]):
    """Verifies the correctness of sliding puzzle solutions."""

    def verify_solution(self, solution: List[Tuple[int, int, int, int]]) -> bool:
        """
        Verify if the solution is valid.
        Returns True if valid, False otherwise.
        """
        current_state = self.problem.initial_state()
        # Check each move in the solution
        for i, action in enumerate(solution):
            # Verify action format
            if not isinstance(action, tuple) or len(action) != 4:
                print(f"Invalid action format at step {i}: {action}")
                return False
            # Verify action is legal
            if action not in self.problem.actions(current_state):
                print(f"Illegal move at step {i}: {action}")
                return False
            # Apply the move
            current_state = self.problem.result(current_state, action)
        # Verify final state is goal state
        if not self.problem.is_goal(current_state):
            print("Final state is not the goal state.")
            return False
        return True

    def calculate_solution_cost(self, solution: List[Tuple[int, int, int, int]]) -> float:
        """Calculate the total cost of the solution."""
        total_cost = 0.0
        current_state = self.problem.initial_state()
        for action in solution:
            next_state = self.problem.result(current_state, action)
            total_cost += self.problem.step_cost(current_state, action, next_state)
            current_state = next_state
        return total_cost
