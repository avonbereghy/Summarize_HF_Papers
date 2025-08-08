# Group Sequence Policy Optimization

**Paper ID:** 2507.18071

**URL:** https://huggingface.co/papers/2507.18071

## Summary

## Executive Summary
This paper introduces **Group Sequence Policy Optimization (GSPO)**, a novel *reinforcement learning* algorithm designed for training large *language models*. Unlike previous algorithms, GSPO defines the importance ratio based on *sequence likelihood* and performs *sequence-level clipping*, *rewarding*, and *optimization*. The authors demonstrate that GSPO achieves superior **training efficiency** and **performance** compared to existing algorithms, notably stabilizing *Mixture-of-Experts (MoE) RL training*, and has the potential for simplifying the design of *RL infrastructure*. These merits of GSPO have contributed to the remarkable improvements in the latest *Qwen3 models*, showcasing its potential for *real-world applications*.

## Key Contributions and Findings
* **Improved Training Efficiency**: GSPO achieves superior *training efficiency* by defining the importance ratio based on *sequence likelihood* and performing *sequence-level clipping*, *rewarding*, and *optimization*, resulting in *faster convergence* and *better stability*.
* **Stabilization of MoE RL Training**: GSPO notably stabilizes *Mixture-of-Experts (MoE) RL training*, which is a challenging task in *reinforcement learning*, by *reducing the variance* of the importance weights and *improving the exploration-exploitation trade-off*.
* **Simplified RL Infrastructure**: GSPO has the potential for simplifying the design of *RL infrastructure* by *reducing the complexity* of the algorithm and *improving the interpretability* of the results, making it easier to *deploy and maintain* in *real-world applications*.
* **Superior Performance**: GSPO achieves superior **performance** compared to existing algorithms, such as *GRPO*, in terms of *accuracy*, *fluency*, and *coherence*, making it a promising approach for *language model training*.

## Methodology Overview
The methodology of GSPO involves **sequence-level importance sampling**, where the importance ratio is defined based on *sequence likelihood*, and **sequence-level clipping**, *rewarding*, and *optimization* are performed to *stabilize the training process* and *improve the performance*. The authors use **large-scale language models** and *reinforcement learning* frameworks to evaluate the effectiveness of GSPO.

## Results and Performance
The results show that GSPO achieves superior **training efficiency** and **performance** compared to *GRPO*, with *significant improvements* in terms of **accuracy**, **fluency**, and **coherence**. The authors also report that GSPO *stabilizes MoE RL training* and *simplifies the design of RL infrastructure*, making it a promising approach for *language model training*. The results are compared to *state-of-the-art models*, such as *Qwen3 models*, and demonstrate the potential of GSPO for *real-world applications*.

## Limitations and Future Work
The authors mention that GSPO may have limitations in terms of *computational complexity* and *scalability*, and potential future directions include *improving the efficiency* of the algorithm and *applying GSPO to other domains*, such as *computer vision* and *robotics*.

## Practical Applications
GSPO has potential real-world applications in *natural language processing*, such as *language translation*, *text summarization*, and *conversational AI*, where *large-scale language models* are used to generate human-like text. The authors also mention that GSPO can be applied to other domains, such as *computer vision* and *robotics*, where *reinforcement learning* is used to train models to perform complex tasks. The *simplified RL infrastructure* and *improved training efficiency* of GSPO make it a promising approach for *deploying and maintaining* *AI models* in *real-world applications*.

---

**Authors:** Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, Jingren Zhou, Junyang Lin
