# Traceable Evidence Enhanced Visual Grounded Reasoning: Evaluation and
  Methodology

**Paper ID:** 2507.07999

**URL:** https://huggingface.co/papers/2507.07999

## Summary

## Executive Summary
The paper introduces **TreeBench**, a diagnostic benchmark for evaluating *visual grounded reasoning* capabilities in models, and **TreeVGR**, a training paradigm that supervises localization and reasoning jointly with *reinforcement learning*. The authors propose that **traceable evidence** is key to advancing *vision-grounded reasoning*, and their approach improves performance on several benchmarks, including *V\* Bench*, *MME-RealWorld*, and **TreeBench**. The paper highlights the importance of *focused visual perception*, *traceable evidence*, and *second-order reasoning* in evaluating and improving *visual grounded reasoning* models.

## Key Contributions and Findings
* **Benchmark Development**: The authors develop **TreeBench**, a benchmark that evaluates *visual grounded reasoning* capabilities in models, with a focus on *dense objects* and *complex scenes*.
* **Training Paradigm**: The authors introduce **TreeVGR**, a training paradigm that uses *reinforcement learning* to supervise localization and reasoning jointly, enabling *accurate localizations* and *explainable reasoning pathways*.
* **Performance Improvement**: The authors demonstrate that **TreeVGR** improves performance on several benchmarks, including *V\* Bench* (+16.8%), *MME-RealWorld* (+12.6%), and **TreeBench** (+13.4%), highlighting the importance of *traceable evidence* in advancing *vision-grounded reasoning*.
* **Evaluation Methodology**: The authors propose a three-stage quality control process to ensure the quality of the benchmark, including *manual annotation* and *expert evaluation*.
* **Model Evaluation**: The authors evaluate several state-of-the-art models, including **OpenAI-o3**, on the **TreeBench** benchmark, highlighting the challenges of *visual grounded reasoning* and the need for improved models.

## Methodology Overview
The methodology involves **benchmark development**, with a focus on *dense objects* and *complex scenes*, and **training paradigm development**, using *reinforcement learning* to supervise localization and reasoning jointly. The authors use **manual annotation** and **expert evaluation** to ensure the quality of the benchmark, and employ *specific techniques* such as *bounding box evaluation* to assess model performance.

## Results and Performance
The results show that **TreeVGR** improves performance on several benchmarks, with **bold** metrics including +16.8% on *V\* Bench*, +12.6% on *MME-RealWorld*, and +13.4% on **TreeBench**. The authors also report that *state-of-the-art models* struggle with the **TreeBench** benchmark, with *OpenAI-o3* scoring only 54.87%, highlighting the challenges of *visual grounded reasoning*.

## Limitations and Future Work
The authors mention that the **TreeBench** benchmark is limited to 405 images, and that future work could involve expanding the benchmark to include more images and *diverse scenarios*. Additionally, the authors suggest that future work could focus on improving the **TreeVGR** training paradigm to achieve even better performance.

## Practical Applications
The paper has potential real-world applications in areas such as *computer vision*, *robotics*, and *human-computer interaction*, where *visual grounded reasoning* is critical. The **TreeBench** benchmark and **TreeVGR** training paradigm could be used to improve models for tasks such as *image captioning*, *visual question answering*, and *object detection*, leading to more accurate and *explainable* models.

---

**Authors:** Haochen Wang, Xiangtai Li, Zilong Huang, Anran Wang, Jiacong Wang, Tao Zhang, Jiani Zheng, Sule Bai, Zijian Kang, Jiashi Feng, Zhuochen Wang, Zhaoxiang Zhang
