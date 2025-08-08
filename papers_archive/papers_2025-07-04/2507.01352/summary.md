# Skywork-Reward-V2: Scaling Preference Data Curation via Human-AI Synergy

**Paper ID:** 2507.01352

**URL:** https://huggingface.co/papers/2507.01352

## Summary

## Executive Summary
The paper introduces **Skywork-Reward-V2**, a suite of reward models that achieve state-of-the-art performance in *reinforcement learning from human feedback* (RLHF) by leveraging **human-AI synergy** in data curation. The authors address the limitations of current preference datasets by creating a large-scale dataset, **SynPref-40M**, comprising 40 million preference pairs, and designing a two-stage pipeline that combines *human annotation quality* with *AI scalability*. This approach enables the training of versatile reward models that excel in *alignment with human preferences*, *objective correctness*, *safety*, and *resistance to stylistic biases*.

## Key Contributions and Findings
* **Large-Scale Preference Dataset**: The authors create **SynPref-40M**, a massive dataset of 40 million preference pairs, which provides a *diverse and nuanced* representation of human preferences.
* **Human-AI Synergistic Pipeline**: The paper presents a two-stage pipeline that leverages the *complementary strengths* of human annotation quality and AI scalability, enabling efficient and high-quality data curation.
* **State-of-the-Art Reward Models**: The **Skywork-Reward-V2** series achieves state-of-the-art performance across seven major reward model benchmarks, demonstrating *substantial progress* in open reward models.
* **Importance of Data Quality**: Ablation studies confirm that the effectiveness of the approach stems not only from *data scale* but also from *high-quality curation*, highlighting the importance of careful data preparation.

## Methodology Overview
The methodology involves **data collection** and **curation** using a two-stage pipeline that combines **human annotation** with **AI-based automatic curation**. The pipeline consists of *human verification* and *AI-driven filtering*, which ensures *high-quality* and *relevant* preference data. The curated data is then used to train **reward models** using *advanced training techniques*.

## Results and Performance
The **Skywork-Reward-V2** series achieves **state-of-the-art performance** across seven major reward model benchmarks, with *significant improvements* in *alignment with human preferences*, *objective correctness*, and *safety*. The models demonstrate **versatility** across a wide range of capabilities, including *best-of-N scaling* and *resistance to stylistic biases*. The results show **substantial progress** in open reward models, with *improved performance* compared to existing state-of-the-art models.

## Limitations and Future Work
The paper mentions the need for further research in *improving data quality* and *scaling up* the human-AI synergistic pipeline. Potential future directions include *exploring new applications* of the **Skywork-Reward-V2** series and *investigating the use of alternative* *machine learning architectures*.

## Practical Applications
The **Skywork-Reward-V2** series has potential *real-world applications* in areas such as *human-computer interaction*, *natural language processing*, and *decision-making systems*. The models can be used to improve the *alignment of AI systems with human values* and *preferences*, enabling more *effective and safe* decision-making. The paper highlights the importance of *high-quality data curation* and *human-AI synergy* in achieving *state-of-the-art performance* in RLHF, which can have significant implications for the development of more *advanced and reliable* AI systems.

---

**Authors:** Chris Yuhao Liu, Liang Zeng, Yuzhen Xiao, Jujie He, Jiacai Liu, Chaojie Wang, Rui Yan, Wei Shen, Fuxiang Zhang, Jiacheng Xu, Yang Liu, Yahui Zhou
