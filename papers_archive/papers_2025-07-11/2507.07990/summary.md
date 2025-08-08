# Multi-Granular Spatio-Temporal Token Merging for Training-Free
  Acceleration of Video LLMs

**Paper ID:** 2507.07990

**URL:** https://huggingface.co/papers/2507.07990

## Summary

## Executive Summary
The proposed **Multi-Granular Spatio-Temporal Token Merging** method, named STTM, addresses the quadratic computational scaling issue in **Video Large Language Models (LLMs)** by exploiting *local spatial and temporal redundancy* in video data. This **training-free** approach transforms each frame into *multi-granular spatial tokens* using a *coarse-to-fine search* over a **quadtree structure**, and then performs *directed pairwise merging* across the **temporal dimension**. By doing so, STTM achieves a significant *speed-up* with minimal *accuracy drop*, making it a promising solution for efficient video understanding.

## Key Contributions and Findings
* **Token Merging Methodology**: STTM introduces a novel *decomposed merging approach* that outperforms existing *token reduction methods* across six video QA benchmarks, with a focus on *local spatial and temporal redundancy*.
* **Efficient Computational Scaling**: The proposed method achieves a **2times speed-up** with only a *0.5% accuracy drop* under a *50% token budget*, and a **3times speed-up** with just a *2% drop* under a *30% budget*.
* **Query-Agnostic Cache Reuse**: STTM allows *KV cache reuse* across different questions for the same video, enabling *efficient query processing* and reducing computational overhead.
* **State-of-the-Art Performance**: The method demonstrates *state-of-the-art performance* on six video QA benchmarks, with significant improvements over existing *token reduction methods*.

## Methodology Overview
The STTM methodology consists of two major components: **frame transformation** and **temporal merging**. The *frame transformation* step uses a **quadtree structure** to generate *multi-granular spatial tokens* through a *coarse-to-fine search*. The *temporal merging* step then performs *directed pairwise merging* across the **temporal dimension** to reduce the number of tokens while preserving essential information.

## Results and Performance
The key results show that STTM achieves **2times** and **3times speed-ups** with minimal *accuracy drops* of *0.5%* and *2%*, respectively, under different *token budgets*. The method also demonstrates *state-of-the-art performance* on six video QA benchmarks, outperforming existing *token reduction methods* by a significant margin. The results are compared to *baselines* and *state-of-the-art methods*, highlighting the effectiveness of STTM in reducing computational overhead while maintaining *high accuracy*.

## Limitations and Future Work
The paper does not explicitly mention limitations, but potential future directions include:
* Exploring *alternative token merging strategies* to further improve efficiency and accuracy
* Investigating the application of STTM to *other video understanding tasks* beyond QA benchmarks
* Developing *more sophisticated cache reuse mechanisms* to optimize query processing

## Practical Applications
The proposed STTM method has significant implications for real-world applications, including:
* **Efficient video analysis**: STTM can be used to accelerate video understanding tasks, such as *video question answering*, *object detection*, and *action recognition*, in various industries, including *surveillance*, *healthcare*, and *entertainment*.
* **Improved user experience**: By reducing computational overhead, STTM can enable *faster* and *more efficient* video processing, leading to improved user experience in applications such as *video streaming* and *social media*.

---

**Authors:** Jeongseok Hyun, Sukjun Hwang, Su Ho Han, Taeoh Kim, Inwoong Lee, Dongyoon Wee, Joon-Young Lee, Seon Joo Kim, Minho Shim
