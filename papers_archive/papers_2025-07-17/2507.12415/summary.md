# SWE-Perf: Can Language Models Optimize Code Performance on Real-World
  Repositories?

**Paper ID:** 2507.12415

**URL:** https://huggingface.co/papers/2507.12415

## Summary

## Executive Summary
The paper introduces **SWE-Perf**, a benchmark designed to evaluate the capability of *Large Language Models (LLMs)* in optimizing code performance at the repository level. The authors aim to address the gap in existing research by systematically assessing *LLMs* on **code performance optimization tasks** within authentic repository contexts. The study reveals a substantial capability gap between existing *LLMs* and **expert-level optimization performance**, highlighting critical research opportunities in this emerging field. The benchmark comprises 140 carefully curated instances derived from *performance-improving pull requests* from popular GitHub repositories, providing a comprehensive evaluation of representative methods.

## Key Contributions and Findings
* **Benchmark Development**: The authors introduce **SWE-Perf**, the first benchmark specifically designed to evaluate *LLMs* on **code performance optimization tasks**. This benchmark comprises 140 carefully curated instances, each derived from *performance-improving pull requests* from popular GitHub repositories.
* **Evaluation of LLMs**: The study evaluates representative *LLMs* using **file-level and repo-level approaches**, such as *Agentless* and *OpenHands*, to reveal their capabilities in optimizing code performance.
* **Capability Gap Identification**: The authors identify a substantial capability gap between existing *LLMs* and **expert-level optimization performance**, highlighting critical research opportunities in this emerging field.
* **Research Opportunities**: The study highlights the need for further research in *code performance optimization* using *LLMs*, emphasizing the importance of developing more effective methods to bridge the capability gap.
* **Practical Implications**: The findings have significant implications for *real-world software engineering*, where **code performance optimization** is critical for production-level systems.

## Methodology Overview
The methodology involves **benchmark development**, where the authors carefully curate 140 instances from *performance-improving pull requests* from popular GitHub repositories. Each instance includes the relevant *codebase*, *target functions*, *performance-related tests*, *expert-authored patches*, and *executable environments*. The authors then evaluate representative *LLMs* using **file-level and repo-level approaches**, such as *Agentless* and *OpenHands*, to assess their capabilities in optimizing code performance.

## Results and Performance
The study reveals a substantial capability gap between existing *LLMs* and **expert-level optimization performance**, with **metrics** such as *execution time* and *memory usage* showing significant differences. The results show that *LLMs* can optimize code performance, but their capabilities are limited compared to **expert-level optimization**. The authors also provide *comparisons* between different *LLMs* and **optimization approaches**, highlighting the strengths and weaknesses of each method.

## Limitations and Future Work
The study mentions several limitations, including the limited size of the benchmark and the focus on specific *programming languages*. Potential future directions include:
* Expanding the benchmark to include more instances and *programming languages*
* Developing more effective *LLMs* that can bridge the capability gap
* Investigating the application of *LLMs* in other areas of *software engineering*, such as *code generation* and *bug fixing*

## Practical Applications
The findings have significant implications for *real-world software engineering*, where **code performance optimization** is critical for production-level systems. Potential practical applications include:
* Using *LLMs* to optimize code performance in *production environments*
* Developing more effective *code optimization tools* that leverage *LLMs*
* Improving the overall quality and efficiency of *software development* by leveraging *LLMs* in **code performance optimization** and other areas of *software engineering*.

---

**Authors:** Xinyi He, Qian Liu, Mingzhe Du, Lin Yan, Zhijie Fan, Yiming Huang, Zejian Yuan, Zejun Ma
