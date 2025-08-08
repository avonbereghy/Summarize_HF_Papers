# CellForge: Agentic Design of Virtual Cell Models

**Paper ID:** 2508.02276

**URL:** https://huggingface.co/papers/2508.02276

## Summary

## Executive Summary
The paper introduces **CellForge**, an *agentic design* system that leverages a multi-agent framework to transform biological datasets and research objectives into optimized computational models for virtual cells. By integrating three core modules - **Task Analysis**, **Method Design**, and **Experiment Execution** - CellForge can output both an optimized model architecture and executable code for training virtual cell models and inference. This approach enables the system to *autonomously build computational models* for virtual cells, addressing the challenges of biological system complexity, data modality heterogeneity, and the need for domain-specific expertise. The use of **large language models (LLMs)** and *iterative interaction* between agents with differing perspectives allows CellForge to provide better solutions than directly addressing a modeling challenge.

## Key Contributions and Findings
* **Introduction of CellForge**: CellForge is a novel *agentic design* system that can autonomously build computational models for virtual cells, using a multi-agent framework to integrate biological datasets and research objectives.
* **Modular Architecture**: The system consists of three core modules: **Task Analysis** for dataset characterization and literature retrieval, **Method Design** for collaborative development of optimized modeling strategies, and **Experiment Execution** for automated code generation. This modular architecture enables *flexible and efficient* model development.
* **Performance Evaluation**: CellForge demonstrates *state-of-the-art performance* in single-cell perturbation prediction, outperforming task-specific methods on six diverse datasets that encompass *gene knockouts*, *drug treatments*, and *cytokine stimulations*.
* **Collaborative Agent Interaction**: The use of *iterative interaction* between LLM agents with differing perspectives allows CellForge to provide better solutions than directly addressing a modeling challenge, highlighting the importance of *collaborative problem-solving* in complex biological systems.
* **Publicly Available Code**: The CellForge code is publicly available on *GitHub*, enabling researchers to *easily access and modify* the system for their own use cases.

## Methodology Overview
The CellForge methodology involves **Task Analysis**, which characterizes the input dataset and retrieves relevant literature using *natural language processing* techniques. The **Method Design** module uses a collaborative approach, where specialized agents with differing perspectives *exchange solutions* until they achieve a reasonable consensus. The **Experiment Execution** module generates executable code for training virtual cell models and inference using *automated programming* techniques.

## Results and Performance
The key results show that CellForge consistently outperforms task-specific state-of-the-art methods in single-cell perturbation prediction, with **high accuracy** and *low error rates*. The system demonstrates *robust performance* across six diverse datasets, encompassing different *biological modalities* and *perturbation types*. The results highlight the effectiveness of CellForge in *predicting responses to diverse perturbations*, a key challenge in virtual cell modeling.

## Limitations and Future Work
The paper mentions several limitations, including the need for *high-quality input data* and the potential for *overfitting* in certain scenarios. Future work directions include *expanding the system to handle more complex biological systems*, *integrating additional data modalities*, and *exploring applications in other fields*, such as *synthetic biology* and *personalized medicine*.

## Practical Applications
The CellForge system has several potential real-world applications, including *predicting responses to drugs or therapies*, *designing synthetic biological systems*, and *developing personalized treatment strategies*. The system can also be used to *simulate the behavior of complex biological systems*, enabling researchers to *test hypotheses and predict outcomes* in a virtual environment. The *agentic design* approach used in CellForge can also be applied to other fields, such as *materials science* and *engineering*, where complex systems need to be designed and optimized.

---

**Authors:** Xiangru Tang, Zhuoyun Yu, Jiapeng Chen, Yan Cui, Daniel Shao, Weixu Wang, Fang Wu, Yuchen Zhuang, Wenqi Shi, Zhi Huang, Arman Cohan, Xihong Lin, Fabian Theis, Smita Krishnaswamy, Mark Gerstein
