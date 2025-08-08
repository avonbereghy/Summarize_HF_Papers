# Listener-Rewarded Thinking in VLMs for Image Preferences

**Paper ID:** 2506.22832

**URL:** https://huggingface.co/papers/2506.22832

## Summary

## Executive Summary
The paper introduces a novel approach to training robust and generalizable reward models for human visual preferences, leveraging **listener-rewarded thinking** in Vision-Language Models (VLMs). By incorporating an independent *listener* model to evaluate the reasoner's chain-of-thought, the authors develop a **listener-augmented GRPO framework** that encourages the reasoner to produce *persuasive explanations*. This approach achieves state-of-the-art results on the ImageReward benchmark and improves out-of-distribution performance on a large-scale human preference dataset, demonstrating a scalable and data-efficient path to aligning VLMs with *nuanced human preferences*.

## Key Contributions and Findings
* **Improved Generalization**: The listener-augmented GRPO framework improves the generalization of reward models, reducing the likelihood of *memorization* and increasing *reasoning accuracy*.
* **Listener-Shaped Rewards**: The introduction of a *listener* model to provide dense, calibrated confidence scores shapes the RL reward signal, encouraging the reasoner to produce *persuasive explanations* that are *independent* of the reasoner's own biases.
* **State-of-the-Art Performance**: The proposed approach achieves **best accuracy** on the ImageReward benchmark (67.4%) and significantly improves out-of-distribution performance on a large-scale human preference dataset, with up to +6% improvement over *naive reasoner* baselines.
* **Reducing Reasoning Contradictions**: The listener-augmented GRPO framework reduces *reasoning contradictions* compared to strong **GRPO** and **SFT** baselines, demonstrating improved *alignment* with human preferences.

## Methodology Overview
The methodology involves **training** a VLM using a **listener-augmented GRPO framework**, which incorporates an independent *listener* model to evaluate the reasoner's chain-of-thought. The *listener* model provides dense, calibrated confidence scores, shaping the **RL reward signal** to encourage the reasoner to produce *persuasive explanations*. The approach leverages *reinforcement learning* and *Group Relative Policy Optimization (GRPO)* to improve generalization and reduce *memorization*.

## Results and Performance
The key results demonstrate **state-of-the-art performance** on the ImageReward benchmark, with **67.4% accuracy**. The approach also improves out-of-distribution performance on a large-scale human preference dataset, with up to **+6% improvement** over *naive reasoner* baselines. The results show *significant reductions* in *reasoning contradictions* compared to strong **GRPO** and **SFT** baselines, demonstrating improved *alignment* with human preferences.

## Limitations and Future Work
The paper does not explicitly mention limitations, but potential future directions include:
* Exploring the application of listener-rewarded thinking to other *domains* and *tasks*
* Investigating the use of *multiple listeners* to further improve generalization and reduce *bias*
* Developing more *efficient* and *scalable* methods for training listener-augmented VLMs

## Practical Applications
The proposed approach has potential real-world applications in:
* **Image and video generation**: Aligning generative models with human visual preferences to produce more *realistic* and *desirable* content
* **Recommendation systems**: Improving the accuracy and *personalization* of recommendations by incorporating human preferences and *nuanced* understanding of user behavior
* **Human-computer interaction**: Developing more *intuitive* and *user-friendly* interfaces that align with human preferences and *cognitive biases*

---

**Authors:** Alexander Gambashidze, Li Pengyi, Matvey Skripkin, Andrey Galichin, Anton Gusarov, Konstantin Sobolev, Andrey Kuznetsov, Ivan Oseledets
