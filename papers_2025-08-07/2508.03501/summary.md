# Training Long-Context, Multi-Turn Software Engineering Agents with
  Reinforcement Learning

**Paper ID:** 2508.03501

**URL:** https://huggingface.co/papers/2508.03501

## Summary

## Executive Summary
This academic paper explores the application of **Reinforcement Learning (RL)** to train *long-context, multi-turn* software engineering agents. The authors demonstrate the successful use of a modified **Decoupled Advantage Policy Optimization (DAPO)** algorithm to train an agent based on *Qwen2.5-72B-Instruct* to solve real-world software engineering tasks. The approach shows a significant increase in the agent's *success rate* on the **SWE-bench Verified** benchmark, outperforming leading open-weight models without relying on *teacher models*. This research provides a viable path toward building more capable *autonomous agents* for complex real-world problems based on **open models**.

## Key Contributions and Findings
* **Improved Success Rate**: The authors' approach increases the agent's success rate on the **SWE-bench Verified** benchmark from 20% to 39%, demonstrating the effectiveness of *reinforcement learning* in software engineering tasks.
* **Multi-Turn Interaction**: The paper highlights the importance of *multi-turn interactions* with a *stateful environment* in software engineering, which is a significant departure from single-turn problems like *mathematical reasoning* or *single-shot code generation*.
* **Autonomous Agents**: The research shows that it is possible to build *autonomous agents* for complex real-world problems using **open models**, without relying on *teacher models* or *fine-tuning*.
* **Comparison to Leading Models**: The authors' agent matches or outperforms leading open-weight models like **DeepSeek-V3-0324** and **Qwen3-235B-A22B** using an identical *scaffolding*, demonstrating the potential of *reinforcement learning* in software engineering.
* **Real-World Applications**: The paper provides a foundation for building more capable *autonomous agents* for real-world software engineering tasks, with potential applications in *code generation*, *code review*, and *software development*.

## Methodology Overview
The authors use a modified **Decoupled Advantage Policy Optimization (DAPO)** algorithm to train an agent based on *Qwen2.5-72B-Instruct*. The methodology involves *reinforcement learning* with a *stateful environment* that responds to each action with a non-trivial *observation*. The agent is trained on real-world software engineering tasks, with a focus on *multi-turn interactions* and *long-context* understanding.

## Results and Performance
The authors report a significant increase in the agent's **success rate** on the **SWE-bench Verified** benchmark, from 20% to 39%. The agent also matches or outperforms leading open-weight models like **DeepSeek-V3-0324** and **Qwen3-235B-A22B** using an identical *scaffolding*. The results demonstrate the effectiveness of *reinforcement learning* in software engineering tasks, with *improved performance* and *increased accuracy*.

## Limitations and Future Work
The authors do not explicitly mention limitations, but potential future directions include:
* Exploring other *reinforcement learning* algorithms and techniques
* Applying the approach to other real-world domains and tasks
* Investigating the use of *transfer learning* and *fine-tuning* to improve performance
* Developing more advanced *stateful environments* and *observation models*

## Practical Applications
The research has significant implications for real-world software engineering tasks, including:
* **Code Generation**: The agent can be used to generate high-quality code for complex software projects
* **Code Review**: The agent can assist in code review tasks, providing *accurate* and *informative* feedback
* **Software Development**: The agent can be integrated into software development workflows, providing *autonomous* support for developers
* **DevOps**: The agent can be used to automate *DevOps* tasks, such as *testing* and *deployment*

---

**Authors:** Alexander Golubev, Maria Trofimova, Sergei Polezhaev, Ibragim Badertdinov, Maksim Nekrashevich, Anton Shevtsov, Simon Karasik, Sergey Abramov, Andrei Andriushchenko, Filipp Fisin, Sergei Skvortsov, Boris Yangel
