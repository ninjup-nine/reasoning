from typing import List, Tuple, Optional, Union

import bittensor as bt


class ReasoningSynapse(bt.Synapse):
    """
    A Reasoning synapse protocol representation which uses bt.Synapse as its base.
    This protocol enables communication between the miner and the validator.

    Attributes:
    - problem: A list of lists of ints indicating the game board state.
    - solution: List[Tuple[int, int, int, int]] containing a list of actions for the problem.
    """
    # Sliding puzzle problem
    problem: List[List[int]]

    # Optional request output, filled by recieving axon.
    response: Optional[List[Tuple[int, int, int, int]]] = None

    def deserialize(self) -> List[Tuple[int, int, int, int]]:
        """
        Deserialize the miner response.

        Returns:
        - List[Tuple[int]]: The deserialized response, which is a list of tuples, which describe the movement of a piece.
        """
        return self.response
