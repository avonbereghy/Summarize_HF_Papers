# Reasoning or Memorization? Unreliable Results of Reinforcement Learning
  Due to Data Contamination

**Paper ID:** 2507.10532

**URL:** https://huggingface.co/papers/2507.10532

## Summary

## Executive Summary
The paper investigates the **reliability** of *reinforcement learning* (RL) methods in enhancing the **reasoning capabilities** of large language models (LLMs). It highlights the potential issue of *data contamination* in popular benchmarks, which can lead to **unreliable results**. The authors introduce a **novel dataset**, RandomCalculation, generated using a *synthetic arithmetic problem generator*, to evaluate RL methods on *uncontaminated benchmarks*. The study emphasizes the importance of **accurate reward signals** and *diverse model families* in ensuring **trustworthy conclusions**.

## Key Contributions and Findings
* **Data Contamination Analysis**: The authors reveal that *pretraining on large-scale web corpora* makes models like Qwen2.5 vulnerable to *data contamination* in popular benchmarks, leading to **unreliable results**.
* **Novel Dataset Introduction**: The introduction of the RandomCalculation dataset, generated using a *synthetic arithmetic problem generator*, provides a *leakage-free* environment for evaluating RL methods.
* **Reward Signal Evaluation**: The study shows that only *accurate reward signals* consistently improve performance, while *noisy or incorrect signals* do not, highlighting the importance of **reward signal quality**.
* **Model Diversity Evaluation**: The authors emphasize the need to evaluate RL methods across *diverse model families*, such as Llama, to ensure **trustworthy conclusions**.
* **Benchmarking Methodology**: The paper proposes a **new benchmarking methodology** that uses *uncontaminated benchmarks* and *diverse model families* to evaluate RL methods.

## Methodology Overview
The methodology involves **pretraining** LLMs on large-scale web corpora, followed by **fine-tuning** using *reinforcement learning* methods. The authors employ a **synthetic arithmetic problem generator** to create the RandomCalculation dataset, which is used to evaluate the RL methods. The study utilizes *techniques like reinforcement learning* and *dataset generation* to investigate the **reliability** of RL methods.

## Results and Performance
The key results show that **accurate reward signals** consistently improve performance, with **significant gains** in mathematical reasoning tasks. In contrast, *noisy or incorrect signals* do not lead to **improved performance**, highlighting the importance of **reward signal quality**. The study also reports *comparisons* between different models, such as Qwen2.5 and Llama, demonstrating the need for **diverse model families** in evaluating RL methods.

## Limitations and Future Work
The study mentions the following limitations:
* The analysis is limited to *mathematical reasoning tasks* and may not generalize to other domains.
* The RandomCalculation dataset may not cover all possible *arithmetic problem types*.
Potential future directions include:
* **Expanding the dataset** to cover more *arithmetic problem types* and domains.
* **Investigating other RL methods** to evaluate their **reliability** and **performance**.

## Practical Applications
The study has significant implications for **real-world applications** of LLMs, such as:
* **Education**: Developing more **reliable** and **effective** AI-powered educational tools.
* **Automated reasoning**: Improving the **accuracy** and **reliability** of automated reasoning systems.
* **Decision-making**: Enhancing the **trustworthiness** of AI-driven decision-making systems.
The paper's findings emphasize the need for **careful evaluation** and **validation** of RL methods to ensure **trustworthy conclusions** and **reliable performance** in real-world applications.

---

**Authors:** Mingqi Wu, Zhihao Zhang, Qiaole Dong, Zhiheng Xi, Jun Zhao, Senjie Jin, Xiaoran Fan, Yuhao Zhou, Yanwei Fu, Qin Liu, Songyang Zhang, Qi Zhang
