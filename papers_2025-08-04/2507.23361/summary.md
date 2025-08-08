# SWE-Exp: Experience-Driven Software Issue Resolution

**Paper ID:** 2507.23361

**URL:** https://huggingface.co/papers/2507.23361

## Summary

## Executive Summary
The paper introduces **SWE-Exp**, an experience-driven approach to software issue resolution, which leverages *large language model (LLM) agents* and *multi-agent collaboration* to improve resolution rates. By distilling concise and actionable experience from prior agent trajectories, **SWE-Exp** enables continuous learning across issues, reducing redundant exploration of failed trajectories and missed chances to adapt successful issue resolution methods. This approach establishes a new paradigm in which automated software engineering agents systematically accumulate and leverage repair expertise, shifting from *trial-and-error exploration* to strategic, experience-driven issue resolution.

## Key Contributions and Findings
* **Experience-Driven Approach**: The paper proposes an experience-driven approach that captures both successful and failed repair attempts, extracting reusable issue resolution knowledge at different levels, from *high-level problem comprehension* to specific *code changes*.
* **Multi-Faceted Experience Bank**: The authors introduce a multi-faceted experience bank that stores and retrieves experience from prior agent trajectories, enabling the agent to learn from its past experiences and adapt to new issues.
* **State-of-the-Art Resolution Rate**: The experiments demonstrate that **SWE-Exp** achieves a state-of-the-art resolution rate of **41.6% Pass@1** on SWE-bench-Verified under open-source agent frameworks, outperforming existing methods in *automated software engineering*.
* **Continuous Learning**: The approach enables continuous learning across issues, allowing the agent to accumulate and leverage repair expertise over time, and fundamentally shifting from *trial-and-error exploration* to strategic, experience-driven issue resolution.

## Methodology Overview
The methodology involves **experience extraction**, **experience storage**, and **experience retrieval** components, using *techniques such as Monte Carlo Tree Search (MCTS)* to distill concise and actionable experience from prior agent trajectories. The **multi-faceted experience bank** is a key component! that captures both successful and failed repair attempts, and extracts reusable issue resolution knowledge at different levels.

## Results and Performance
The experiments demonstrate that **SWE-Exp** achieves a **41.6% Pass@1** resolution rate on SWE-bench-Verified, outperforming existing methods in *automated software engineering*. This result is *significantly higher* than the baseline methods, indicating the effectiveness of the experience-driven approach. The authors also report *improved performance* in terms of *resolution time* and *exploration efficiency*.

## Limitations and Future Work
The paper does not mention specific limitations, but potential future directions include:
* Exploring the application of **SWE-Exp** to other domains, such as *natural language processing* or *computer vision*
* Investigating the use of *transfer learning* to adapt the experience-driven approach to new issues or domains
* Developing more advanced *experience extraction* and *experience retrieval* techniques to further improve the performance of **SWE-Exp**

## Practical Applications
The **SWE-Exp** approach has potential practical applications in *automated software engineering*, such as:
* Improving the efficiency and effectiveness of software issue resolution processes
* Enhancing the capabilities of automated software engineering agents to accumulate and leverage repair expertise
* Reducing the time and cost associated with software issue resolution, and improving the overall quality of software systems.

---

**Authors:** Silin Chen, Shaoxin Lin, Xiaodong Gu, Yuling Shi, Heng Lian, Longfei Yun, Dong Chen, Weiguo Sun, Lin Cao, Qianxiang Wang
