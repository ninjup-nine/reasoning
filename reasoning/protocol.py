from typing import List, Tuple, Optional, Dict

import bittensor as bt


class ReasoningSynapse(bt.Synapse):
    """
    A Reasoning synapse protocol representation which uses bt.Synapse as its base.
    This protocol enables communication between the miner and the validator.

    Attributes:
    - problem: A list of lists of ints indicating the game board state.
    - solution: A list of actions  problem.
    """
    type: str
    # Initial problem state
    problem: List[List[int]]

    # Optional request output, filled by recieving axon.
    response: Optional[List[Tuple[int, int, int, int]]] = None

    def deserialize(self) -> Dict[str, List[List[int]]]:
        """
        Deserialize the miner response.

        Returns:
        - Dict[str, A]: The deserialized response, which is a list of actions to solve the problem.
        """
        return self.response
