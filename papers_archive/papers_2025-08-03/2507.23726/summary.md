# Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving

**Paper ID:** 2507.23726

**URL:** https://huggingface.co/papers/2507.23726

## Summary

## Executive Summary
The paper introduces **Seed-Prover**, a *lemma-style whole-proof reasoning model* that leverages **reinforcement learning** and **formal verification** to achieve significant advancements in **automated mathematical reasoning**. By utilizing a dedicated domain-specific language like *Lean*, Seed-Prover can iteratively refine its proof based on *feedback*, *proved lemmas*, and *self-summarization*. This enables the model to perform both **deep** and **broad reasoning**, making it a powerful tool for solving complex mathematical problems, including *IMO-level contest problems*.

## Key Contributions and Findings
* **Advancements in Automated Theorem Proving**: Seed-Prover proves *78.1% of formalized past IMO problems*, demonstrating its effectiveness in *automated mathematical reasoning*.
* **Introduction of Seed-Geometry**: A *geometry reasoning engine* that outperforms previous formal geometry engines, addressing the lack of *geometry support* in *Lean*.
* **Test-Time Inference Strategies**: The authors design three *test-time inference strategies* that enable both **deep** and **broad reasoning**, allowing Seed-Prover to solve complex mathematical problems.
* **State-of-the-Art Performance**: Seed-Prover achieves over *50%* on *PutnamBench*, outperforming the previous **state-of-the-art** by a large margin.
* **Real-World Applications**: Seed-Prover and Seed-Geometry are used to participate in *IMO 2025*, fully proving *5 out of 6 problems* and demonstrating their potential for real-world applications.

## Methodology Overview
The methodology involves **Seed-Prover**, a *lemma-style whole-proof reasoning model* that utilizes **reinforcement learning** and **formal verification**. The model is trained using *Lean*, a dedicated domain-specific language that provides clear *supervision signals*. The authors also employ *self-summarization* and *feedback* mechanisms to enable the model to iteratively refine its proof. Additionally, they introduce **Seed-Geometry**, a *geometry reasoning engine* that addresses the lack of *geometry support* in *Lean*.

## Results and Performance
The key results include **78.1%** proof rate on formalized past IMO problems, **saturation** of *MiniF2F*, and over **50%** performance on *PutnamBench*. These results demonstrate the effectiveness of Seed-Prover in *automated mathematical reasoning*, outperforming the previous **state-of-the-art** by a large margin. The authors also report that Seed-Prover and Seed-Geometry fully prove *5 out of 6 problems* in *IMO 2025*, showcasing their potential for real-world applications.

## Limitations and Future Work
The authors do not explicitly mention any limitations, but potential future directions include:
* Improving the performance of Seed-Prover on more complex mathematical problems
* Extending the capabilities of Seed-Geometry to support a wider range of geometric reasoning tasks
* Exploring the application of Seed-Prover and Seed-Geometry in other domains, such as *computer science* or *engineering*

## Practical Applications
The potential real-world applications of Seed-Prover and Seed-Geometry include:
* **Automated theorem proving**: Seed-Prover can be used to automate the proof of mathematical theorems, reducing the time and effort required for human mathematicians.
* **Mathematical education**: Seed-Prover and Seed-Geometry can be used to create interactive mathematical learning tools, helping students to understand complex mathematical concepts.
* **Computer science and engineering**: The techniques developed in this paper can be applied to other domains, such as *formal verification* of software and hardware systems.

---

**Authors:** Luoxin Chen, Jinming Gu, Liankai Huang, Wenhao Huang, Zhicheng Jiang, Allan Jie, Xiaoran Jin, Xing Jin, Chenggang Li, Kaijing Ma, Cheng Ren, Jiawei Shen, Wenlei Shi, Tong Sun, He Sun, Jiahui Wang, Siran Wang, Zhihong Wang, Chenrui Wei, Shufa Wei, Yonghui Wu, Yuchen Wu, Yihang Xia, Huajian Xin, Fan Yang, Huaiyuan Ying, Hongyi Yuan, Zheng Yuan, Tianyang Zhan, Chi Zhang, Yue Zhang, Ge Zhang, Tianyun Zhao, Jianqiu Zhao, Yichi Zhou, Thomas Hanwen Zhu
