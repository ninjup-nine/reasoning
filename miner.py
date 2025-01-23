import os
import time
import argparse
import traceback
import bittensor as bt
from typing import Tuple

from reasoning.puzzle import SlidingPuzzle
from reasoning.search import AStarSearch

from protocol import ReasoningSynapse


class Miner:
    def __init__(self):
        self.config = self.get_config()
        self.setup_logging()
        self.setup_bittensor_objects()

    def get_config(self):
        # Set up the configuration parser
        parser = argparse.ArgumentParser()
        # TODO: Add your custom miner arguments to the parser.
        parser.add_argument(
            "--custom",
            default="my_custom_value",
            help="Adds a custom value to the parser.",
        )
        # Adds override arguments for network and netuid.
        parser.add_argument(
            "--netuid", type=int, default=1, help="The chain subnet uid."
        )
        # Adds subtensor specific arguments.
        bt.subtensor.add_args(parser)
        # Adds logging specific arguments.
        bt.logging.add_args(parser)
        # Adds wallet specific arguments.
        bt.wallet.add_args(parser)
        # Adds axon specific arguments.
        bt.axon.add_args(parser)
        # Parse the arguments.
        config = bt.config(parser)
        # Set up logging directory
        config.full_path = os.path.expanduser(
            "{}/{}/{}/netuid{}/{}".format(
                config.logging.logging_dir,
                config.wallet.name,
                config.wallet.hotkey_str,
                config.netuid,
                "miner",
            )
        )
        # Ensure the directory for logging exists.
        os.makedirs(config.full_path, exist_ok=True)
        return config

    def setup_logging(self):
        # Activate Bittensor's logging with the set configurations.
        bt.logging(config=self.config, logging_dir=self.config.full_path)
        bt.logging.info(
            f"Running miner for subnet: {self.config.netuid} on network: {self.config.subtensor.network} with config:"
        )
        bt.logging.info(self.config)

    def setup_bittensor_objects(self):
        # Initialize Bittensor miner objects
        bt.logging.info("Setting up Bittensor objects.")

        # Initialize wallet.
        self.wallet = bt.wallet(config=self.config)
        bt.logging.info(f"Wallet: {self.wallet}")

        # Initialize subtensor.
        self.subtensor = bt.subtensor(config=self.config)
        bt.logging.info(f"Subtensor: {self.subtensor}")

        # Initialize metagraph.
        self.metagraph = self.subtensor.metagraph(self.config.netuid)
        bt.logging.info(f"Metagraph: {self.metagraph}")

        if self.wallet.hotkey.ss58_address not in self.metagraph.hotkeys:
            bt.logging.error(
                f"\nYour miner: {self.wallet} is not registered to chain connection: {self.subtensor} \nRun 'btcli register' and try again."
            )
            exit()
        else:
            # Each miner gets a unique identity (UID) in the network.
            self.my_subnet_uid = self.metagraph.hotkeys.index(
                self.wallet.hotkey.ss58_address
            )
            bt.logging.info(f"Running miner on uid: {self.my_subnet_uid}")

    def blacklist_fn(self, synapse: ReasoningSynapse) -> Tuple[bool, str]:
        # Ignore requests from unrecognized entities.
        if synapse.dendrite.hotkey not in self.metagraph.hotkeys:
            bt.logging.trace(
                f"Blacklisting unrecognized hotkey {synapse.dendrite.hotkey}"
            )
            return True, None
        bt.logging.trace(
            f"Not blacklisting recognized hotkey {synapse.dendrite.hotkey}"
        )
        return False, None

    def forward(self, synapse: ReasoningSynapse) -> ReasoningSynapse:
        """
        Processes the incoming synapse by performing AStarSearch on the data.

        Args:
            synapse (ReasoningSynapse): The synapse object containing the starting state of the reasoning problem.

        Returns:
            ReasoningSynapse: The synapse object with a list of actions to solve the problem.
        """
        if synapse.type == "sliding_puzzle":
            problem = synapse.problem
            bt.logging.info(f"Received {synapse.type} problem from validator: {problem}")
            problem = SlidingPuzzle(problem)
            solver = AStarSearch(problem)
            result = solver.solve(time_limit=30)
            bt.logging.info(f"Result: {result}")
            if result['success']:
                bt.logging.info("Problem solved. Submitting solution to validator.")
                synapse.response = result['solution']
        return synapse

    def setup_axon(self):
        # Build and link miner functions to the axon.
        self.axon = bt.axon(wallet=self.wallet, config=self.config)

        # Attach functions to the axon.
        bt.logging.info("Attaching forward function to axon.")
        self.axon.attach(
            forward_fn=self.forward,
            blacklist_fn=self.blacklist_fn,
        )

        # Serve the axon.
        bt.logging.info(
            f"Serving axon on network: {self.config.subtensor.network} with netuid: {self.config.netuid}"
        )
        self.axon.serve(netuid=self.config.netuid, subtensor=self.subtensor)
        bt.logging.info(f"Axon: {self.axon}")

        # Start the axon server.
        bt.logging.info(f"Starting axon server on port: {self.config.axon.port}")
        self.axon.start()

    def run(self):
        self.setup_axon()

        # Keep the miner alive.
        bt.logging.info(f"Starting main loop")
        step = 0
        while True:
            try:
                # Periodically update our knowledge of the network graph.
                if step % 60 == 0:
                    self.metagraph.sync()
                    log = (
                        f"Block: {self.metagraph.block.item()} | "
                        f"Incentive: {self.metagraph.I[self.my_subnet_uid]} | "
                    )
                    bt.logging.info(log)
                step += 1
                time.sleep(1)

            except KeyboardInterrupt:
                self.axon.stop()
                bt.logging.success("Miner killed by keyboard interrupt.")
                break
            except Exception as e:
                bt.logging.error(traceback.format_exc())
                continue


# Run the miner.
if __name__ == "__main__":
    miner = Miner()
    miner.run()
