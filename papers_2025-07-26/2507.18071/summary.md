# Group Sequence Policy Optimization

**Paper ID:** 2507.18071

**URL:** https://huggingface.co/papers/2507.18071

## Summary

## Executive Summary
This paper introduces **Group Sequence Policy Optimization (GSPO)**, a novel *reinforcement learning* algorithm designed for training large *language models*. Unlike previous algorithms, GSPO defines the importance ratio based on *sequence likelihood* and performs *sequence-level clipping*, *rewarding*, and *optimization*. The authors demonstrate that GSPO achieves superior **training efficiency** and **performance** compared to existing algorithms, notably stabilizing *Mixture-of-Experts (MoE) RL training*. The merits of GSPO have contributed to remarkable improvements in the latest *Qwen3 models*, showcasing its potential for simplifying *RL infrastructure* design.

## Key Contributions and Findings
* **Improved Training Efficiency**: GSPO achieves superior *training speed* and *stability* compared to existing algorithms, making it an attractive choice for large-scale *language model* training.
* **Stabilized MoE RL Training**: GSPO notably stabilizes *Mixture-of-Experts (MoE) RL training*, which is a challenging task in *reinforcement learning*.
* **Simplified RL Infrastructure**: The authors suggest that GSPO has the potential to simplify the design of *RL infrastructure*, making it easier to implement and deploy *reinforcement learning* algorithms.
* **Superior Performance**: GSPO demonstrates superior **performance** compared to existing algorithms, including the *GRPO algorithm*, in terms of *training efficiency* and *model accuracy*.
* **Sequence-Level Optimization**: GSPO performs *sequence-level clipping*, *rewarding*, and *optimization*, which is a key distinction from previous algorithms that adopt *token-level importance ratios*.

## Methodology Overview
The methodology of GSPO involves **sequence likelihood** calculation and **sequence-level clipping**, which are used to define the importance ratio. The authors employ *reinforcement learning* techniques, including *policy optimization*, to train large *language models*. The **GSPO algorithm** consists of several major components, including *sequence encoding*, *importance ratio calculation*, and *policy optimization*, which are combined to achieve efficient and stable training.

## Results and Performance
The authors report significant improvements in **training efficiency** and **model accuracy** using GSPO compared to existing algorithms. Specifically, GSPO achieves superior **performance** in terms of *training speed* and *stability*, with *remarkable improvements* in the latest *Qwen3 models*. The results demonstrate that GSPO outperforms the *GRPO algorithm* in terms of **training efficiency** and **model accuracy**, with *notable improvements* in *Mixture-of-Experts (MoE) RL training*.

## Limitations and Future Work
The authors do not explicitly mention any limitations of the GSPO algorithm. However, potential future directions may include:
* Exploring the application of GSPO to other *reinforcement learning* tasks beyond *language model* training.
* Investigating the use of GSPO in combination with other *reinforcement learning* algorithms to further improve **training efficiency** and **performance**.
* Developing more efficient and scalable implementations of the GSPO algorithm to support large-scale *language model* training.

## Practical Applications
The GSPO algorithm has significant potential for practical applications in *natural language processing* and *reinforcement learning*. Some potential real-world applications include:
* **Language Model Training**: GSPO can be used to train large *language models* more efficiently and effectively, leading to improved *model accuracy* and **performance**.
* **Chatbots and Virtual Assistants**: GSPO can be applied to train *chatbots* and *virtual assistants* to better understand and respond to user input.
* **Text Generation**: GSPO can be used to improve *text generation* tasks, such as *language translation* and *text summarization*.

---

**Authors:** Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, Jingren Zhou, Junyang Lin
