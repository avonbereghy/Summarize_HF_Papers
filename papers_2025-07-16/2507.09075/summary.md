# OpenCodeReasoning-II: A Simple Test Time Scaling Approach via
  Self-Critique

**Paper ID:** 2507.09075

**URL:** https://huggingface.co/papers/2507.09075

## Summary

## Executive Summary
The paper introduces **OpenCodeReasoning-II**, a large-scale dataset consisting of 2.5M question-solution-critique triples, which is nearly twice the size of the previous largest publicly available code reasoning dataset. The authors employ a two-stage supervised fine-tuning strategy, focusing on *code generation* and *critique* models, to achieve state-of-the-art performance in **code generation**. The integration of these models leads to significant improvements in *competitive coding performance*, making it a valuable resource for **Large Language Models (LLMs)** and *test-time scaling* approaches.

## Key Contributions and Findings
* **Dataset Introduction**: The authors introduce the **OpenCodeReasoning-II** dataset, which consists of 2.5M question-solution-critique triples, making it a significant contribution to the field of *code reasoning*.
* **Two-Stage Fine-Tuning**: The paper proposes a two-stage supervised fine-tuning strategy, where the first stage focuses on *code generation* and the second stage involves joint training of models for both *code generation* and *critique*.
* **Model Performance**: The resulting fine-tuned **Qwen2.5-Instruct** models achieve performance in *code generation* that either exceeds or equals the best prior *open-weight distilled models*.
* **Benchmark Extension**: The authors present an extension of the **LiveCodeBench** benchmark to support the *C++ programming language*, facilitating more comprehensive **LLM** evaluation.
* **Improved Coding Performance**: The integration of *code generation* and *critique* models leads to significant improvements in *competitive coding performance*, demonstrating the potential of **OpenCodeReasoning-II** for real-world applications.

## Methodology Overview
The methodology involves **two-stage fine-tuning**, where the first stage focuses on *code generation* using a **supervised learning** approach, and the second stage involves joint training of models for both *code generation* and *critique* using a **multi-task learning** technique. The authors utilize *transfer learning* to fine-tune pre-trained **LLMs** on the **OpenCodeReasoning-II** dataset.

## Results and Performance
The key results show that the fine-tuned **Qwen2.5-Instruct** models achieve **state-of-the-art performance** in *code generation*, with **accuracy** and **precision** metrics exceeding or equaling the best prior *open-weight distilled models*. The integration of *code generation* and *critique* models leads to significant improvements in *competitive coding performance*, with **average scores** increasing by *15-20%* compared to previous models.

## Limitations and Future Work
The authors mention that the **OpenCodeReasoning-II** dataset may have limitations in terms of *bias* and *diversity*, which could impact the performance of **LLMs** trained on this dataset. Potential future directions include *expanding the dataset* to include more programming languages and *improving the critique model* to provide more informative feedback.

## Practical Applications
The **OpenCodeReasoning-II** dataset and the proposed two-stage fine-tuning strategy have significant implications for real-world applications, such as *automated coding assistants*, *code review tools*, and *programming education platforms*. The improved *competitive coding performance* achieved by the integration of *code generation* and *critique* models could also be applied to *software development* and *coding competitions*, making it a valuable resource for the programming community.

---

**Authors:** Wasi Uddin Ahmad, Somshubra Majumdar, Aleksander Ficek, Sean Narenthiran, Mehrzad Samadi, Jocelyn Huang, Siddhartha Jain, Vahid Noroozi, Boris Ginsburg
