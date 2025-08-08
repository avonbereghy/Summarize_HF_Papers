# Multi-Granular Spatio-Temporal Token Merging for Training-Free
  Acceleration of Video LLMs

**Paper ID:** 2507.07990

**URL:** https://huggingface.co/papers/2507.07990

## Summary

## Executive Summary
The proposed method, **STTM** (Spatio-Temporal Token Merging), is a *training-free* approach that accelerates video large language models (LLMs) by reducing the number of *spatio-temporal tokens*. By exploiting *local spatial and temporal redundancy* in video data, **STTM** achieves a significant speed-up with minimal accuracy drop. This is particularly useful for video understanding tasks, where *quadratic computational scaling* with token count can be a major bottleneck. The method's *query-agnostic* nature also allows for **KV cache reuse** across different questions for the same video.

## Key Contributions and Findings
* **Token Reduction Method**: The proposed **STTM** method outperforms existing token reduction methods across six video QA benchmarks, with a *decomposed merging approach* that transforms each frame into *multi-granular spatial tokens*.
* **Speed-Up and Accuracy**: **STTM** achieves a **2-times speed-up** with only a *0.5% accuracy drop* under a 50% token budget, and a **3-times speed-up** with just a *2% drop* under a 30% budget.
* **Query-Agnostic Nature**: The method's *query-agnostic* nature allows for **KV cache reuse** across different questions for the same video, making it more efficient and practical for real-world applications.
* **Local Spatial and Temporal Redundancy**: The proposed method exploits *local spatial and temporal redundancy* in video data, which has been overlooked in prior work, to reduce the number of *spatio-temporal tokens*.
* **Quadtree Structure**: The method uses a *quadtree structure* to perform a *coarse-to-fine search* for *multi-granular spatial tokens*, allowing for more efficient and effective token reduction.

## Methodology Overview
The **STTM** methodology consists of two major components: **token transformation** and **token merging**. The **token transformation** component uses a *quadtree structure* to transform each frame into *multi-granular spatial tokens* using a *coarse-to-fine search*. The **token merging** component then performs *directed pairwise merging* across the temporal dimension to reduce the number of *spatio-temporal tokens*.

## Results and Performance
The proposed **STTM** method achieves significant speed-up with minimal accuracy drop, with **2-times speed-up** and *0.5% accuracy drop* under a 50% token budget, and **3-times speed-up** with *2% drop* under a 30% budget. The method also outperforms existing token reduction methods across six video QA benchmarks, with *state-of-the-art results* in terms of **speed-up** and **accuracy**.

## Limitations and Future Work
The proposed method has some limitations, including the need for further optimization and fine-tuning for specific video understanding tasks. Potential future directions include exploring other *token reduction methods*, improving the *efficiency and effectiveness* of the **STTM** method, and applying the method to other *computer vision tasks*.

## Practical Applications
The proposed **STTM** method has significant practical applications in real-world video understanding tasks, such as *video question answering*, *video object detection*, and *video segmentation*. The method's *query-agnostic* nature and ability to achieve significant speed-up with minimal accuracy drop make it particularly useful for applications where *computational efficiency* and *accuracy* are crucial. Potential applications include *video surveillance*, *autonomous vehicles*, and *healthcare*, where fast and accurate video understanding is essential.

---

**Authors:** Jeongseok Hyun, Sukjun Hwang, Su Ho Han, Taeoh Kim, Inwoong Lee, Dongyoon Wee, Joon-Young Lee, Seon Joo Kim, Minho Shim
