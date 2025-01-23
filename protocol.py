from typing import List, Optional, Tuple, Dict

import bittensor as bt


class ReasoningSynapse(bt.Synapse):
    """
    A Reasoning synapse protocol representation which uses bt.Synapse as its base.
    This protocol enables communication between the miner and the validator.

    Attributes:
    - problem: A list of lists of ints indicating the game board state.
    - solution: A list of actions  problem.
    """
    # Filled by validator
    type: str
    problem: List[List[int]] # Update this when adding more problem types

    # Filled by miner
    solution: Optional[List[Tuple[int, int, int, int]]] = None # Update this when adding more problem types
