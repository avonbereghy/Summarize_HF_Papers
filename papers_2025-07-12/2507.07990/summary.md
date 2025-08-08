# Multi-Granular Spatio-Temporal Token Merging for Training-Free
  Acceleration of Video LLMs

**Paper ID:** 2507.07990

**URL:** https://huggingface.co/papers/2507.07990

## Summary

## Executive Summary
The proposed **Multi-Granular Spatio-Temporal Token Merging** method, named STTM, addresses the quadratic computational scaling issue in **Video Large Language Models (LLMs)** by exploiting *local spatial and temporal redundancy* in video data. This **training-free** approach transforms each frame into *multi-granular spatial tokens* using a *coarse-to-fine search* over a **quadtree structure**, and then performs *directed pairwise merging* across the **temporal dimension**. By doing so, STTM achieves a significant *speed-up* with minimal *accuracy drop*, making it a promising solution for efficient video understanding.

## Key Contributions and Findings
* **Token Merging Methodology**: STTM introduces a novel *decomposed merging approach* that outperforms existing *token reduction methods* across six video QA benchmarks.
* **Efficient Computational Scaling**: The proposed method achieves a **2times speed-up** with only a *0.5% accuracy drop* under a *50% token budget*, and a **3times speed-up** with just a *2% drop* under a *30% budget*.
* **Query-Agnostic Cache Reuse**: STTM allows *KV cache reuse* across different questions for the same video, enabling *efficient querying* and *reduced computational overhead*.
* **Improved Video Understanding**: The method demonstrates strong *video understanding* capabilities, leveraging *spatio-temporal tokens* to capture complex video dynamics.
* **Flexibility and Scalability**: STTM can be applied to various video analysis tasks, making it a *versatile* and *scalable* solution for real-world applications.

## Methodology Overview
The STTM methodology consists of two major components: **frame transformation** and **temporal merging**. The *frame transformation* step uses a **quadtree structure** to generate *multi-granular spatial tokens*, while the *temporal merging* step performs *directed pairwise merging* across the **temporal dimension** using a *coarse-to-fine search* approach.

## Results and Performance
The results show that STTM achieves **state-of-the-art performance** on six video QA benchmarks, with a significant *speed-up* compared to existing methods. The method demonstrates a **2times speed-up** with only a *0.5% accuracy drop* under a *50% token budget*, and a **3times speed-up** with just a *2% drop* under a *30% budget*. These results highlight the effectiveness of STTM in reducing computational overhead while maintaining *strong video understanding* capabilities.

## Limitations and Future Work
The paper does not explicitly mention any limitations, but potential future directions include:
* Exploring the application of STTM to other video analysis tasks, such as *object detection* and *segmentation*
* Investigating the use of *alternative merging strategies* to further improve efficiency and accuracy
* Developing *more advanced cache reuse mechanisms* to optimize querying efficiency

## Practical Applications
The proposed STTM method has significant implications for real-world applications, including:
* **Efficient video analysis**: STTM can be used to accelerate video understanding tasks, such as *video question answering* and *video captioning*
* **Improved user experience**: By reducing computational overhead, STTM can enable *faster* and *more efficient* video analysis, leading to a better user experience
* **Increased scalability**: The method's ability to handle large volumes of video data makes it an attractive solution for *large-scale video analysis* applications, such as *surveillance* and *content moderation*

---

**Authors:** Jeongseok Hyun, Sukjun Hwang, Su Ho Han, Taeoh Kim, Inwoong Lee, Dongyoon Wee, Joon-Young Lee, Seon Joo Kim, Minho Shim
