# Skywork-Reward-V2: Scaling Preference Data Curation via Human-AI Synergy

**Paper ID:** 2507.01352

**URL:** https://huggingface.co/papers/2507.01352

## Summary

## Executive Summary
The paper introduces **Skywork-Reward-V2**, a suite of reward models that achieve state-of-the-art performance in *reinforcement learning from human feedback* (RLHF) by leveraging **human-AI synergy** in data curation. The authors address the limitations of current preference datasets by creating a large-scale dataset, **SynPref-40M**, comprising 40 million preference pairs, and propose a *two-stage pipeline* that combines the strengths of human annotation quality and AI scalability. This approach enables the training of versatile reward models that excel in *alignment with human preferences*, *objective correctness*, *safety*, and *resistance to stylistic biases*.

## Key Contributions and Findings
* **Large-Scale Preference Dataset**: The authors create **SynPref-40M**, a massive dataset of 40 million preference pairs, which is used to train the **Skywork-Reward-V2** models, highlighting the importance of *data scale* and *high-quality curation*.
* **Human-AI Synergistic Curation**: The paper proposes a *human-AI synergistic two-stage pipeline* that leverages the complementary strengths of human annotation quality and AI scalability, enabling *efficient data curation* at scale.
* **State-of-the-Art Reward Models**: The **Skywork-Reward-V2** series achieves state-of-the-art performance across seven major reward model benchmarks, demonstrating *substantial progress* in open reward models and the potential of *human-AI curation synergy*.
* **Ablation Studies**: The authors conduct *ablation studies* to confirm that the effectiveness of their approach stems not only from *data scale* but also from *high-quality curation*, emphasizing the importance of careful data preparation.

## Methodology Overview
The methodology involves **two major components**: (1) the creation of the **SynPref-40M** dataset, which is curated using a *human-AI synergistic two-stage pipeline*, and (2) the training of the **Skywork-Reward-V2** models on a carefully curated subset of 26 million preference pairs. The pipeline leverages *large language models* to perform automatic curation based on *human guidance*, ensuring *high-quality annotations*.

## Results and Performance
The **Skywork-Reward-V2** series achieves **state-of-the-art performance** across seven major reward model benchmarks, with *impressive results* in *alignment with human preferences*, *objective correctness*, *safety*, and *resistance to stylistic biases*. The models demonstrate **versatility** across a wide range of capabilities, including *best-of-N scaling*, and outperform existing models in *most evaluation metrics*.

## Limitations and Future Work
The paper mentions the potential **limitations** of the approach, including the need for *large-scale datasets* and *high-quality annotations*. Future work may focus on exploring **new applications** of the **Skywork-Reward-V2** models, such as *real-world reinforcement learning tasks*, and investigating **alternative curation methods** to further improve *data quality*.

## Practical Applications
The **Skywork-Reward-V2** models have potential *real-world applications* in areas like *autonomous systems*, *human-computer interaction*, and *decision-making systems*, where *alignment with human preferences* and *safety* are crucial. The models can be used to improve the *performance* and *reliability* of these systems, enabling *more efficient* and *effective* decision-making processes.

---

**Authors:** Chris Yuhao Liu, Liang Zeng, Yuzhen Xiao, Jujie He, Jiacai Liu, Chaojie Wang, Rui Yan, Wei Shen, Fuxiang Zhang, Jiacheng Xu, Yang Liu, Yahui Zhou
