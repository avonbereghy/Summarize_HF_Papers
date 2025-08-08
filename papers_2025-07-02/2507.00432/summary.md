# Does Math Reasoning Improve General LLM Capabilities? Understanding
  Transferability of LLM Reasoning

**Paper ID:** 2507.00432

**URL:** https://huggingface.co/papers/2507.00432

## Summary

## Executive Summary
The paper explores the **transferability of large language models (LLMs)** and their ability to generalize across different domains, with a focus on *math reasoning* as a key area of improvement. The authors evaluate over 20 models and find that most models that excel in math fail to transfer their gains to other domains, suggesting that standard post-training recipes, such as **supervised fine-tuning (SFT)**, may not be effective in advancing *general problem-solving abilities*. The study highlights the importance of **reinforcement learning (RL)** in preserving *general-domain structure* and promoting *transfer learning*.

## Key Contributions and Findings
* **Math Reasoning Evaluation**: The authors evaluate the performance of LLMs on *math benchmarks* and find that while models have surpassed human-level performance, they often fail to transfer their gains to other domains, such as *scientific QA* or *agent planning*.
* **Tuning Method Comparison**: The study compares the effectiveness of **reinforcement learning (RL)** and **supervised fine-tuning (SFT)** in promoting *transfer learning* and finds that RL-tuned models generalize better across domains, while SFT-tuned models often *forget general capabilities*.
* **Latent-Space Analysis**: The authors conduct *latent-space representation* and *token-space distribution shift* analyses, which reveal that SFT induces substantial *representation and output drift*, while RL preserves *general-domain structure*.
* **Implications for Post-Training Recipes**: The study suggests that standard post-training recipes, particularly the reliance on SFT-distilled data, may need to be rethought in order to advance *reasoning models* and promote *transfer learning*.

## Methodology Overview
The authors employ a **controlled experiment** approach, using *Qwen3-14B models* and varying the **tuning method** (RL vs. SFT) and *training data* (math-only vs. general-domain). The study utilizes *benchmark datasets* and *evaluation metrics* to assess the performance of the models across different domains.

## Results and Performance
The key results show that **RL-tuned models** outperform **SFT-tuned models** in terms of *transfer learning* and *generalization* across domains, with **significant improvements** in *math reasoning* and *scientific QA* tasks. The study also finds that SFT-tuned models exhibit *substantial representation and output drift*, while RL-tuned models preserve *general-domain structure*.

## Limitations and Future Work
The study mentions the following limitations:
* The focus on *math reasoning* as a key area of improvement may not be representative of other domains.
* The use of *Qwen3-14B models* may not be generalizable to other LLM architectures.
Potential future directions include:
* Exploring the application of RL and other *tuning methods* to other domains and tasks.
* Investigating the use of *multitask learning* and *domain adaptation* techniques to promote *transfer learning*.

## Practical Applications
The study has implications for the development of **more generalizable LLMs** that can be applied to a wide range of tasks and domains, including:
* **Math education**: Developing LLMs that can provide *personalized math instruction* and *problem-solving support*.
* **Scientific research**: Creating LLMs that can assist with *scientific discovery* and *hypothesis generation*.
* **AI-powered decision-making**: Building LLMs that can provide *informed decision-making support* and *risk analysis* across various domains.

---

**Authors:** Maggie Huan, Yuetai Li, Tuney Zheng, Xiaoyu Xu, Seungone Kim, Minxin Du, Radha Poovendran, Graham Neubig, Xiang Yue
