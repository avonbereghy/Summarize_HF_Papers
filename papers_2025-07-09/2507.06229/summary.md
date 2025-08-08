# Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving

**Paper ID:** 2507.06229

**URL:** https://huggingface.co/papers/2507.06229

## Summary

## Executive Summary
The paper introduces **Agent KB**, a novel hierarchical experience framework that enables complex *agentic problem solving* via a **Reason-Retrieve-Refine** pipeline. This framework addresses a core limitation in traditional agents, which cannot learn from each other's *experiences*. By capturing both high-level **strategies** and detailed *execution logs*, **Agent KB** creates a shared **knowledge base** that enables cross-agent *knowledge transfer*. This leads to improved *success rates* and *generalization* of successful **strategies** to new tasks.

## Key Contributions and Findings
* **Modular Framework**: **Agent KB** provides a modular, framework-agnostic infrastructure for enabling agents to learn from *past experiences* and generalize successful **strategies** to new tasks.
* **Cross-Agent Knowledge Transfer**: The framework enables cross-agent *knowledge transfer* by capturing both high-level **strategies** and detailed *execution logs*, creating a shared **knowledge base**.
* **Improved Success Rates**: **Agent KB** improves *success rates* by up to **16.28 percentage points** on the GAIA benchmark, with significant improvements for *Claude-3* and *GPT-4* on intermediate tasks.
* **Code Repair**: **Agent KB** enables *Claude-3* to improve from **41.33%** to **53.33%** on SWE-bench code repair tasks.
* **Generalization**: The framework allows for *generalization* of successful **strategies** to new tasks, demonstrating its potential for *real-world applications*.

## Methodology Overview
The methodology involves a **hierarchical experience framework** with a novel **Reason-Retrieve-Refine** pipeline, which includes *capturing high-level strategies* and *detailed execution logs*. The framework uses **machine learning** techniques to enable *cross-agent knowledge transfer* and *generalization* of successful **strategies**.

## Results and Performance
The key results show significant improvements in **success rates**, with **Agent KB** outperforming traditional agents by up to **16.28 percentage points** on the GAIA benchmark. *Claude-3* improves from **38.46%** to **57.69%** on the most challenging tasks, while *GPT-4* improves from **53.49%** to **73.26%** on intermediate tasks. On SWE-bench code repair, *Claude-3* improves from **41.33%** to **53.33%**, demonstrating the framework's *effectiveness*.

## Limitations and Future Work
The paper does not explicitly mention limitations, but potential future directions include:
* Exploring the application of **Agent KB** to other *domains* and *tasks*
* Investigating the use of *different machine learning techniques* to improve *knowledge transfer* and *generalization*
* Developing more *efficient* and *scalable* methods for capturing and storing *execution logs*

## Practical Applications
The **Agent KB** framework has potential *real-world applications* in areas such as:
* *Code repair* and *software development*
* *Natural language processing* and *language understanding*
* *Decision-making* and *problem-solving* in complex *domains*
* *Autonomous systems* and *robotics*, where *agents* need to learn from *past experiences* and adapt to new situations.

---

**Authors:** Xiangru Tang, Tianrui Qin, Tianhao Peng, Ziyang Zhou, Daniel Shao, Tingting Du, Xinming Wei, Peng Xia, Fang Wu, He Zhu, Ge Zhang, Jiaheng Liu, Xingyao Wang, Sirui Hong, Chenglin Wu, Hao Cheng, Chi Wang, Wangchunshu Zhou
