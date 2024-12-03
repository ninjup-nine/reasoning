# Background
## Current State of Reasoning Models
- Reasoning models are a frontier technology in LLM development.
- Operate using a different paradigm than traditional LLMs.
- Difference lies in test-time compute, where long chains of reasoning are generated to help answer complex queries.
- Requires many times more tokens to be generated than traditional LLMs.

- Currently frontier model is OpenAIs o1 model.
- Entirely closed-source, including the training code, model weights, and no technical report giving a high-level overview of the approach

- o1 was trained using by framing this as a tree-search problem
- The model generated lots of different reasoning paths, with some coming to the right answer to questions and some not
- Those reasoning paths that generated correct answers were rewarded, and those that did not were penalized.

## Open-source LLMs
- Open-source LLMs have empowered developers to build novel applications without relying on proprietary models.
- Open-source models are also more transparent, allowing for easier auditing and understanding of the model's capabilities and limitations.
- Open-source models are also more customizable, allowing developers to fine-tune the model to their specific needs.
- Open-source models are also more flexible, allowing for easier integration into existing systems and workflows.
- Open-source models are also more accessible, allowing for easier sharing and collaboration among developers.


## Tree-search methods
- Many methods exist for solving tree-search problems, including Monte Carlo Tree Search (MCTS), and AlphaZero
- Improving the methods we have to solve tree-search problems is key in developing better reasoning models.


# What does this project do?
- This subnet incentivises the creation of novel methods for solving tree-search problems.
- We create a framework for evaluating the performance of different tree-search methods using.

# Validators
- Validators are responsible for creating different configuraitons of common tree-search problems. Examples of these problems include n-puzzle, maze, towers of Hanoi,and d-chain problems.
- Validators take a set of parameters for a tree-search problem, and evaluate the performance of miners against the following criteria:
    - Highest score wins
    - Lowest runtime wins
    - Lowest memory usage wins

# Miners
- Miners are responsible for solving the tree-search problem using different tree-search methods.
- They submit their proposed solution to the validator, who then evaluates the solution against the criteria above.
- The validator then attests to the correctness of the solution, and the miner is rewarded.

# Installation

- Basic Installation Guide: Installation Guide
- For Miners: Miner Installation Guide
- For Validators: Validator Installation Guide



# Contribute

Refer to our Contribution Guidelines for detailed instructions on how to contribute to the Reasoning subnet. We welcome contributions from developers, miners, validators, and users who want to improve tree-search methods.

# License

Reasoning is licensed under the MIT License. Feel free to use, modify, and distribute our codebase for your projects. We appreciate any feedback, suggestions, and contributions to help us improve our solutions and make them more accessible to the community.
