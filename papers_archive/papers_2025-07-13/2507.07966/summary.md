# Scaling RL to Long Videos

**Paper ID:** 2507.07966

**URL:** https://huggingface.co/papers/2507.07966

## Summary

## Executive Summary
The paper introduces a **full-stack framework** for scaling up reasoning in *vision-language models* (VLMs) to long videos, leveraging **reinforcement learning**. This framework addresses the unique challenges of long video reasoning by integrating a **large-scale dataset**, a **two-stage training pipeline**, and a **training infrastructure** for long video RL. The proposed framework, **LongVILA-R1-7B**, achieves *strong performance* on long video QA benchmarks and demonstrates *consistent performance gains* as the number of input video frames scales.

## Key Contributions and Findings
* **Large-Scale Dataset**: The paper introduces a large-scale dataset, **LongVideo-Reason**, comprising 52K long video QA pairs with *high-quality reasoning annotations* across diverse domains.
* **Two-Stage Training Pipeline**: The authors propose a two-stage training pipeline that extends VLMs with *chain-of-thought supervised fine-tuning* (CoT-SFT) and **reinforcement learning** (RL).
* **Training Infrastructure**: The paper presents a training infrastructure for long video RL, named **Multi-modal Reinforcement Sequence Parallelism** (MR-SP), which incorporates *sequence parallelism* and a *vLLM-based engine* tailored for long video.
* **Performance Evaluation**: The proposed framework, **LongVILA-R1-7B**, achieves *strong performance* on long video QA benchmarks and outperforms other models, such as **Video-R1-7B** and **Gemini-1.5-Pro**, on certain tasks.
* **Efficiency**: The **MR-SP** system achieves up to *2.1x speedup* on long video RL training, making it more efficient for large-scale video processing.

## Methodology Overview
The methodology consists of **three major components**: a **large-scale dataset**, a **two-stage training pipeline**, and a **training infrastructure**. The **two-stage training pipeline** involves *chain-of-thought supervised fine-tuning* (CoT-SFT) and **reinforcement learning** (RL), while the **training infrastructure** incorporates *sequence parallelism* and a *vLLM-based engine* tailored for long video.

## Results and Performance
The key results show that **LongVILA-R1-7B** achieves **strong performance** on long video QA benchmarks, such as **VideoMME**, and outperforms other models, such as **Video-R1-7B** and **Gemini-1.5-Pro**, on certain tasks, including *temporal reasoning*, *goal and purpose reasoning*, *spatial reasoning*, and *plot reasoning*. The **MR-SP** system also achieves a *2.1x speedup* on long video RL training, demonstrating its efficiency.

## Limitations and Future Work
The paper does not explicitly mention limitations, but potential future directions include:
* Exploring other *modalities*, such as audio and text, for long video reasoning
* Improving the efficiency of the **MR-SP** system for even larger-scale video processing
* Applying the proposed framework to other applications, such as *image and video generation*

## Practical Applications
The proposed framework has potential real-world applications in areas such as:
* **Video analysis and understanding**: The framework can be used to analyze and understand long videos, such as *sports games*, *movies*, and *vlogs*.
* **Autonomous systems**: The framework can be applied to autonomous systems, such as *self-driving cars*, to improve their ability to understand and respond to complex visual scenes.
* **Multimedia processing**: The framework can be used to improve the efficiency and effectiveness of multimedia processing systems, such as *video editing software* and *video streaming platforms*.

---

**Authors:** Yukang Chen, Wei Huang, Baifeng Shi, Qinghao Hu, Hanrong Ye, Ligeng Zhu, Zhijian Liu, Pavlo Molchanov, Jan Kautz, Xiaojuan Qi, Sifei Liu, Hongxu Yin, Yao Lu, Song Han
