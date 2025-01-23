import numpy as np
from typing import List, Tuple

import bittensor as bt

from reasoning.puzzle.verifier import SlidingPuzzleVerifier
from reasoning.puzzle.puzzle import SlidingPuzzle


def get_reward(puzzle: List[List[int]], solution: List[Tuple[int, int, int, int]] | None) -> float:
    """
    Reward the miner response based on the quality of their sliding puzzle solution.
    
    Args:
    - puzzle (List[List[int]]): The initial puzzle state
    - solution (List[Tuple[int, int, int, int]] | None): The sequence of moves provided by the miner
    
    Returns:
    - float: The reward value between 0 and 1
    """
    # Return 1.0 if puzzle is already solved
    if SlidingPuzzle(puzzle).is_goal(puzzle) and (solution is None or solution == []):
        bt.logging.debug(f"Puzzle already solved - returning 1.0 reward")
        return 1.0
    
    # Return 0 for invalid/None solutions
    if solution is None:
        bt.logging.debug(f"Solution was None - returning 0 reward")
        return 0.0
    
    # Verify the solution
    problem = SlidingPuzzle(puzzle)
    verifier = SlidingPuzzleVerifier(problem)
    is_valid = verifier.verify_solution(solution)
    
    if not is_valid:
        bt.logging.debug(f"Invalid solution - returning 0 reward")
        return 0.0
        
    # Calculate reward based on solution quality
    total_cost = verifier.calculate_solution_cost(solution)
    
    # Convert cost to reward using exponential decay: longer solutions get lower rewards
    reward = np.exp(-0.1 * total_cost)
    
    bt.logging.debug(f"Valid solution with cost {total_cost} - reward: {reward}")
    return float(reward)
