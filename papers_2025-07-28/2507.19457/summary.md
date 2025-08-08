# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

**Paper ID:** 2507.19457

**URL:** https://huggingface.co/papers/2507.19457

## Summary

## Executive Summary
The paper introduces **GEPA**, a novel prompt optimizer that leverages *natural language reflection* to learn high-level rules from trial and error, outperforming traditional *reinforcement learning* methods like **GRPO**. By incorporating *interpretable language* and *Pareto frontier* analysis, **GEPA** can achieve significant quality gains with *fewer rollouts* and demonstrate promising results in various tasks, including code optimization. The authors argue that the *interpretable nature of language* provides a richer learning medium for **LLMs**, enabling **GEPA** to excel in downstream tasks.

## Key Contributions and Findings
* **Introduction of GEPA**: The paper presents **GEPA**, a prompt optimizer that utilizes *natural language reflection* to diagnose problems, propose, and test prompt updates, leading to improved performance.
* **Comparison with GRPO**: **GEPA** outperforms **GRPO** by *10% on average* and up to *20%* while using *up to 35x fewer rollouts*, demonstrating its efficiency and effectiveness.
* **Comparison with MIPROv2**: **GEPA** also outperforms the leading prompt optimizer, **MIPROv2**, by *over 10%* across two **LLMs**, showcasing its potential as a superior optimization strategy.
* **Code Optimization Results**: **GEPA** demonstrates promising results as an *inference-time search strategy* for code optimization, highlighting its versatility and applicability.

## Methodology Overview
The methodology involves **GEPA**, which consists of **major components** such as *system-level trajectory sampling*, *natural language reflection*, and *Pareto frontier* analysis. The authors employ *specific techniques* like *genetic algorithms* and *reflection* to optimize prompts and improve performance.

## Results and Performance
The key results show that **GEPA** achieves **high-quality gains** with *fewer rollouts*, outperforming **GRPO** in terms of **average performance** by *10%* and **peak performance** by up to *20%*. The results also highlight **GEPA**'s efficiency, using *up to 35x fewer rollouts* than **GRPO**. In comparison to **MIPROv2**, **GEPA** demonstrates *superior performance* across two **LLMs**.

## Limitations and Future Work
The paper does not explicitly mention limitations, but potential future directions include:
* Exploring **GEPA**'s applicability to other domains and tasks
* Investigating the use of **GEPA** in conjunction with other optimization strategies
* Further analyzing the *interpretable nature of language* and its implications for **LLMs**

## Practical Applications
The introduction of **GEPA** has significant implications for various real-world applications, including:
* **Code optimization**: **GEPA** can be used to optimize code and improve its performance, leading to more efficient and effective software development.
* **Natural language processing**: **GEPA**'s ability to leverage *natural language reflection* can be applied to various **NLP** tasks, such as language translation, text summarization, and sentiment analysis.
* **AI system development**: **GEPA** can be used to optimize and improve the performance of **AI systems**, leading to more efficient and effective decision-making processes.

---

**Authors:** Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, Christopher Potts, Koushik Sen, Alexandros G. Dimakis, Ion Stoica, Dan Klein, Matei Zaharia, Omar Khattab
