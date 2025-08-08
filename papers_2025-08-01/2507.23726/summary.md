# Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving

**Paper ID:** 2507.23726

**URL:** https://huggingface.co/papers/2507.23726

## Summary

## Executive Summary
The paper introduces **Seed-Prover**, a novel approach to automated theorem proving that leverages *reinforcement learning* and *formal verification* to achieve significant advancements in mathematical reasoning. By utilizing a dedicated domain-specific language like **Lean**, Seed-Prover can iteratively refine its proof based on *feedback* and *self-summarization*. This enables both **deep** and **broad** reasoning, allowing the model to tackle complex problems like IMO-level contest questions. The authors also introduce **Seed-Geometry**, a geometry reasoning engine that addresses the lack of geometry support in Lean, and demonstrate the effectiveness of their approach by fully proving 5 out of 6 IMO 2025 problems.

## Key Contributions and Findings
* **Automated Theorem Proving**: Seed-Prover achieves state-of-the-art performance in automated theorem proving, proving *78.1%* of formalized past IMO problems and saturating *MiniF2F*.
* **Geometry Reasoning**: The introduction of **Seed-Geometry** addresses the lack of geometry support in Lean, outperforming previous formal geometry engines and enabling the solution of geometry-related problems.
* **Long Chain-of-Thought Reasoning**: Seed-Prover demonstrates the effectiveness of *long chain-of-thought reasoning* in mathematical problem-solving, allowing the model to refine its proof iteratively and achieve significant advancements in automated mathematical reasoning.
* **Formal Verification**: The use of *formal verification* provides clear supervision signals, enabling effective training of the model through *reinforcement learning*.
* **Test-Time Inference Strategies**: The authors design three test-time inference strategies that enable both **deep** and **broad** reasoning, allowing Seed-Prover to tackle complex problems and achieve state-of-the-art performance.

## Methodology Overview
The methodology involves **Seed-Prover**, a lemma-style whole-proof reasoning model that utilizes *reinforcement learning* and *formal verification* to refine its proof iteratively. The model consists of **major components** like *proof refinement*, *self-summarization*, and *feedback mechanisms*, which enable the model to achieve **deep** and **broad** reasoning. The authors also employ *specific techniques* like *long chain-of-thought reasoning* and *geometry reasoning* to address the challenges of automated theorem proving.

## Results and Performance
The key results include **78.1%** proof rate for formalized past IMO problems, **saturation** of *MiniF2F*, and *over 50%* performance on *PutnamBench*, outperforming the previous state-of-the-art by a *large margin*. The authors also demonstrate the effectiveness of their approach by fully proving 5 out of 6 IMO 2025 problems, showcasing the potential of **Seed-Prover** and **Seed-Geometry** in automated mathematical reasoning.

## Limitations and Future Work
The authors mention the lack of geometry support in Lean as a limitation, which they address by introducing **Seed-Geometry**. Potential future directions include *improving the performance* of Seed-Prover and Seed-Geometry, *expanding the scope* of automated theorem proving to other areas of mathematics, and *exploring the applications* of formal verification and long chain-of-thought reasoning in other domains.

## Practical Applications
The practical applications of **Seed-Prover** and **Seed-Geometry** include *automated proof verification*, *mathematical discovery*, and *education*. The ability to automate theorem proving can *revolutionize* the field of mathematics, enabling researchers to focus on higher-level problems and accelerating the discovery of new mathematical concepts. Additionally, the use of formal verification and long chain-of-thought reasoning can have *far-reaching implications* in areas like *artificial intelligence*, *computer science*, and *cognitive psychology*.

---

**Authors:** Luoxin Chen, Jinming Gu, Liankai Huang, Wenhao Huang, Zhicheng Jiang, Allan Jie, Xiaoran Jin, Xing Jin, Chenggang Li, Kaijing Ma, Cheng Ren, Jiawei Shen, Wenlei Shi, Tong Sun, He Sun, Jiahui Wang, Siran Wang, Zhihong Wang, Chenrui Wei, Shufa Wei, Yonghui Wu, Yuchen Wu, Yihang Xia, Huajian Xin, Fan Yang, Huaiyuan Ying, Hongyi Yuan, Zheng Yuan, Tianyang Zhan, Chi Zhang, Yue Zhang, Ge Zhang, Tianyun Zhao, Jianqiu Zhao, Yichi Zhou, Thomas Hanwen Zhu
