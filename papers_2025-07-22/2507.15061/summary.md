# WebShaper: Agentically Data Synthesizing via Information-Seeking
  Formalization

**Paper ID:** 2507.15061

**URL:** https://huggingface.co/papers/2507.15061

## Summary

## Executive Summary
The paper introduces **WebShaper**, a novel framework for synthesizing data for *information-seeking* (IS) tasks, which enables **Large Language Model** (LLM)-powered agents to perform complex tasks through *web-based* information retrieval. By adopting a **formalization-driven** approach, WebShaper constructs a dataset that mitigates the inconsistency between *information structure* and *reasoning structure*, question and answer. This is achieved through the concept of **Knowledge Projections** (KP), which allows for precise control over *reasoning structure* by KP operation compositions. The framework demonstrates **state-of-the-art** performance on *GAIA* and *WebWalkerQA* benchmarks.

## Key Contributions and Findings
* **Formalization of IS Tasks**: WebShaper systematically formalizes IS tasks through *set theory*, enabling precise control over *reasoning structure* by KP operation compositions.
* **Knowledge Projections (KP)**: The concept of KP allows for *precise control* over *reasoning structure*, enabling the creation of complex questions with *retrieval* and *validation* tools.
* **Multi-Step Expansion Process**: The framework uses a *multi-step expansion process* to synthesize data, starting with *seed tasks* and expanding them into more complex questions using an *agentic Expander*.
* **State-of-the-Art Performance**: WebShaper achieves *state-of-the-art* performance among open-sourced IS agents on *GAIA* and *WebWalkerQA* benchmarks, demonstrating the effectiveness of the framework.
* **Data Synthesis**: The framework provides a novel approach to *data synthesis*, enabling the creation of high-quality training data for IS agents.

## Methodology Overview
The methodology involves **formalizing** IS tasks through *set theory*, and then using a **multi-step expansion process** to synthesize data. This process includes creating *seed tasks*, and then using an *agentic Expander* to expand them into more complex questions with *retrieval* and *validation* tools based on the **Knowledge Projections** (KP) concept.

## Results and Performance
The results demonstrate that WebShaper achieves **state-of-the-art** performance on *GAIA* and *WebWalkerQA* benchmarks, with **improved accuracy** and **efficiency** compared to existing approaches. The framework also shows *significant improvements* in terms of **question complexity** and **reasoning structure**, demonstrating its ability to handle complex IS tasks.

## Limitations and Future Work
The paper does not explicitly mention any limitations, but potential future directions include:
* Exploring the application of WebShaper to other *domains* and *tasks*
* Investigating the use of *alternative formalization approaches*
* Developing more *advanced Expander* techniques to further improve the quality of synthesized data

## Practical Applications
The WebShaper framework has potential practical applications in areas such as:
* **Virtual assistants**: enabling more effective and efficient *information-seeking* capabilities
* **Question answering systems**: improving the accuracy and complexity of *question answering* tasks
* **Natural language processing**: enhancing the ability of *language models* to handle complex and open-ended! tasks
* **Web search and retrieval**: improving the effectiveness of *web search* and *information retrieval* systems.

---

**Authors:** Zhengwei Tao, Jialong Wu, Wenbiao Yin, Junkai Zhang, Baixuan Li, Haiyang Shen, Kuan Li, Liwen Zhang, Xinyu Wang, Yong Jiang, Pengjun Xie, Fei Huang, Jingren Zhou
