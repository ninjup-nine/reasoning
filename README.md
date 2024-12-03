<a id="top"></a>

<h1 align="center">R E A S O N I N G</h1>

<img src="./static/banner.png" alt="Reasoning Banner" style='width: 100%; height: auto;'>

<p align="center"><i>A decentralized network for improving frontier AI reasoning models, built on Bittensor, the foremost decentralized AI network.</i></p>

![Version](https://img.shields.io/badge/Version-0.0.1-blue)
![Language](https://img.shields.io/badge/Language-Python-blue)
![License](https://img.shields.io/badge/License-MIT-blue)

![Last Commit](https://img.shields.io/github/last-commit/ninjup-nine/reasoning)
![Issues](https://img.shields.io/github/issues/ninjup-nine/reasoning)
![Contributors](https://img.shields.io/github/contributors/ninjup-nine/reasoning)

![Stars](https://img.shields.io/github/stars/ninjup-nine/reasoning?style=social)
![Forks](https://img.shields.io/github/forks/ninjup-nine/reasoning?style=social)

<hr>

> [!WARNING]
> The Reasoning subnet is under active development and may undergo breaking changes. Please join our [Discord](https://discord.gg/YourDiscordLink) to stay updated. If you encounter any bugs or wish to contribute, please refer to our [Contribution Guidelines](./CONTRIBUTING.md) for instructions.

## Our Philosophy 💡

At the Reasoning Subnet, we believe in pushing the boundaries of AI reasoning models through collaboration, innovation, and transparency. Our approach is rooted in these core principles:

### Collaboration 🤝

We foster a collaborative community where developers, miners, validators, and researchers can contribute and share ideas. Together, we aim to accelerate progress in AI reasoning capabilities.

### Innovation 🚀

We are committed to innovating and improving upon existing tree-search algorithms to enhance reasoning models. By incentivizing novel methods for solving tree-search problems, we encourage developers to explore new techniques and push the boundaries of what's possible.

### Transparency 🔍

We believe in the importance of open-source models and transparent methodologies. By providing access to our codebase, documentation, and research, we aim to empower others to understand, reproduce, and build upon our work, fostering trust and facilitating further advancements in AI.

<hr>

# Subnet Information

<details>
    <summary><h2>Table of Contents 📚</h2></summary>
    <ol style="list-style: none;">
        <li>
            <a href="#about" style="color: #3ecf8e;">About 🌐</a>
            <ul style="list-style: none; margin-left: 2px;">
                <li>
                    → <a href="#what-is-the-reasoning-subnet" style="color: #edb334;">What is the Reasoning Subnet? 🔍</a>
                </li>
                <li>
                    → <a href="#background" style="color: #edb334;">Background 🧠</a>
                </li>
                <li>
                    → <a href="#the-role-of-open-source-llms" style="color: #edb334;">The Role of Open-Source LLMs 🔓</a>
                </li>
                <li>
                    → <a href="#importance-of-tree-search-methods" style="color: #edb334;">Importance of Tree-Search Methods 🌳</a>
                </li>
            </ul>
        </li>
        <li>
            <a href="#validators" style="color: #3ecf8e;">Validators 🛡️</a>
        </li>
        <li>
            <a href="#miners" style="color: #3ecf8e;">Miners ⛏️</a>
        </li>
        <li>
            <a href="#installation" style="color: #3ecf8e;">Installation 🛠️</a>
            <ul style="list-style: none; margin-left: 2px;">
                <li>
                    → <a href="#basic-installation-guide" style="color: #edb334;">Basic Installation Guide 📘</a>
                </li>
                <li>
                    → <a href="#for-miners" style="color: #edb334;">For Miners ⛏️</a>
                </li>
                <li>
                    → <a href="#for-validators" style="color: #edb334;">For Validators 🛡️</a>
                </li>
            </ul>
        </li>
        <li>
            <a href="#contribute" style="color: #3ecf8e;">Contribute 🤝</a>
        </li>
        <li>
            <a href="#license" style="color: #3ecf8e;">License 📜</a>
        </li>
        <li>
            <a href="#contact" style="color: #3ecf8e;">Contact 📞</a>
        </li>
    </ol>
</details>

<a id="about"></a>

## About 🌐

<a id="what-is-the-reasoning-subnet"></a>

### What is the Reasoning Subnet? 🔍

The Reasoning subnet aims to improve the capabilities of frontier AI reasoning models. It does this by incentivizing the creation of novel methods for solving tree-search problems. By providing a framework for evaluating the performance of different tree-search algorithms, we encourage developers to innovate and improve upon existing techniques.

<a id="background"></a>

### Background 🧠

Reasoning models represent a cutting-edge frontier in the development of Large Language Models (LLMs). Unlike traditional LLMs that primarily focus on predicting the next word in a sequence based on learned language patterns, reasoning models are designed to simulate complex cognitive processes. They operate by generating long chains of reasoning to solve intricate queries, effectively mimicking human problem-solving techniques.

One of the key distinctions between reasoning models and traditional LLMs lies in their computational paradigms during inference, also known as test-time compute. Reasoning models require the generation of extensive reasoning paths, which means they produce significantly more tokens than traditional models. This approach allows them to explore multiple potential solutions before arriving at an answer, enabling them to tackle more complex tasks that involve logic, deduction, and multi-step problem-solving.

Organizations like OpenAI are at the forefront of developing advanced reasoning models. While specifics about these models may not be publicly disclosed due to proprietary constraints, it is understood that they employ sophisticated techniques such as framing problem-solving as tree-search problems. In this context, the model generates numerous reasoning paths; some lead to correct answers, while others do not. Through reinforcement learning mechanisms, reasoning paths that yield correct answers are rewarded, and those that do not are penalized. This training process refines the model's ability to select more effective reasoning strategies over time.

The closed-source nature of these advanced models, including the lack of access to training code, model weights, and detailed technical reports, presents challenges for the broader AI community. Without transparency, it becomes difficult for researchers and developers to understand the underlying methodologies, reproduce results, or build upon these innovations.

<a id="the-role-of-open-source-llms"></a>

### The Role of Open-Source LLMs 🔓

Open-source LLMs have significantly empowered developers and researchers by providing access to sophisticated language models without relying on proprietary platforms. These models encourage innovation by allowing users to build novel applications tailored to specific needs, ranging from natural language processing tasks to specialized domain applications.

Transparency is a hallmark of open-source models. The ability to inspect and understand the model's architecture, training data, and methodologies allows for thorough auditing and enhances trust in the model's outputs. This scrutiny helps identify biases, limitations, and potential areas for improvement, leading to more robust and reliable AI systems.

Customization is another advantage offered by open-source LLMs. Developers can fine-tune models on domain-specific datasets to improve performance in targeted applications. This flexibility facilitates better integration into existing systems and workflows, as the models can be adapted to meet particular requirements.

Accessibility is a key benefit, as open-source models foster a collaborative environment where developers can share knowledge, tools, and improvements. This collaborative spirit accelerates development cycles and promotes the democratization of AI technology, ensuring that advancements are not limited to organizations with extensive resources.

<a id="importance-of-tree-search-methods"></a>

### Importance of Tree-Search Methods 🌳

Tree-search methods are fundamental algorithms used to solve complex decision-making problems, and they play a crucial role in enhancing reasoning models. Techniques such as Monte Carlo Tree Search (MCTS) and algorithms inspired by AlphaZero have been instrumental in advancing artificial intelligence, particularly in strategic game playing and problem-solving domains.

MCTS is a heuristic search algorithm that uses randomness and statistical sampling to make decisions in complex spaces. It balances exploration of new paths with exploitation of known successful paths, making it effective for navigating large and complicated search trees. AlphaZero's approach, which combines deep learning with tree search, has demonstrated unprecedented success in mastering games like chess and Go without prior human knowledge.

Improving tree-search methods is essential for developing better reasoning models. Enhancements in these algorithms enable more efficient exploration of possible reasoning paths, reduce computational overhead, and increase the accuracy of the models' outputs. By optimizing how tree-search algorithms handle exploration, evaluation, and backpropagation of rewards, researchers can create reasoning models that are more capable of solving complex tasks.

<a id="validators"></a>

## Validators 🛡️

Validators play a critical role in this ecosystem. They are responsible for creating diverse configurations of common tree-search problems, including examples like the n-puzzle, maze navigation, Towers of Hanoi, and d-chain problems. Validators evaluate the performance of submitted solutions from miners against defined criteria:

- **Highest Score Wins**: Solutions are ranked based on the score achieved in solving the problem.
- **Lowest Runtime Wins**: Efficiency is rewarded by assessing how quickly a solution arrives at the correct answer.
- **Lowest Memory Usage Wins**: Optimizing memory usage is essential for scalability and performance.

<a id="miners"></a>

## Miners ⛏️

Miners are tasked with developing and implementing tree-search algorithms to solve the problems provided by validators. They apply different methods and strategies in their solutions, aiming to optimize performance based on the evaluation criteria. Upon submitting their solutions, validators assess their effectiveness, correctness, and resource utilization. Successful miners are rewarded, incentivizing continual improvement and innovation in tree-search methodologies.

<a id="installation"></a>

## Installation 🛠️

Here at the Reasoning Subnet, we strive to make the installation process as seamless as possible, regardless of your technical background. We have crafted step-by-step guides and tutorials to get you started:

<a id="basic-installation-guide"></a>

- **Basic Installation Guide**: Refer to the [Installation Guide](https://github.com/ninjup-nine/reasoning/blob/main/docs/basic_installation.md) for general setup instructions.

<a id="for-miners"></a>

- **For Miners**: Follow the [Miner Installation Guide](https://github.com/ninjup-nine/reasoning/blob/main/docs/miner.md) to set up your mining environment and start contributing solutions.

<a id="for-validators"></a>

- **For Validators**: The [Validator Installation Guide](https://github.com/ninjup-nine/reasoning/blob/main/docs/validator.md) provides detailed steps to configure and manage validation tasks.

<a id="contribute"></a>

## Contribute 🤝

We welcome contributions from developers, miners, validators, and users who are interested in improving tree-search methods. Refer to our [Contribution Guidelines](./CONTRIBUTING.md) for detailed instructions on how to participate in the project. Collaboration and collective effort are key to advancing the capabilities of reasoning models and AI technology as a whole.

<a id="license"></a>

## License 📜

The Reasoning subnet is licensed under the [MIT License](./LICENSE.md). Feel free to use, modify, and distribute our codebase for your projects. We appreciate any feedback, suggestions, and contributions to help us improve our solutions and make them more accessible to the community.

<a id="contact"></a>

## Contact 📞

For any inquiries, please reach out to us via:

- **Github**: Leave an issue on [Github](https://github.com/ninjup-nine/reasoning/issues)

<hr>

<pre align="center">
     ___          ___          ___          ___       ___                              ___     
    /\  \        /\  \        /\  \        /\  \     /\  \                            /\  \    
   /::\  \      /::\  \      /::\  \      /::\  \    \:\  \       ___          ___    \:\  \   
  /:/\:\  \    /:/\:\  \    /:/\:\  \    /:/\:\  \    \:\  \     /\__\        /\__\    \:\  \  
 /::\~\:\  \  /::\~\:\  \  /::\~\:\__\  /:/  \:\  \   /::\  \   /:/__/       /:/__/    /::\  \ 
/:/\:\ \:\__\/:/\:\ \:\__\/:/\:\ \:|__|/:/__/ \:\__\ /:/\:\__\ /::\  \      /::\  \   /:/\:\__\
\/_|::\/:/  /\/_|::\/:/  /\/_|:\ \:\/:/\:\  \  \/__/ \:\/:/  / \/\:\  \__  /:/\:\  \ /:/  \/__/
   |:|::/  /    |:|::/  /    |:|:\::/  \:\  \         \::/  /     \:\/\__\/:/  \:\  /:/  /     
   |:|\/__/     |:|\/__/     |:|::/    \:\  \         /:/  /       \::/  /:/__/ \:\/:/  /      
   |:|  |       |:|  |       |:|\/__    \:\__\       /:/  /         \/__/ \:\  \  \::/__/       
    \|__|        \|__|        \|__|       \/__/       \/__/                  \:\__\  \/\__\      
                                                                            \/__/   \/__/      
</pre>

[Back to Top](#top)