# Traceable Evidence Enhanced Visual Grounded Reasoning: Evaluation and
  Methodology

**Paper ID:** 2507.07999

**URL:** https://huggingface.co/papers/2507.07999

## Summary

## Executive Summary
The paper introduces **TreeBench**, a diagnostic benchmark for evaluating *visual grounded reasoning* capabilities in models, and **TreeVGR**, a training paradigm that supervises localization and reasoning jointly with *reinforcement learning*. The authors propose that **traceable evidence** is key to advancing *vision-grounded reasoning*, and their approach improves performance on several benchmarks, including **V\* Bench** and **MME-RealWorld**. By prioritizing images with *dense objects* and incorporating *manual annotations*, the authors create a challenging benchmark that even the most advanced models struggle with, highlighting the need for more accurate and *explainable* models.

## Key Contributions and Findings
* **Benchmark Development**: The authors create **TreeBench**, a benchmark that evaluates *visual grounded reasoning* capabilities in models, with a focus on *focused visual perception* and *traceable evidence*.
* **Training Paradigm**: The authors introduce **TreeVGR**, a training paradigm that supervises localization and reasoning jointly with *reinforcement learning*, enabling accurate localizations and *explainable reasoning pathways*.
* **Performance Evaluation**: The authors evaluate the performance of **TreeVGR** on several benchmarks, including **V\* Bench**, **MME-RealWorld**, and **TreeBench**, and demonstrate significant improvements in *accuracy* and *explainability*.
* **Methodology**: The authors prioritize images with *dense objects* and incorporate *manual annotations* to create a high-quality benchmark, and use *quality control* stages to ensure the accuracy and consistency of the annotations.
* **Code Availability**: The authors make the code for **TreeVGR** available at https://github.com/Haochen-Wang409/TreeVGR, allowing for easy reproduction and extension of the results.

## Methodology Overview
The methodology involves **benchmark creation**, which includes *image sampling* from **SA-1B**, *manual annotation* of questions, candidate options, and answers, and *quality control* stages to ensure accuracy and consistency. The authors also use **reinforcement learning** to supervise localization and reasoning jointly, and prioritize images with *dense objects* to create a challenging benchmark.

## Results and Performance
The results show that **TreeVGR** improves performance on several benchmarks, including **V\* Bench** (+16.8%), **MME-RealWorld** (+12.6%), and **TreeBench** (+13.4%), demonstrating the effectiveness of the approach. The authors also report that even the most advanced models, such as **OpenAI-o3**, struggle with **TreeBench**, achieving only *54.87% accuracy*, highlighting the need for more accurate and *explainable* models.

## Limitations and Future Work
The authors do not explicitly mention limitations, but potential future directions include:
* Extending the benchmark to include more *diverse* and *complex* scenes
* Improving the *efficiency* and *scalability* of the training paradigm
* Applying the approach to other *domains* and *tasks*

## Practical Applications
The approach has potential practical applications in areas such as:
* **Visual question answering**: The ability to accurately answer questions about images has numerous applications in areas such as *image search*, *image captioning*, and *visual dialogue systems*.
* **Image understanding**: The approach can be used to improve *image understanding* and *scene interpretation*, with applications in areas such as *autonomous driving*, *robotics*, and *surveillance*.
* **Explainable AI**: The focus on *traceable evidence* and *explainable reasoning pathways* can be used to improve the *transparency* and *trustworthiness* of AI systems, with applications in areas such as *healthcare*, *finance*, and *education*.

---

**Authors:** Haochen Wang, Xiangtai Li, Zilong Huang, Anran Wang, Jiacong Wang, Tao Zhang, Jiani Zheng, Sule Bai, Zijian Kang, Jiashi Feng, Zhuochen Wang, Zhaoxiang Zhang
