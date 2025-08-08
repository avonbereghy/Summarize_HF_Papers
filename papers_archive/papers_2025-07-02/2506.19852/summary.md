# Radial Attention: O(nlog n) Sparse Attention with Energy Decay for
  Long Video Generation

**Paper ID:** 2506.19852

**URL:** https://huggingface.co/papers/2506.19852

## Summary

## Executive Summary
The paper introduces **Radial Attention**, a novel sparse attention mechanism that leverages *Spatiotemporal Energy Decay* in video diffusion models to achieve efficient and high-quality video generation. By translating energy decay into exponentially decaying compute density, **Radial Attention** reduces computational costs, making it possible to generate longer videos with minimal tuning. The proposed method employs a simple, static attention mask, allowing for *pre-trained video diffusion models* to extend their generation length with efficient *LoRA-based fine-tuning*. This approach enables video generation up to *4 times longer* while reducing training costs and accelerating inference.

## Key Contributions and Findings
* **Scalable Attention Mechanism**: The paper proposes **Radial Attention**, a scalable sparse attention mechanism with *O(n log n) complexity*, which is significantly more efficient than standard *O(n^2) dense attention*.
* **Spatiotemporal Energy Decay**: The authors identify a phenomenon termed *Spatiotemporal Energy Decay*, where post-softmax attention scores diminish as spatial and temporal distance between tokens increase, akin to the physical decay of signal or waves over space and time in nature.
* **Efficient Fine-Tuning**: **Radial Attention** allows for efficient *LoRA-based fine-tuning*, enabling pre-trained video diffusion models to extend their generation length with minimal tuning.
* **Improved Performance**: The proposed method achieves up to a *1.9 times speedup* over the original dense attention and enables video generation up to *4 times longer* while reducing training costs and accelerating inference.

## Methodology Overview
The methodology involves **Radial Attention**, which employs a simple, static attention mask where each token attends to *spatially nearby tokens*, with the attention window size shrinking with *temporal distance*. The authors use **video diffusion models** as the foundation and apply *LoRA-based fine-tuning* to extend the generation length of pre-trained models.

## Results and Performance
The key results show that **Radial Attention** maintains video quality across various models, achieving **up to 1.9 times speedup** over the original dense attention. The proposed method enables video generation **up to 4 times longer** while reducing **training costs by up to 4.4 times** and accelerating **inference by up to 3.7 times** compared to dense attention inference.

## Limitations and Future Work
The paper does not explicitly mention limitations, but potential future directions include:
* Exploring the application of **Radial Attention** to other domains, such as image generation or natural language processing
* Investigating the use of **Radial Attention** in combination with other efficient attention mechanisms
* Further optimizing the **Radial Attention** mechanism to improve performance and efficiency

## Practical Applications
The proposed **Radial Attention** mechanism has potential real-world applications in:
* **Video generation**: enabling the creation of longer, high-quality videos with reduced computational costs
* **Computer vision**: improving the efficiency and performance of video-based computer vision tasks, such as object detection or tracking
* **Multimedia processing**: accelerating the processing and analysis of large video datasets, enabling new applications and services in fields like entertainment, education, or surveillance.

---

**Authors:** Xingyang Li, Muyang Li, Tianle Cai, Haocheng Xi, Shuo Yang, Yujun Lin, Lvmin Zhang, Songlin Yang, Jinbo Hu, Kelly Peng, Maneesh Agrawala, Ion Stoica, Kurt Keutzer, Song Han
