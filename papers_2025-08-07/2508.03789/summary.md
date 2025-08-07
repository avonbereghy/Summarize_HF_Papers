# HPSv3: Towards Wide-Spectrum Human Preference Score

**Paper ID:** 2508.03789

**Authors:** Yuhang Ma, Xiaoshi Wu, Keqiang Sun, Hongsheng Li

**URL:** https://huggingface.co/papers/2508.03789

## Summary

## Executive Summary

This paper introduces **HPSv3**, a novel *human preference score* for evaluating text-to-image generation models.  Addressing limitations of existing metrics, HPSv3 leverages a **large-scale dataset (HPDv3)** containing *1.08M text-image pairs and 1.17M pairwise comparisons*, encompassing a *wide spectrum* of image quality.  A *Vision-Language Model (VLM)-based preference model* trained with an *uncertainty-aware ranking loss* is used, along with a novel iterative refinement method, **Chain-of-Human-Preference (CoHP)**, to improve image generation quality.  Experiments demonstrate HPSv3's robustness and CoHP's effectiveness in aligning image generation with human preferences. The code and dataset are publicly available.


## Key Contributions and Findings

* **Large-Scale Human Preference Dataset (HPDv3):** The authors introduce HPDv3, a *comprehensive dataset* containing *1.08M text-image pairs and 1.17M pairwise comparisons*, covering a wide range of image quality from various generative models and real-world sources.  This significantly expands the data available for training and evaluating preference models.

* **Vision-Language Model (VLM)-based Preference Model:**  A *VLM* is trained using an *uncertainty-aware ranking loss* to learn fine-grained preferences between image-text pairs. This approach improves the accuracy and robustness of the preference scoring compared to previous methods.

* **Chain-of-Human-Preference (CoHP) Refinement Method:** CoHP is a novel *iterative image refinement technique* that uses HPSv3 to iteratively select the best image at each step, leading to improved image quality without requiring additional data.

* **Robust and Wide-Spectrum Evaluation Metric:**  HPSv3 is shown to be a *robust and effective metric* for evaluating text-to-image generation models across a *wide spectrum of image quality*.

* **Publicly Available Resources:** The code and the HPDv3 dataset are made publicly available, facilitating further research and development in the field.


## Methodology Overview

The methodology involves three main components: (1) **Creation of HPDv3:**  A large dataset of text-image pairs and pairwise comparisons is compiled from various sources, including *state-of-the-art generative models and real-world images*. (2) **Training a VLM-based Preference Model:** A *VLM* is trained on HPDv3 using an *uncertainty-aware ranking loss* to predict human preferences. (3) **Development of CoHP:** An *iterative refinement algorithm* is developed that uses HPSv3 to select the best image at each step, improving image quality.


## Results and Performance

Experiments demonstrate that HPSv3 provides a *more robust and accurate evaluation* compared to existing metrics.  CoHP shows a *significant improvement* in image generation quality, demonstrating its effectiveness in aligning generated images with human preferences.  Specific **quantitative metrics** (e.g., correlation with human judgments) are presented in the paper to support these claims.  *Comparisons with other state-of-the-art methods* highlight the superior performance of HPSv3 and CoHP.


## Limitations and Future Work

While HPSv3 represents a significant advancement, limitations include the potential biases inherent in the dataset and the computational cost of training the VLM.  Future work could focus on addressing these biases, improving the efficiency of the VLM, and exploring the application of HPSv3 to other image generation tasks beyond text-to-image.


## Practical Applications

HPSv3 and CoHP have several practical applications. They can be used to: (1) **Benchmark and compare different text-to-image generation models** objectively, (2) **Guide the development of new models** by providing a clear measure of human preference alignment, (3) **Improve the quality of generated images** through iterative refinement using CoHP, and (4) **Enable more efficient and human-centered design** of text-to-image systems.