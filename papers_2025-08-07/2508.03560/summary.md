# LaTCoder: Converting Webpage Design to Code with Layout-as-Thought

**Paper ID:** 2508.03560

**Authors:** Yi Gui, Zhen Li, Zhongyi Zhang, Guohao Wang, Tianpeng Lv, Gaoyang Jiang, Yi Liu, Dongping Chen, Yao Wan, Hongyu Zhang, Wenbin Jiang, Xuanhua Shi, Hai Jin

**URL:** https://huggingface.co/papers/2508.03560

## Summary

## Executive Summary

LaTCoder is a novel approach to **design-to-code** conversion that significantly improves the accuracy of webpage layout preservation during code generation.  Unlike existing methods that often struggle with complex layouts, LaTCoder leverages a *Layout-as-Thought (LaT)* strategy inspired by *Chain-of-Thought (CoT)* reasoning. This involves dividing the webpage design into image blocks, prompting a *Multimodal Large Language Model (MLLM)* to generate code for each block using a CoT-based approach, and employing two assembly strategies with dynamic selection for optimal output.  Experimental results on both public and newly created challenging benchmarks demonstrate substantial improvements in *TreeBLEU* scores and *Mean Absolute Error (MAE)*, with strong preference shown by human evaluators for LaTCoder's generated webpages.


## Key Contributions and Findings

* **Improved Layout Preservation:** LaTCoder addresses the common issue of layout inaccuracies in existing design-to-code systems by incorporating *Layout-as-Thought (LaT)*, resulting in significantly better preservation of the original design's structure.

* **Efficient Block-Based Approach:** The *efficient image block division algorithm* simplifies the input for the MLLM, making the process more manageable and improving the accuracy of code generation for complex layouts.

* **Hybrid Assembly Strategy:** The use of both *absolute positioning* and an *MLLM-based assembly method*, with dynamic selection, allows for flexibility and optimization of the final code output, leading to higher quality results.

* **Superior Performance on Challenging Benchmarks:**  LaTCoder demonstrates *substantial improvements* in *TreeBLEU* (+66.67% with DeepSeek-VL2) and *MAE* (-38% with DeepSeek-VL2) compared to direct prompting methods, particularly on the newly introduced *CC-HARD* benchmark containing complex layouts.

* **Strong Human Preference:**  Human evaluation shows a clear preference for LaTCoder's generated webpages in *over 60%* of cases, validating the effectiveness of the proposed approach.


## Methodology Overview

LaTCoder's methodology consists of three main stages:  **1. Image Block Division:** The input webpage design is divided into smaller, manageable image blocks using an *efficient algorithm*. **2. CoT-based Code Generation:**  A *Multimodal Large Language Model (MLLM)*, such as *DeepSeek-VL2, Gemini, or GPT-4o*, generates code for each block using a *Chain-of-Thought (CoT)* prompt. **3. Assembly and Selection:** Two assembly strategies, *absolute positioning* and an *MLLM-based method*, are employed, with a dynamic selection process choosing the optimal output based on the generated code.


## Results and Performance

LaTCoder achieved significant improvements over baseline methods.  *TreeBLEU* scores increased by *66.67%* and *MAE* decreased by *38%* when using *DeepSeek-VL2* as the backbone MLLM.  Human evaluation showed a preference for LaTCoder's output in *over 60%* of cases. These results demonstrate the effectiveness of LaTCoder, especially on the more challenging *CC-HARD* benchmark.


## Limitations and Future Work

While LaTCoder shows significant improvements, limitations include potential challenges with extremely complex or unusual layouts.  Future work could focus on handling more intricate designs, improving the robustness of the assembly strategies, and exploring different MLLMs and prompting techniques to further enhance performance.  Investigating the scalability of the approach to larger and more complex webpages is also crucial.


## Practical Applications

LaTCoder has significant implications for **front-end development**, potentially accelerating the UI development process by automating the conversion of designs into functional code. This could *reduce development time and costs*, allowing designers and developers to focus on more complex aspects of the project.  It could also improve the accessibility of web development for individuals with less coding experience.