# Group Sequence Policy Optimization

**Paper ID:** 2507.18071

**URL:** https://huggingface.co/papers/2507.18071

## Summary

## Executive Summary
This paper introduces **Group Sequence Policy Optimization (GSPO)**, a novel *reinforcement learning* algorithm designed for training large *language models*. Unlike previous algorithms, GSPO defines the importance ratio based on *sequence likelihood* and performs *sequence-level clipping*, *rewarding*, and *optimization*. The authors demonstrate that GSPO achieves superior **training efficiency** and **performance** compared to existing algorithms, notably stabilizing *Mixture-of-Experts (MoE) RL training* and simplifying the design of *RL infrastructure*. These merits of GSPO have contributed to the remarkable improvements in the latest *Qwen3 models*, showcasing its potential for *real-world applications*.

## Key Contributions and Findings
* **Improved Training Efficiency**: GSPO achieves superior *training speed* and *stability* compared to existing algorithms, making it an attractive choice for large-scale *language model* training.
* **Stabilized MoE RL Training**: GSPO notably stabilizes *Mixture-of-Experts (MoE) RL training*, which is a challenging task in *reinforcement learning*.
* **Simplified RL Infrastructure**: GSPO has the potential to simplify the design of *RL infrastructure*, making it easier to implement and deploy *reinforcement learning* algorithms in *real-world applications*.
* **Superior Performance**: GSPO demonstrates superior **performance** compared to existing algorithms, including the *GRPO algorithm*, in terms of *training efficiency* and *model accuracy*.
* **Sequence-Level Optimization**: GSPO performs *sequence-level clipping*, *rewarding*, and *optimization*, which is a key difference from previous algorithms that adopt *token-level importance ratios*.

## Methodology Overview
The methodology of GSPO involves **sequence likelihood** calculation, **sequence-level clipping**, and **optimization** using *reinforcement learning* techniques. The authors use **importance sampling** to estimate the *sequence likelihood* and perform *clipping* to stabilize the training process. The **optimization** process involves updating the model parameters using *gradient descent* and *reward functions*.

## Results and Performance
The results show that GSPO achieves superior **training efficiency** and **performance** compared to existing algorithms, with *significant improvements* in *training speed* and *model accuracy*. The authors report **state-of-the-art results** on several benchmarks, including the *Qwen3 models*, with GSPO outperforming the *GRPO algorithm* in terms of **training efficiency** and **performance**. The results are compared to existing algorithms using *metrics* such as **training time**, **model accuracy**, and **reward functions*.

## Limitations and Future Work
The authors mention that GSPO may have limitations in terms of **computational cost** and **scalability**, which could be addressed in future work. Potential future directions include *extending GSPO to other domains*, *improving the scalability of GSPO*, and *exploring new applications* of GSPO in *real-world scenarios*.

## Practical Applications
GSPO has potential *practical applications* in *natural language processing*, *computer vision*, and *robotics*, where *reinforcement learning* is used to train large *language models* or *control policies*. The authors suggest that GSPO could be used to improve the **efficiency** and **performance** of *reinforcement learning* algorithms in *real-world applications*, such as *chatbots*, *virtual assistants*, and *autonomous vehicles*.

---

**Authors:** Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, Jingren Zhou, Junyang Lin
