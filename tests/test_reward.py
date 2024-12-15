import pytest
import numpy as np
from reasoning.reward import reward, get_rewards
from typing import List, Tuple

class TestReward:
    # Test fixtures
    @pytest.fixture
    def solved_puzzle(self):
        return [
            [1, 2],
            [3, 0]
        ]

    @pytest.fixture
    def unsolved_puzzle(self):
        return [
            [0, 2],
            [3, 1]
        ]

    def test_reward_none_solution(self, solved_puzzle):
        """
        Test that None solution returns 0 reward.
        This represents an invalid or failed solution attempt.
        """
        assert reward(solved_puzzle, None) == 0.0

    def test_reward_empty_solution(self, solved_puzzle):
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

    def test_reward_valid_cycle(self, solved_puzzle):
        """
        Test reward for valid but unnecessary moves.
        Cycles should receive positive but suboptimal rewards.
        """
        cycle_solution = [
            (1, 1, 1, 0),  # Move 3 right
            (1, 0, 1, 1),  # Move 3 left
        ]
        result = reward(solved_puzzle, cycle_solution)
        assert 0 < result < 1.0

    def test_get_rewards(self, solved_puzzle):
        """
        Test get_rewards function with multiple solutions.
        Verifies correct handling of various solution types.
        """
        solutions = [
            [],  # Perfect solution
            [(1, 1, 1, 0), (1, 0, 1, 1)],  # Valid but suboptimal
            None,  # Invalid solution
            [(0, 0, 0, 1)]  # Valid single move
        ]
        rewards = get_rewards(None, solved_puzzle, solutions)
        
        assert len(rewards) == len(solutions)
        assert rewards[0] == 1.0  # Perfect solution
        assert 0 < rewards[1] < 1.0  # Suboptimal solution
        assert rewards[2] == 0.0  # Invalid solution
        assert 0 < rewards[3] < rewards[0]  # Valid but unnecessary move

    def test_reward_decreases_with_length(self, solved_puzzle):
        """
        Test that longer solutions get lower rewards.
        Verifies that solution efficiency is factored into reward.
        """
        short_solution = [(1, 1, 1, 0)]
        long_solution = [(1, 1, 1, 0)] * 5  # Same move repeated 5 times
        
        short_reward = reward(solved_puzzle, short_solution)
        long_reward = reward(solved_puzzle, long_solution)
        
        assert short_reward > long_reward
        assert 0 < long_reward < short_reward < 1.0

    def test_reward_edge_cases(self, solved_puzzle):
        """
        Test edge cases and boundary conditions.
        """
        # Empty puzzle
        with pytest.raises(ValueError):
            reward([], [])
        
        # None puzzle
        with pytest.raises(ValueError):
            reward(None, [])
        
        # Very long solution
        very_long = [(1, 1, 1, 0)] * 1000
        assert 0 <= reward(solved_puzzle, very_long) < 0.1
