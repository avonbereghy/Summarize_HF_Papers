# Pixels, Patterns, but No Poetry: To See The World like Humans

**Paper ID:** 2507.16863

**URL:** https://huggingface.co/papers/2507.16863

## Summary

## Executive Summary
The paper **Pixels, Patterns, but No Poetry: To See The World like Humans** explores the challenge of achieving *human-like perception* in **Multimodal Large Language Models (MLLMs)**. The authors introduce the **Turing Eye Test (TET)**, a *perception-oriented benchmark* that evaluates MLLMs' performance on *synthetic images*. The findings reveal that state-of-the-art MLLMs exhibit *catastrophic failures* on these tasks, which are *trivial for humans*. The results suggest that the **vision tower** is the key component that needs improvement, rather than the *language backbone*, to achieve *human-like perception*.

## Key Contributions and Findings
* **Introduction of the Turing Eye Test**: The authors introduce the *TET*, a benchmark that evaluates MLLMs' performance on *synthetic images* and provides a new perspective on *perception-oriented tasks*.
* **Evaluation of State-of-the-Art MLLMs**: The authors find that state-of-the-art MLLMs exhibit *catastrophic failures* on the *TET tasks*, which are *trivial for humans*, highlighting the need for improvement in *vision tower generalization*.
* **Importance of Vision Tower Fine-Tuning**: The authors show that *fine-tuning the vision tower* enables rapid adaptation to the *TET tasks*, while *in-context learning* and *training on language backbone* are not effective.
* **Gap between MLLMs and Human Perception**: The authors identify a key gap between current MLLMs and *human perception*, which is the ability to generalize to new *visual patterns* and *perceptual tasks*.

## Methodology Overview
The authors use a **benchmark-based approach** to evaluate MLLMs' performance on *perception-oriented tasks*. The **Turing Eye Test (TET)** is a *diagnostic benchmark* that consists of four tasks that test MLLMs' ability to process *synthetic images*. The authors use *state-of-the-art MLLMs* and evaluate their performance using *in-context learning*, *training on language backbone*, and *fine-tuning the vision tower*.

## Results and Performance
The authors report **catastrophic failures** of state-of-the-art MLLMs on the *TET tasks*, with *low accuracy* and *high error rates*. In contrast, *fine-tuning the vision tower* enables rapid adaptation to the *TET tasks*, with **significant improvements** in *accuracy* and *error rates*. The results are compared to *human performance*, which is *near-perfect* on the same tasks.

## Limitations and Future Work
The authors mention that the current version of the **Turing Eye Test (TET)** has limited *diversity* and *scope*, and plan to introduce more *diverse tasks* and *methods* to enhance *visual generalization* in future work. The authors also acknowledge the need for further research on *vision tower generalization* and *human-like perception*.

## Practical Applications
The research has potential *real-world applications* in areas such as **computer vision**, **robotics**, and **human-computer interaction**. The ability to achieve *human-like perception* in MLLMs could enable more *effective* and *efficient* interaction between humans and machines, and could have significant implications for *artificial intelligence* and *machine learning*.

---

**Authors:** Hongcheng Gao, Zihao Huang, Lin Xu, Jingyi Tang, Xinhao Li, Yue Liu, Haoyang Li, Taihang Hu, Minhua Lin, Xinlong Yang, Ge Wu, Balong Bi, Hongyu Chen, Wentao Zhang
