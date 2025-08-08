# Traceable Evidence Enhanced Visual Grounded Reasoning: Evaluation and
  Methodology

**Paper ID:** 2507.07999

**URL:** https://huggingface.co/papers/2507.07999

## Summary

## Executive Summary
The paper introduces **TreeBench**, a diagnostic benchmark for evaluating *visual grounded reasoning* capabilities in models, and **TreeVGR**, a training paradigm that supervises localization and reasoning jointly with *reinforcement learning*. The authors propose that **traceable evidence** is key to advancing *vision-grounded reasoning*, and their results show significant improvements in performance on various benchmarks, including **V\* Bench** and **MME-RealWorld**. The paper highlights the importance of *focused visual perception* and *second-order reasoning* in achieving accurate and explainable results.

## Key Contributions and Findings
* **Benchmark Development**: The authors propose **TreeBench**, a benchmark built on three principles: *focused visual perception*, *traceable evidence*, and *second-order reasoning*, which provides a comprehensive evaluation of *visual grounded reasoning* capabilities.
* **Training Paradigm**: The paper introduces **TreeVGR**, a training paradigm that enables accurate localizations and explainable reasoning pathways by supervising localization and reasoning jointly with *reinforcement learning*.
* **Performance Evaluation**: The results show that **TreeVGR** improves performance on various benchmarks, including **V\* Bench** (+16.8%) and **MME-RealWorld** (+12.6%), and achieves a significant improvement on **TreeBench** (+13.4%).
* **Model Comparison**: The authors compare the performance of various models, including **OpenAI-o3**, which scores only 54.87% on **TreeBench**, highlighting the challenges of *visual grounded reasoning*.
* **Code Availability**: The code for **TreeVGR** is made available at https://github.com/Haochen-Wang409/TreeVGR, allowing for further research and development.

## Methodology Overview
The methodology involves **benchmark construction**, which includes sampling 1K high-quality images from **SA-1B** and manually annotating questions, candidate options, and answers using *eight LMM experts*. The **TreeVGR** training paradigm consists of **joint supervision** of localization and reasoning using *reinforcement learning*, which enables accurate localizations and explainable reasoning pathways.

## Results and Performance
The results show significant improvements in performance on various benchmarks, with **TreeVGR** achieving **54.87%** accuracy on **TreeBench**, outperforming other models, including **OpenAI-o3**. The results also show improvements on **V\* Bench** (+16.8%) and **MME-RealWorld** (+12.6%), demonstrating the effectiveness of **TreeVGR** in advancing *vision-grounded reasoning*. The performance is compared to other models, highlighting the *state-of-the-art* results achieved by **TreeVGR**.

## Limitations and Future Work
The paper mentions that the current **TreeBench** benchmark consists of only 405 challenging visual question-answering pairs, which may not be sufficient to comprehensively evaluate *visual grounded reasoning* capabilities. Future work may involve expanding the benchmark to include more images and questions, as well as exploring other *techniques* and *methods* to further improve performance.

## Practical Applications
The paper has significant implications for real-world applications, such as *visual question answering*, *image captioning*, and *human-computer interaction*. The development of **TreeBench** and **TreeVGR** can lead to more accurate and explainable results in these applications, enabling more effective *decision-making* and *problem-solving*. The paper also highlights the potential for *visual grounded reasoning* to be used in various fields, including *healthcare*, *education*, and *entertainment*.

---

**Authors:** Haochen Wang, Xiangtai Li, Zilong Huang, Anran Wang, Jiacong Wang, Tao Zhang, Jiani Zheng, Sule Bai, Zijian Kang, Jiashi Feng, Zhuochen Wang, Zhaoxiang Zhang
