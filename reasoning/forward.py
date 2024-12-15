import random
import time
import bittensor as bt

from reasoning.protocol import ReasoningSynapse
from reasoning.puzzle.generator import SlidingPuzzleGenerator
from reasoning.reward import get_rewards
from reasoning.utils.uids import get_random_uids

PUZZLE_TYPES = ["sliding_puzzle"]


async def forward(self):
    """
    The forward function is called by the validator every time step.

    It is responsible for querying the network and scoring the responses.

    Args:
        self (:obj:`bittensor.neuron.Neuron`): The neuron object which contains all the necessary state for the validator.

    """
    # Get random UIDs to query
    miner_uids = get_random_uids(self, k=self.config.neuron.sample_size)
    
    puzzle_type = random.choice(PUZZLE_TYPES)

    if puzzle_type == "sliding_puzzle":
        # Generate the puzzle problem
        generator = SlidingPuzzleGenerator(3)
        puzzle = generator.generate()

        # Prepare the synapse object
        synapse = ReasoningSynapse(type="sliding_puzzle", problem=puzzle)

        # Query the network
        responses = self.dendrite.query(
            axons=[self.metagraph.axons[uid] for uid in miner_uids],
            synapse=synapse,
            deserialize=True,
        )

        bt.logging.info(f"Received responses: {responses}")

        # Score the responses
        rewards = get_rewards(self, query=puzzle, responses=responses)

        bt.logging.info(f"Scored responses: {rewards}")

        # Update the scores based on the rewards
        self.update_scores(rewards, miner_uids)
        time.sleep(5)
