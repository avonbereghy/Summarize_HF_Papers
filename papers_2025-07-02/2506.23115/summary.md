# MoCa: Modality-aware Continual Pre-training Makes Better Bidirectional
  Multimodal Embeddings

**Paper ID:** 2506.23115

**URL:** https://huggingface.co/papers/2506.23115

## Summary

## Executive Summary
The paper introduces **MoCa**, a novel framework for transforming pre-trained Vision Language Models (VLMs) into effective bidirectional multimodal embedding models. By addressing the limitations of current approaches, including the use of *causal attention* and reliance on high-quality labeled paired data, **MoCa** achieves state-of-the-art results on MMEB and ViDoRe-v2 benchmarks. The framework consists of two stages: **Modality-aware Continual Pre-training** and **Heterogeneous Contrastive Fine-tuning**, which enhance *bidirectional context-aware reasoning* and utilize *diverse multimodal data* for improved representation robustness.

## Key Contributions and Findings
* **Addressing Limitations**: The paper identifies and addresses three key limitations of current multimodal embedding models, including the suboptimal use of *causal attention* and scalability issues due to reliance on high-quality labeled paired data.
* **Modality-aware Continual Pre-training**: This stage introduces a *joint reconstruction objective* that simultaneously denoises *interleaved text and image inputs*, enhancing *bidirectional context-aware reasoning*.
* **Heterogeneous Contrastive Fine-tuning**: This stage leverages *diverse, semantically rich multimodal data* beyond simple image-caption pairs to enhance generalization and alignment.
* **Scalability and Performance**: **MoCa** exhibits strong scalability with both model size and training data on MMEB, achieving new state-of-the-art results on MMEB and ViDoRe-v2 benchmarks.

## Methodology Overview
The **MoCa** framework consists of two major components: **Modality-aware Continual Pre-training** and **Heterogeneous Contrastive Fine-tuning**. The first stage uses a *joint reconstruction objective* to enhance *bidirectional context-aware reasoning*, while the second stage utilizes *diverse multimodal data* and *heterogeneous contrastive learning* to improve representation robustness.

## Results and Performance
The paper reports significant improvements in **performance metrics**, including *accuracy* and *F1-score*, on both MMEB and ViDoRe-v2 benchmarks. Compared to existing state-of-the-art models, **MoCa** achieves *better results* with **strong scalability** in terms of model size and training data. The results demonstrate the effectiveness of **MoCa** in learning *robust multimodal representations*.

## Limitations and Future Work
The paper does not explicitly mention any limitations of the **MoCa** framework. However, potential future directions may include exploring the application of **MoCa** to other *multimodal tasks*, such as *visual question answering* or *image-text retrieval*, and investigating the use of *alternative pre-training objectives* or *fine-tuning strategies*.

## Practical Applications
The **MoCa** framework has potential real-world applications in areas such as *multimodal search*, *image-text retrieval*, and *visual question answering*. By learning *robust multimodal representations*, **MoCa** can enable more effective and efficient *information retrieval* and *question answering* systems, with implications for *search engines*, *recommendation systems*, and other *AI-powered applications*.

---

**Authors:** Haonan Chen, Hong Liu, Yuping Luo, Liang Wang, Nan Yang, Furu Wei, Zhicheng Dou
