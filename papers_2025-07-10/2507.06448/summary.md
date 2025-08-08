# Perception-Aware Policy Optimization for Multimodal Reasoning

**Paper ID:** 2507.06448

**URL:** https://huggingface.co/papers/2507.06448

## Summary

## Executive Summary
The paper introduces **Perception-Aware Policy Optimization (PAPO)**, a novel approach to improve the performance of Large Language Models (LLMs) in *multimodal reasoning tasks*. By incorporating an *Implicit Perception Loss* into the **GRPO** objective, PAPO encourages the model to learn to perceive visual inputs while learning to reason, without relying on additional data curation or external reward models. This approach yields significant improvements in overall performance, particularly on tasks with high *vision dependency*, and lays the groundwork for a new **RL** framework that promotes *visually grounded reasoning*.

## Key Contributions and Findings
* **Improved Multimodal Reasoning**: PAPO achieves significant overall improvements (4.4%) on diverse *multimodal benchmarks*, with more pronounced improvements (8.0%) on tasks with high *vision dependency*.
* **Perception Error Reduction**: The approach reduces *perception errors* by 30.5%, indicating improved *perceptual capabilities* with PAPO.
* **Double Entropy Loss**: The authors identify a unique *loss hacking issue* and mitigate it through a **Double Entropy Loss**, ensuring the stability and effectiveness of the PAPO framework.
* **RL Framework**: PAPO introduces a deeper integration of *perception-aware supervision* into **RLVR** learning objectives, paving the way for a new **RL** framework that encourages *visually grounded reasoning*.

## Methodology Overview
The methodology involves **GRPO** as the foundation, with the addition of an *Implicit Perception Loss* in the form of a **KL divergence term**. This term encourages the model to learn to perceive visual inputs while learning to reason, using only internal *supervision signals*. The approach also incorporates a **Double Entropy Loss** to mitigate *loss hacking issues* and ensure the stability of the PAPO framework.

## Results and Performance
The results show significant improvements in **overall performance** (4.4%) and **perception error reduction** (30.5%), with more pronounced improvements (8.0%) on tasks with high *vision dependency*. The **Double Entropy Loss** ensures the stability and effectiveness of the PAPO framework, outperforming baseline models in *multimodal benchmarks*.

## Limitations and Future Work
The paper mentions the potential for *loss hacking issues* and the need for further analysis and mitigation strategies. Future work may involve exploring the application of PAPO to other *multimodal tasks*, investigating the use of alternative *perception loss functions*, and developing more advanced **RL** frameworks that incorporate *perception-aware supervision*.

## Practical Applications
The PAPO framework has potential applications in real-world scenarios that involve *multimodal reasoning*, such as *visual question answering*, *image captioning*, and *human-computer interaction*. The approach can be used to improve the performance of LLMs in these tasks, enabling more accurate and effective *visually grounded reasoning* and decision-making.

---

**Authors:** Zhenhailong Wang, Xuehang Guo, Sofia Stoica, Haiyang Xu, Hongru Wang, Hyeonjeong Ha, Xiusi Chen, Yangyi Chen, Ming Yan, Fei Huang, Heng Ji
