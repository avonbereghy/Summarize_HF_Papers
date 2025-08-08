# Skywork-Reward-V2: Scaling Preference Data Curation via Human-AI Synergy

**Paper ID:** 2507.01352

**URL:** https://huggingface.co/papers/2507.01352

## Summary

## Executive Summary
The paper introduces **Skywork-Reward-V2**, a suite of reward models that achieve state-of-the-art performance in *reinforcement learning from human feedback* (RLHF) by leveraging a large-scale preference dataset, **SynPref-40M**, and a human-AI synergistic curation pipeline. This approach addresses the limitations of current *preference datasets*, which are often *narrowly scoped* or lack *rigorous quality control*. By combining human annotation quality with AI scalability, the authors demonstrate significant improvements in *alignment with human preferences*, *objective correctness*, and *safety*.

## Key Contributions and Findings
* **Large-Scale Preference Dataset**: The authors introduce **SynPref-40M**, a dataset comprising 40 million *preference pairs*, which enables training of more accurate and robust reward models.
* **Human-AI Synergistic Curation**: The paper presents a two-stage pipeline that leverages the complementary strengths of human annotation quality and AI scalability, allowing for *efficient and effective data curation*.
* **State-of-the-Art Reward Models**: The authors introduce **Skywork-Reward-V2**, a suite of eight reward models ranging from 0.6B to 8B parameters, which achieve state-of-the-art performance across seven major *reward model benchmarks*.
* **Ablation Studies**: The authors conduct ablation studies to confirm that the effectiveness of their approach stems not only from *data scale* but also from *high-quality curation*.
* **Versatility and Robustness**: The paper demonstrates the versatility and robustness of **Skywork-Reward-V2** across a wide range of capabilities, including *resistance to stylistic biases* and *best-of-N scaling*.

## Methodology Overview
The methodology consists of two major components: **data collection** and **model training**. The authors use a human-AI synergistic pipeline to collect and curate a large-scale preference dataset, **SynPref-40M**, which is then used to train a suite of reward models, **Skywork-Reward-V2**, using *large language models* and *reinforcement learning techniques*.

## Results and Performance
The key results show that **Skywork-Reward-V2** achieves state-of-the-art performance across seven major *reward model benchmarks*, with **significant improvements** in *alignment with human preferences*, *objective correctness*, and *safety*. The authors also report **high scores** in terms of *resistance to stylistic biases* and *best-of-N scaling*, demonstrating the versatility and robustness of their approach.

## Limitations and Future Work
The authors mention that their approach still has limitations, including the potential for *bias in human annotations* and the need for *further evaluation* of their models in real-world applications. Potential future directions include *exploring new methods for data curation* and *applying their approach to other areas of AI research*.

## Practical Applications
The paper has significant implications for *real-world applications* of reinforcement learning, including *autonomous systems*, *human-computer interaction*, and *decision-making systems*. The authors' approach can be used to develop more accurate and robust reward models that align with human preferences and values, leading to more *effective and safe* AI systems.

---

**Authors:** Chris Yuhao Liu, Liang Zeng, Yuzhen Xiao, Jujie He, Jiacai Liu, Chaojie Wang, Rui Yan, Wei Shen, Fuxiang Zhang, Jiacheng Xu, Yang Liu, Yahui Zhou
