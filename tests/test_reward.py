import pytest
import numpy as np
from reasoning.reward import reward, get_rewards

class TestReward:
    # Test fixtures
    @pytest.fixture
    def solved_puzzle(self):
        return [
            [0, 1],
            [2, 3]
        ]

    @pytest.fixture
    def unsolved_puzzle(self):
        return [
            [0, 2],
            [3, 1]
        ]

    def test_none_solution_completed_puzzle(self, solved_puzzle):
        """
        Test that None solution returns 1.0 reward on already solved puzzle.
        """
        assert reward(solved_puzzle, None) == 1.0

    def test_empty_solution_completed_puzzle(self, solved_puzzle):
        """
        Test reward for empty solution on solved puzzle.
        Empty solution is optimal when puzzle is already solved.
        """
        assert reward(solved_puzzle, []) == 1.0

    def test_reward_invalid_move(self, solved_puzzle):
        """
        Test that invalid moves return 0 reward.
        Invalid moves include moving non-adjacent tiles or illegal movements.
        """
        invalid_moves = [
            [(0, 0, 1, 0)],  # Moving non-adjacent tile
            [(2, 2, 1, 1)],  # Out of bounds
            [(-1, 0, 0, 0)], # Negative indices
        ]
        for move in invalid_moves:
            assert reward(solved_puzzle, move) == 0.0

    def test_none_solution_incomplete_puzzle(self, unsolved_puzzle):
        """
        Test that None solution returns 0.0 reward on unsolved puzzle.
        No solution means no attempt to solve, which should be penalized.
        """
        assert reward(unsolved_puzzle, None) == 0.0

    def test_empty_solution_incomplete_puzzle(self, unsolved_puzzle):
        """
        Test reward for empty solution on unsolved puzzle.
        Empty solution is suboptimal when puzzle needs solving.
        """
        assert reward(unsolved_puzzle, []) == 0.0

    def test_nonsense_response(self, unsolved_puzzle):
        """
        Test reward for nonsense response.
        """
        assert reward(unsolved_puzzle, "nonsense") == 0.0
