# Mono-InternVL-1.5: Towards Cheaper and Faster Monolithic Multimodal
  Large Language Models

**Paper ID:** 2507.12566

**URL:** https://huggingface.co/papers/2507.12566

## Summary

## Executive Summary
This paper introduces **Mono-InternVL-1.5**, a *state-of-the-art* monolithic Multimodal Large Language Model (MLLM) that integrates visual encoding and language decoding into a single model. The key idea is to embed a new visual parameter space into a pre-trained LLM, enabling stable learning of visual knowledge from *noisy data* via **delta tuning**. This approach addresses the challenges of unstable optimization and catastrophic forgetting in existing MLLMs, leading to a cheaper and faster model with competitive performance.

## Key Contributions and Findings
* **Model Architecture**: The authors propose **Mono-InternVL**, an advanced monolithic MLLM that incorporates a set of visual experts through a *multimodal mixture-of-experts architecture*, allowing for efficient learning of visual knowledge.
* **Pre-training Strategy**: The paper introduces **Endogenous Visual Pre-training (EViP)**, an innovative pre-training strategy that maximizes the visual capabilities of Mono-InternVL via *progressive learning*, and its improved version **EViP++**.
* **Efficient Inference**: The authors design a **fused CUDA kernel** to speed up the MoE operations during inference, reducing the training and inference costs of Mono-InternVL-1.5.
* **Competitive Performance**: The results demonstrate that Mono-InternVL outperforms existing monolithic MLLMs on *12 out of 15 benchmarks*, with a significant improvement of +114-point over Emu3 on OCRBench.

## Methodology Overview
The methodology involves **pre-training** a large language model and then embedding a new visual parameter space into it using **delta tuning**. The **multimodal mixture-of-experts architecture** is used to incorporate visual experts, and the **EViP** and **EViP++** strategies are employed to maximize the visual capabilities of the model. The authors also utilize *progressive learning* and *efficient inference techniques*, such as the **fused CUDA kernel**, to reduce the training and inference costs.

## Results and Performance
The results show that Mono-InternVL-1.5 achieves **competitive performance** with Mono-InternVL, while reducing the **training cost** and **inference cost**. The model outperforms existing monolithic MLLMs on *12 out of 15 benchmarks*, with a significant improvement in **first-token latency** of up to *69%* compared to its modular counterpart, InternVL-1.5.

## Limitations and Future Work
The paper mentions that Mono-InternVL-1.5 still has a relatively *high data cost*, which could be a limitation. Potential future directions include exploring ways to further reduce the data cost and improving the performance of the model on *low-resource benchmarks*.

## Practical Applications
The proposed **Mono-InternVL-1.5** model has potential real-world applications in *multimodal tasks*, such as *visual question answering*, *image captioning*, and *text-based image retrieval*. The model's ability to efficiently learn visual knowledge and reduce inference costs makes it a promising solution for *real-time applications* and *edge devices*. Additionally, the model's *competitive performance* and *low latency* make it suitable for applications that require *fast and accurate* multimodal processing, such as *virtual assistants* and *human-computer interaction systems*.

---

**Authors:** Gen Luo, Wenhan Dou, Wenhao Li, Zhaokai Wang, Xue Yang, Changyao Tian, Hao Li, Weiyun Wang, Wenhai Wang, Xizhou Zhu, Yu Qiao, Jifeng Dai
