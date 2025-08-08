# MiroMind-M1: An Open-Source Advancement in Mathematical Reasoning via
  Context-Aware Multi-Stage Policy Optimization

**Paper ID:** 2507.14683

**URL:** https://huggingface.co/papers/2507.14683

## Summary

## Executive Summary
The paper introduces **MiroMind-M1**, a fully open-source *reasoning language model* (RLM) that achieves state-of-the-art performance in *mathematical reasoning* tasks. By leveraging a **Qwen-2.5 backbone** and a novel *Context-Aware Multi-Stage Policy Optimization* algorithm, the model demonstrates superior *token efficiency* and robustness. The authors release the complete stack, including models, datasets, and training configurations, to facilitate *reproducibility* and foster community advancement in **RLM development**.

## Key Contributions and Findings
* **Model Architecture**: The MiroMind-M1 series is built on a **Qwen-2.5 backbone**, which provides a solid foundation for *mathematical reasoning* tasks. The model is trained in two stages: *SFT* (Supervised Fine-Tuning) and *RLVR* (Reinforcement Learning with Verification).
* **Training Methodology**: The authors introduce *Context-Aware Multi-Stage Policy Optimization*, an algorithm that integrates *length-progressive training* with an adaptive *repetition penalty* to encourage *context-aware RL training*.
* **Performance Evaluation**: The model achieves **state-of-the-art** or competitive performance on the *AIME24*, *AIME25*, and *MATH benchmarks*, with superior *token efficiency* among **Qwen-2.5-based open-source models**.
* **Open-Source Resources**: The authors release the complete stack, including models, datasets, and training configurations, to facilitate *reproducibility* and community advancement in **RLM development**.
* **Dataset Curation**: The authors curate a carefully selected corpus of *719K math-reasoning problems* with verified *CoT trajectories*, which serves as a valuable resource for future research.

## Methodology Overview
The methodology involves **two-stage training**: *SFT* on a carefully curated corpus of *math-reasoning problems*, followed by *RLVR* on a set of *challenging and verifiable problems*. The authors employ **Context-Aware Multi-Stage Policy Optimization**, which integrates *length-progressive training* with an adaptive *repetition penalty* to encourage *context-aware RL training*. The model is built on a **Qwen-2.5 backbone**, which provides a solid foundation for *mathematical reasoning* tasks.

## Results and Performance
The model achieves **state-of-the-art** performance on the *AIME24*, *AIME25*, and *MATH benchmarks*, with superior *token efficiency* among **Qwen-2.5-based open-source models**. The results demonstrate the effectiveness of the *Context-Aware Multi-Stage Policy Optimization* algorithm in improving the model's *robustness* and *efficiency*. The authors also report competitive performance compared to other *open-source RLMs*, highlighting the potential of the MiroMind-M1 series for *mathematical reasoning* tasks.

## Limitations and Future Work
The authors do not explicitly mention limitations, but potential future directions include:
* Exploring the application of the MiroMind-M1 series to other *domains* and *tasks*
* Investigating the use of *different backbone architectures* and *training methodologies*
* Developing more *efficient* and *effective* algorithms for *context-aware RL training*

## Practical Applications
The MiroMind-M1 series has potential *practical applications* in:
* **Education**: The model can be used to develop *intelligent tutoring systems* that provide personalized *mathematical reasoning* guidance to students.
* **Research**: The model can be used to automate *mathematical reasoning* tasks, freeing up researchers to focus on higher-level tasks and accelerating the discovery of new *mathematical concepts*.
* **Industry**: The model can be used to develop *decision-support systems* that leverage *mathematical reasoning* to provide insights and recommendations in various *domains*.

---

**Authors:** Xingxuan Li, Yao Xiao, Dianwen Ng, Hai Ye, Yue Deng, Xiang Lin, Bin Wang, Zhanfeng Mo, Chong Zhang, Yueyi Zhang, Zonglin Yang, Ruilin Li, Lei Lei, Shihao Xu, Han Zhao, Weiling Chen, Feng Ji, Lidong Bing
