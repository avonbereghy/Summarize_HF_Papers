# LeanK: Learnable K Cache Channel Pruning for Efficient Decoding

**Paper ID:** 2508.02215

**Authors:** Yike Zhang, Zhiyuan He, Huiqiang Jiang, Chengruidong Zhang, Yuqing Yang, Jianyong Wang, Lili Qiu

**URL:** https://huggingface.co/papers/2508.02215

## Summary

## Executive Summary

This paper introduces **LeanK**, a *learning-based method* for pruning the key (K) cache in large language models (LLMs) to improve decoding efficiency.  By leveraging *static channel sparsity* and a *novel two-stage training process*, LeanK learns a *channel-wise mask* to remove unimportant K cache channels, achieving significant memory reduction (*up to 70% K cache and 16-18% V cache*) and a *1.3x speedup* in attention computation without compromising accuracy.  The learned importance distribution provides valuable insights into model channels and attention heads during long-context inference.

## Key Contributions and Findings

* **Learnable K Cache Pruning:** LeanK introduces a novel *learning-based approach* to prune the K cache, unlike traditional heuristic methods.  This allows for *data-driven optimization* of sparsity.

* **Two-Stage Training Process:** A *two-stage training process* ensures the learned sparsity pattern satisfies both *specific sparsity ratios* and *hardware alignment requirements*, maximizing efficiency gains.

* **Significant Memory Reduction and Speedup:**  LeanK achieves *substantial memory reductions* in both K and V caches (*up to 70% and 16-18%, respectively*) and a *1.3x speedup* in attention computation.

* **Insights into Model Channels:** The learned importance distribution offers valuable *insights into the importance of different channels and attention heads* during long-context inference, aiding model understanding and optimization.

* **Open-Source Code Availability:** The authors provide *open-source code*, facilitating reproducibility and further research.


## Methodology Overview

LeanK employs a **two-stage training process**.  The *first stage* trains the LLM normally. The *second stage* uses a *learned mask* to prune unimportant K cache channels. This mask is learned by minimizing a *loss function* that balances accuracy and sparsity.  A *custom decoding kernel* is then implemented to leverage the pruned cache for faster attention computation.  The *sparsity ratio* and *hardware alignment* are considered during mask learning.

## Results and Performance

LeanK demonstrates *significant improvements* in both memory usage and decoding speed.  **K cache memory reduction** reached *up to 70%*, while **V cache memory reduction** was *16-18%*.  The **speedup in attention computation** was *1.3x*.  Importantly, these gains were achieved *without significant accuracy loss*.

## Limitations and Future Work

A limitation is that the effectiveness of LeanK might depend on the specific LLM architecture and task. Future work could explore *adaptive pruning strategies* that dynamically adjust sparsity based on the input sequence length or context.  Investigating the impact of LeanK on different LLM architectures and tasks is also warranted.

## Practical Applications

LeanK has significant implications for deploying LLMs on resource-constrained devices.  The *reduced memory footprint* and *increased speed* enable efficient processing of long-context tasks on *mobile devices and edge servers*, expanding the accessibility and applicability of LLMs in various domains.  This could lead to advancements in applications requiring real-time processing of long sequences, such as *chatbots, machine translation, and question answering systems*.