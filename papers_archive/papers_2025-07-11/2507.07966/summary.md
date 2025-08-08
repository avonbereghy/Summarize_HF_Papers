# Scaling RL to Long Videos

**Paper ID:** 2507.07966

**URL:** https://huggingface.co/papers/2507.07966

## Summary

## Executive Summary
The paper introduces a **full-stack framework** for scaling up reasoning in *vision-language models* (VLMs) to long videos, leveraging **reinforcement learning**. This framework addresses the unique challenges of long video reasoning by integrating a **large-scale dataset**, a **two-stage training pipeline**, and a **training infrastructure** for long video RL. The proposed framework, **LongVILA-R1-7B**, achieves *strong performance* on long video QA benchmarks and demonstrates *consistent performance gains* as the number of input video frames scales.

## Key Contributions and Findings
* **Large-Scale Dataset**: The authors introduce a *large-scale dataset*, LongVideo-Reason, comprising 52K long video QA pairs with *high-quality reasoning annotations* across diverse domains.
* **Two-Stage Training Pipeline**: The paper proposes a **two-stage training pipeline** that extends VLMs with *chain-of-thought supervised fine-tuning* (CoT-SFT) and **reinforcement learning** (RL).
* **Training Infrastructure**: The authors develop a **training infrastructure** for long video RL, named Multi-modal Reinforcement Sequence Parallelism (MR-SP), which incorporates *sequence parallelism* and a *vLLM-based engine* tailored for long video.
* **Performance Evaluation**: The proposed framework, LongVILA-R1-7B, achieves *strong performance* on long video QA benchmarks and outperforms other models, such as Video-R1-7B and Gemini-1.5-Pro, on the LongVideo-Reason-eval benchmark.
* **Efficiency**: The MR-SP system achieves up to *2.1x speedup* on long video RL training, demonstrating its *efficiency* and *scalability*.

## Methodology Overview
The methodology involves **three major components**: a **large-scale dataset**, a **two-stage training pipeline**, and a **training infrastructure**. The **two-stage training pipeline** consists of *chain-of-thought supervised fine-tuning* (CoT-SFT) and **reinforcement learning** (RL). The **training infrastructure**, MR-SP, incorporates *sequence parallelism* and a *vLLM-based engine* tailored for long video, using *cached video embeddings* for efficient rollout and prefilling.

## Results and Performance
The key results show that LongVILA-R1-7B achieves **strong performance** on long video QA benchmarks, such as VideoMME, and outperforms other models, such as Video-R1-7B and Gemini-1.5-Pro, on the LongVideo-Reason-eval benchmark. The results also demonstrate *consistent performance gains* as the number of input video frames scales, with a **2.1x speedup** on long video RL training using the MR-SP system. The performance is evaluated using *temporal reasoning*, *goal and purpose reasoning*, *spatial reasoning*, and *plot reasoning* metrics.

## Limitations and Future Work
The paper does not explicitly mention limitations, but potential future directions include:
* Exploring other *modalities*, such as audio and image, for RL training
* Applying the proposed framework to other *domains* and *tasks*
* Investigating the *efficacy* of the MR-SP system on other models and datasets

## Practical Applications
The proposed framework has potential real-world applications in:
* **Video analysis** and *understanding*, such as video summarization and video question answering
* **Multimedia processing**, such as image and video generation
* **Human-computer interaction**, such as video-based dialogue systems and human-robot interaction
* **Education** and *entertainment*, such as interactive video-based learning platforms and video games.

---

**Authors:** Yukang Chen, Wei Huang, Baifeng Shi, Qinghao Hu, Hanrong Ye, Ligeng Zhu, Zhijian Liu, Pavlo Molchanov, Jan Kautz, Xiaojuan Qi, Sifei Liu, Hongxu Yin, Yao Lu, Song Han
