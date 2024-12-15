<a id="top"></a>

<h1 align="center">R E A S O N I N G</h1>

<p align="center"><i>A subnet for improving AI reasoning algorithms.</i></p>

![Version](https://img.shields.io/badge/Version-0.0.1-blue)
![Language](https://img.shields.io/badge/Language-Python-blue)
![License](https://img.shields.io/badge/License-MIT-blue)

![Last Commit](https://img.shields.io/github/last-commit/ninjup-nine/reasoning)
![Issues](https://img.shields.io/github/issues/ninjup-nine/reasoning)
![Contributors](https://img.shields.io/github/contributors/ninjup-nine/reasoning)

<hr>

> [!WARNING]
> The Reasoning subnet is under active development and may undergo breaking changes. Please join our [Discord](https://discord.gg/YourDiscordLink) to stay updated. If you encounter any bugs or wish to contribute, please refer to our [Contribution Guidelines](./CONTRIBUTING.md) for instructions.

## Background

Reasoning models mark a cutting-edge advancement in the domain of Large Language Models (LLMs). They differ from previous generations (such as GPT-4), by simulating complex cognitive processes. Their inference approach, involving generating extensive reasoning paths, allows them to tackle tasks requiring logic and multi-step problem-solving. Organizations like OpenAI lead advancements using tree-search methods that reward effective reasoning paths. Nonetheless, the proprietary nature of these systems restricts broader research and development efforts, limiting community engagement.

Conversely, open-source LLMs empower developers and researchers with accessible language models for diverse applications. These models' transparency allows thorough auditing, fosters customization for domain-specific needs, and promotes collaboration. Tree-search methods, like Monte Carlo Tree Search (MCTS) and AlphaZero-inspired algorithms, play a pivotal role in advancing reasoning models. Refined tree-search algorithms enhance exploration, reduce computational demands, and improve accuracy, making reasoning models more adept at solving complex tasks. Open-source frameworks thus drive democratization and continued innovation in AI technology.

## Validators

Validators play a critical role in this ecosystem. They are responsible for creating diverse configurations of common tree-search problems, including examples like sliding-puzzles, maze navigation, Towers of Hanoi, and d-chain problems. Validators evaluate the performance of submitted solutions from miners against defined criteria:

## Miners

Miners are tasked with developing and implementing tree-search algorithms to solve the problems provided by validators. They can apply different methods and strategies in their solutions. Our evaluation criteria are continually evolving, but currently we reward miners for proposing solutions that reach a correct answer in the fewest number of steps.

## Installation

Following is how to run a miner or validator:

- **Basic Installation Guide**: Refer to the [Installation Guide](https://github.com/ninjup-nine/reasoning/blob/main/docs/basic_installation.md) for general setup instructions.

- **For Miners**: Follow the [Miner Installation Guide](https://github.com/ninjup-nine/reasoning/blob/main/docs/miner.md) to set up your mining environment and start contributing solutions.

- **For Validators**: The [Validator Installation Guide](https://github.com/ninjup-nine/reasoning/blob/main/docs/validator.md) provides detailed steps to configure and manage validation tasks.

## Contribute

We welcome contributions from developers, miners, validators, and users who are interested in improving tree-search methods. Refer to our [Contribution Guidelines](./CONTRIBUTING.md) for detailed instructions on how to participate in the project. Collaboration and collective effort are key to advancing the capabilities of reasoning models and AI technology as a whole.

## License

The Reasoning subnet is licensed under the [MIT License](./LICENSE.md). Feel free to use, modify, and distribute our codebase for your projects. We appreciate any feedback, suggestions, and contributions to help us improve our solutions and make them more accessible to the community.

## Contact

For any inquiries, reach out to us via:

- **Github**: Leave an issue on [Github](https://github.com/ninjup-nine/reasoning/issues)
- **Discord**: Join our [Discord](https://discord.gg/2uXqxgs4)
- **Email**: [hello@reasoning.sh](mailto:ninjup.nine@gmail.com)

<hr>

<pre align="center">
     ___          ___     
    /\  \        /\  \    
   /::\  \      /::\  \   
  /:/\:\  \    /:/\:\  \  
 /::\~\:\  \  /::\~\:\  \ 
/:/\:\ \:\__\/:/\:\ \:\__\
\/_|::\/:/  /\/_|::\/:/  /
   |:|::/  /    |:|::/  /   
   |:|\/__/     |:|\/__/   
   |:|  |       |:|  |        
    \|__|        \|__|
</pre>

[Back to Top](#top)