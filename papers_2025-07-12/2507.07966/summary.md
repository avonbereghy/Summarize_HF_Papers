# Scaling RL to Long Videos

**Paper ID:** 2507.07966

**URL:** https://huggingface.co/papers/2507.07966

## Summary

## Executive Summary
The paper introduces a **full-stack framework** for scaling up reasoning in *vision-language models* (VLMs) to long videos, leveraging **reinforcement learning**. This framework addresses the unique challenges of long video reasoning by integrating a **large-scale dataset**, a **two-stage training pipeline**, and a **training infrastructure** for long video RL. The proposed framework, LongVILA-R1, achieves *strong performance* on long video QA benchmarks and demonstrates *consistent performance gains* as the number of input video frames scales.

## Key Contributions and Findings
* **Large-Scale Dataset**: The authors introduce LongVideo-Reason, a *large-scale dataset* comprising 52K long video QA pairs with *high-quality reasoning annotations* across diverse domains.
* **Two-Stage Training Pipeline**: The paper proposes a **two-stage training pipeline** that extends VLMs with *chain-of-thought supervised fine-tuning* (CoT-SFT) and **reinforcement learning** (RL) for long video reasoning.
* **Training Infrastructure**: The authors develop Multi-modal Reinforcement Sequence Parallelism (MR-SP), a **training infrastructure** for long video RL that incorporates *sequence parallelism* and a *vLLM-based engine* tailored for long video.
* **Performance Evaluation**: LongVILA-R1 achieves *strong performance* on long video QA benchmarks, outperforming Video-R1-7B and matching Gemini-1.5-Pro on the LongVideo-Reason-eval benchmark.
* **Efficiency**: The MR-SP system achieves up to **2.1x speedup** on long video RL training, supporting RL training on *hour-long videos* with 3,600 frames or around 256k tokens.

## Methodology Overview
The methodology consists of **three major components**: a **large-scale dataset** (LongVideo-Reason), a **two-stage training pipeline** (CoT-SFT and RL), and a **training infrastructure** (MR-SP). The pipeline uses *chain-of-thought supervised fine-tuning* to pre-train the model, followed by **reinforcement learning** to fine-tune the model for long video reasoning. The MR-SP infrastructure incorporates *sequence parallelism* and a *vLLM-based engine* to efficiently process long videos.

## Results and Performance
The results show that LongVILA-R1 achieves **strong performance** on long video QA benchmarks, with *state-of-the-art results* on VideoMME and LongVideo-Reason-eval. The model outperforms Video-R1-7B and matches Gemini-1.5-Pro on **temporal reasoning**, **goal and purpose reasoning**, **spatial reasoning**, and **plot reasoning** tasks. The MR-SP system also achieves a **2.1x speedup** on long video RL training, demonstrating *efficient scalability*.

## Limitations and Future Work
The paper does not explicitly mention limitations, but potential future directions include:
* Exploring **multi-modal inputs** (e.g., text, audio, and video) for long video reasoning
* Developing **more efficient training infrastructures** for long video RL
* Applying LongVILA-R1 to **real-world applications** such as video analysis, recommendation systems, and autonomous driving

## Practical Applications
The proposed framework has potential **practical applications** in:
* **Video analysis**: LongVILA-R1 can be used for *automated video analysis*, such as object detection, tracking, and recognition.
* **Recommendation systems**: The model can be used to *recommend videos* based on user preferences and viewing history.
* **Autonomous driving**: LongVILA-R1 can be applied to *autonomous driving* tasks, such as scene understanding, object detection, and decision-making.
* **Healthcare**: The framework can be used for *medical video analysis*, such as disease diagnosis and patient monitoring.

---

**Authors:** Yukang Chen, Wei Huang, Baifeng Shi, Qinghao Hu, Hanrong Ye, Ligeng Zhu, Zhijian Liu, Pavlo Molchanov, Jan Kautz, Xiaojuan Qi, Sifei Liu, Hongxu Yin, Yao Lu, Song Han
