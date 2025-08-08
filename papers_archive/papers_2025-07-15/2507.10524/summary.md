# Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive
  Token-Level Computation

**Paper ID:** 2507.10524

**URL:** https://huggingface.co/papers/2507.10524

## Summary

## Executive Summary
The paper introduces **Mixture-of-Recursions (MoR)**, a unified framework that combines **parameter efficiency** and **adaptive computation** to improve the performance of language models. By reusing a shared stack of layers across recursion steps and using lightweight routers to dynamically assign recursion depths to individual tokens, MoR achieves *significant reductions in computational and memory demands*. This allows MoR to focus *quadratic attention computation* only among tokens still active at a given recursion depth, further improving *memory access efficiency*. The authors demonstrate that MoR forms a new *Pareto frontier*, achieving higher quality without incurring large-model costs.

## Key Contributions and Findings
* **Unified Framework**: MoR combines **parameter sharing** and **adaptive computation** to achieve both efficiency and effectiveness in language models, allowing for *dynamic recursive depths* and *adaptive token-level computation*.
* **Recursive Transformer**: The authors propose a **Recursive Transformer** architecture that reuses a shared stack of layers across recursion steps, enabling *parameter efficiency* and *reduced memory footprint*.
* **KV Sharing Variant**: MoR also introduces a *KV sharing variant* that reuses key-value pairs from the first recursion, specifically designed to *decrease prefill latency* and *memory footprint*.
* **Performance Gains**: The authors demonstrate that MoR achieves *significant improvements in validation perplexity* and *few-shot accuracy*, while delivering *higher throughput* compared to vanilla and existing recursive baselines.
* **Scalability**: MoR is shown to be effective across model scales ranging from **135M to 1.7B parameters**, making it a promising approach for large-scale language modeling.

## Methodology Overview
The methodology involves **Mixture-of-Recursions (MoR)**, which combines **parameter sharing** and **adaptive computation** using a **Recursive Transformer** architecture. The authors employ *lightweight routers* to dynamically assign recursion depths to individual tokens, allowing for *adaptive token-level computation*. The **KV sharing variant** is also used to reuse key-value pairs from the first recursion, reducing *prefill latency* and *memory footprint*.

## Results and Performance
The authors report **significant improvements in validation perplexity** and **few-shot accuracy**, with MoR achieving *state-of-the-art results* across model scales. In terms of **throughput**, MoR delivers *higher performance* compared to vanilla and existing recursive baselines. The results demonstrate that MoR forms a new *Pareto frontier*, achieving higher quality without incurring large-model costs, with **equal training FLOPs** and *smaller model sizes*.

## Limitations and Future Work
The authors do not explicitly mention limitations, but potential future directions include:
* Exploring the application of MoR to other *natural language processing tasks*
* Investigating the use of MoR in *multimodal learning* scenarios
* Developing more efficient *routing mechanisms* for adaptive computation

## Practical Applications
The proposed **Mixture-of-Recursions (MoR)** framework has potential practical applications in:
* **Language modeling**: MoR can be used to improve the performance of language models, enabling more efficient and effective *text generation* and *language understanding*.
* **Conversational AI**: MoR can be applied to conversational AI systems, allowing for more *efficient* and *effective* dialogue management and response generation.
* **Natural language processing**: MoR can be used in a variety of NLP tasks, such as *sentiment analysis*, *question answering*, and *machine translation*, enabling more accurate and efficient processing of *large datasets*.

---

**Authors:** Sangmin Bae, Yujin Kim, Reza Bayat, Sungnyun Kim, Jiyoun Ha, Tal Schuster, Adam Fisch, Hrayr Harutyunyan, Ziwei Ji, Aaron Courville, Se-Young Yun
