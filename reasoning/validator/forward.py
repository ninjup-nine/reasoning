import time
import bittensor as bt

from reasoning.protocol import ReasoningSynapse
from reasoning.validator.search import SlidingPuzzleGenerator
from reasoning.validator.reward import get_rewards
from reasoning.utils.uids import get_random_uids


async def forward(self):
    """
    The forward function is called by the validator every time step.

    It is responsible for querying the network and scoring the responses.

    Args:
        self (:obj:`bittensor.neuron.Neuron`): The neuron object which contains all the necessary state for the validator.

    """
    # Get random UIDs to query
    miner_uids = get_random_uids(self, k=self.config.neuron.sample_size)

    # Generate the puzzle problem
    generator = SlidingPuzzleGenerator()
    puzzle = generator.generate()

    # Prepare the synapse object
    synapse = ReasoningSynapse(problem=puzzle)
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
