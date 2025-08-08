# Tool-integrated Reinforcement Learning for Repo Deep Search

**Paper ID:** 2508.03012

**URL:** https://huggingface.co/papers/2508.03012

## Summary

## Executive Summary
The paper presents **ToolTrain**, a novel two-stage training framework that combines *rejection-sampled supervised fine-tuning* and **tool-integrated reinforcement learning** to enhance the ability of *Large Language Models (LLMs)* to utilize repository retrieval tools for *issue localization*. This approach aims to bridge the *semantic gap* between natural language issue descriptions and faulty code, requiring complex *multi-hop reasoning* through code dependencies. By leveraging **tool-integrated reinforcement learning**, the framework enables LLMs to effectively navigate and reason through the codebase, leading to improved *issue localization* and *end-to-end issue resolution* performance.

## Key Contributions and Findings
* **Improved Issue Localization**: The paper demonstrates that *ToolTrain*-trained models achieve *state-of-the-art* performance on *function-level localization*, with the 32B model even surpassing *Claude-3.7*. This highlights the effectiveness of the proposed framework in enhancing LLMs' ability to utilize repository retrieval tools.
* **Tool-Integrated Reinforcement Learning**: The authors introduce a novel *reinforcement learning* approach that integrates repository retrieval tools, allowing LLMs to learn how to effectively use these tools for *issue localization*.
* **End-to-End Issue Resolution**: The paper shows that improved *issue localization* performance translates to better *end-to-end issue resolution* performance, demonstrating the practical impact of the proposed framework on automated software development.
* **Scalability and Generalizability**: The results suggest that the *ToolTrain* framework can be applied to different model sizes and architectures, making it a scalable and generalizable solution for *issue localization*.

## Methodology Overview
The methodology consists of two major components: **supervised fine-tuning** and **tool-integrated reinforcement learning**. The *supervised fine-tuning* stage involves *rejection-sampled* fine-tuning of LLMs on a dataset of issue descriptions and corresponding code locations. The *tool-integrated reinforcement learning* stage uses *reinforcement learning* to train LLMs to effectively utilize repository retrieval tools for *issue localization*. The framework leverages *multi-hop reasoning* and *navigation* through code dependencies to improve *issue localization* performance.

## Results and Performance
The key results show that *ToolTrain*-trained models achieve **state-of-the-art** performance on *function-level localization*, with the 32B model surpassing *Claude-3.7* by a significant margin. The results also demonstrate that improved *issue localization* performance leads to better **end-to-end issue resolution** performance, with *ToolTrain*-trained models outperforming baseline models on *resolution success rate* and *resolution time* metrics. The comparison with *Claude-3.7* highlights the effectiveness of the proposed framework in *real-world* scenarios.

## Limitations and Future Work
The paper mentions that the proposed framework requires a large dataset of issue descriptions and corresponding code locations, which can be time-consuming and expensive to collect. Future work includes exploring *transfer learning* and *few-shot learning* approaches to reduce the dataset requirements and improve the scalability of the framework. Additionally, the authors plan to investigate the application of the *ToolTrain* framework to other software development tasks, such as *code completion* and *bug fixing*.

## Practical Applications
The proposed framework has significant implications for *automated software development*, enabling developers to quickly and accurately identify and resolve issues in large codebases. The *ToolTrain* framework can be integrated into *integrated development environments (IDEs)* and *continuous integration/continuous deployment (CI/CD) pipelines* to improve the efficiency and effectiveness of software development processes. Additionally, the framework can be applied to other domains, such as *technical support* and *cybersecurity*, where *issue localization* and *resolution* are critical tasks.

---

**Authors:** Zexiong Ma, Chao Peng, Qunhong Zeng, Pengfei Gao, Yanzhen Zou, Bing Xie
