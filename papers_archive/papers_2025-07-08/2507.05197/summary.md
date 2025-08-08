# Pre-Trained Policy Discriminators are General Reward Models

**Paper ID:** 2507.05197

**URL:** https://huggingface.co/papers/2507.05197

## Summary

## Executive Summary
The paper **Pre-Trained Policy Discriminators are General Reward Models** introduces a novel approach to *reward modeling* by formulating it as a **policy discriminator**, which quantifies the difference between two policies to generate a *reward signal*. The proposed method, **Policy Discriminative Learning (POLAR)**, trains a *reward model* to discern identical policies and discriminate different ones, capturing the *relative difference* between one policy and an arbitrary target policy. This approach has shown to substantially outperform traditional non-pre-trained methods, enhancing *reward model* performance and demonstrating robust *generalization capabilities*.

## Key Contributions and Findings
* **Novel Reward Modeling Approach**: The paper proposes a new perspective on *reward modeling* by formulating it as a **policy discriminator**, which quantifies the difference between two policies to generate a *reward signal*.
* **Policy Discriminative Learning (POLAR)**: The authors introduce **POLAR**, a scalable pre-training method that trains a *reward model* to discern identical policies and discriminate different ones, capturing the *relative difference* between one policy and an arbitrary target policy.
* **Improved Performance**: The paper demonstrates that **POLAR** substantially outperforms traditional non-pre-trained methods, significantly enhancing *reward model* performance and providing reliable *reward signals*.
* **Robust Generalization Capabilities**: The authors show that **POLAR** exhibits robust *generalization capabilities* in *Reinforcement Learning from Human Feedback (RLHF)* using *Reinforcement Fine-tuning (RFT)*.
* **Scaling Properties**: The paper reveals a clear *power-law relationship* between computation and performance, supported by linear correlation coefficients approaching 0.99.

## Methodology Overview
The methodology consists of **Policy Discriminative Learning (POLAR)**, which involves training a *reward model* to discern identical policies and discriminate different ones using *relative difference* as a *high-level optimization objective*. The approach leverages *pre-training* to develop a scalable and general *reward model*.

## Results and Performance
The key results show that **POLAR** substantially outperforms traditional non-pre-trained methods, with **preference accuracy** improving from 54.8% to 81.0% on *STEM tasks* and from 57.9% to 85.5% on *creative writing tasks* compared to *state-of-the-art (SOTA) baselines*. Additionally, **POLAR** improves *policy performance*, with *LLaMa3.1-8B* improving from an average of 47.36% to 56.33% and *Qwen2.5-32B* improving from 64.49% to 70.47% on 20 *benchmarks*.

## Limitations and Future Work
The paper does not explicitly mention limitations, but potential future directions include exploring the application of **POLAR** to other *domains* and *tasks*, as well as investigating the use of *different architectures* and *training methods* to further improve *reward model* performance.

## Practical Applications
The proposed **POLAR** approach has potential real-world applications in areas such as *autonomous systems*, *robotics*, and *natural language processing*, where *reward modeling* is crucial for developing effective and efficient *policies*. Additionally, the approach can be used to improve *human-computer interaction* and *decision-making systems* by providing reliable *reward signals* and enhancing *policy performance*.

---

**Authors:** Shihan Dou, Shichun Liu, Yuming Yang, Yicheng Zou, Yunhua Zhou, Shuhao Xing, Chenhao Huang, Qiming Ge, Demin Song, Haijun Lv, Songyang Gao, Chengqi Lv, Enyu Zhou, Honglin Guo, Zhiheng Xi, Wenwei Zhang, Qipeng Guo, Qi Zhang, Xipeng Qiu, Xuanjing Huang, Tao Gui, Kai Chen
