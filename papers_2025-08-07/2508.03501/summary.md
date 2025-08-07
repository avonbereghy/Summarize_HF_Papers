# Training Long-Context, Multi-Turn Software Engineering Agents with
  Reinforcement Learning

**Paper ID:** 2508.03501

**Authors:** Alexander Golubev, Maria Trofimova, Sergei Polezhaev, Ibragim Badertdinov, Maksim Nekrashevich, Anton Shevtsov, Simon Karasik, Sergey Abramov, Andrei Andriushchenko, Filipp Fisin, Sergei Skvortsov, Boris Yangel

**URL:** https://huggingface.co/papers/2508.03501

## Summary

## Executive Summary

This paper presents a novel approach to training **long-context, multi-turn software engineering agents** using *Reinforcement Learning (RL)*.  Unlike previous RL applications to Large Language Models (LLMs) which focused on single-turn problems, this work tackles the complexities of real-world software engineering tasks requiring rich, stateful interactions.  By employing a modified *Decoupled Advantage Policy Optimization (DAPO)* algorithm and training an agent on the *Qwen2.5-72B-Instruct* LLM, the researchers achieved a significant improvement in success rate on the *SWE-bench Verified* benchmark, surpassing a fine-tuned baseline and matching/exceeding the performance of leading open-weight models like *DeepSeek-V3-0324* and *Qwen3-235B-A22B* on *SWE-rebench*. This demonstrates a viable path towards creating more capable autonomous agents for complex real-world problems using open-source models.


## Key Contributions and Findings

* **Successful Application of RL to Long-Context, Multi-Turn Problems:** The paper successfully applies *Reinforcement Learning* to a challenging domain (software engineering) that demands extended, interactive engagement with a stateful environment, unlike simpler single-turn tasks.  This expands the capabilities of RL-trained LLMs.

* **Significant Performance Improvement on SWE Benchmarks:** The trained agent achieved a *39%* success rate on the *SWE-bench Verified* benchmark, a substantial increase from the *20%* baseline.  On *SWE-rebench*, it matched or exceeded the performance of leading open-weight models.

* **Teacher-Free Training:** The improved performance was achieved *without* relying on any teacher models, showcasing the potential of RL for autonomous agent development.

* **Utilizing a Modified DAPO Algorithm:**  The study successfully adapted the *DAPO algorithm* for effective training in the complex multi-turn software engineering environment.

* **Demonstrates Viability of Open-Source Model-Based Agents:** The results highlight the potential of building high-performing agents for complex tasks using readily available *open-source LLMs* like *Qwen2.5-72B-Instruct*.


## Methodology Overview

The research employed a *modified Decoupled Advantage Policy Optimization (DAPO) algorithm* to train a software engineering agent. The agent, based on the *Qwen2.5-72B-Instruct LLM*, interacted with a stateful environment representing real-world software engineering tasks.  The *DAPO algorithm* optimized the agent's policy to maximize its success rate in completing these tasks. The training process involved *reward signals* based on the successful completion of tasks within the environment.


## Results and Performance

The trained agent achieved a *39%* success rate on the *SWE-bench Verified* benchmark, significantly improving upon the *20%* baseline.  On the *SWE-rebench* benchmark, the agent's performance *matched or exceeded* that of leading open-weight models like *DeepSeek-V3-0324* and *Qwen3-235B-A22B*, using an identical scaffolding.


## Limitations and Future Work

While the results are promising, the study acknowledges the need for further research.  Limitations might include the specific benchmarks used and the generalizability of the approach to other software engineering tasks and domains. Future work could explore scaling to larger models, investigating different RL algorithms, and expanding the scope of the tasks considered.  Further investigation into the robustness and generalization capabilities of the trained agent is also warranted.


## Practical Applications

This research has significant implications for the development of **autonomous software engineering tools**.  The trained agent could assist developers with various tasks, such as *code generation, debugging, and testing*.  This could lead to increased efficiency and productivity in software development, potentially reducing development time and costs.  The approach also opens up possibilities for creating more intelligent and adaptable software systems capable of handling complex and evolving requirements.