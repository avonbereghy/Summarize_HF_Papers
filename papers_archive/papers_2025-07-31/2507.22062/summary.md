# MetaCLIP 2: A Worldwide Scaling Recipe

**Paper ID:** 2507.22062

**URL:** https://huggingface.co/papers/2507.22062

## Summary

## Executive Summary
The paper introduces **MetaCLIP 2**, a novel approach to training *Contrastive Language-Image Pretraining (CLIP)* models on a worldwide scale, leveraging *image-text pairs* from the global web. By addressing the challenges of handling non-English data and the *"curse of multilinguality"*, MetaCLIP 2 achieves state-of-the-art performance on various *multilingual benchmarks*, including *zero-shot ImageNet classification* and *image-to-text retrieval* tasks. This is made possible through a carefully designed *training recipe* that enables mutual benefits from both English and non-English data, ultimately leading to improved performance and more robust models.

## Key Contributions and Findings
* **Scaling CLIP Training**: The authors propose a *scalable training approach* that can handle large amounts of data from the worldwide web, including non-English content, to improve the performance of CLIP models.
* **Addressing the Curse of Multilinguality**: MetaCLIP 2 mitigates the *"curse of multilinguality"* by developing a *recipe* that allows for the effective utilization of both English and non-English data, resulting in better performance than English-only models.
* **State-of-the-Art Performance**: The model achieves *state-of-the-art results* on several multilingual benchmarks, including *CVQA*, *Babel-ImageNet*, and *XM3600*, demonstrating its effectiveness in *image-to-text retrieval* and *zero-shot classification* tasks.
* **Mutual Benefits from Data**: The authors demonstrate that their approach enables mutual benefits from English and non-English data, leading to improved performance and more robust models.
* **Rigorous Ablations**: The paper presents *rigorous ablations* to identify the necessary components and techniques required to achieve state-of-the-art performance, providing valuable insights for future research.

## Methodology Overview
The methodology involves **large-scale data collection** and **preprocessing**, followed by **contrastive learning** using a *ViT-H/14 architecture*. The authors employ **multilingual training** techniques, including *language-specific preprocessing* and *data augmentation*, to effectively utilize both English and non-English data. The **training recipe** is designed to address the challenges of scaling CLIP training to worldwide web data.

## Results and Performance
The results show that MetaCLIP 2 achieves **state-of-the-art performance** on various benchmarks, including *zero-shot ImageNet classification* with an accuracy of **0.8%** higher than its English-only counterpart, and **57.4%** on *CVQA*, **50.2%** on *Babel-ImageNet*, and **64.3%** on *XM3600* for *image-to-text retrieval*. The model outperforms existing approaches, such as *mSigLIP*, by **0.7%** on *zero-shot ImageNet classification*.

## Limitations and Future Work
The authors acknowledge the potential **limitations** of their approach, including the need for large amounts of labeled data and the challenges of handling low-resource languages. Future work may focus on **improving the efficiency** of the training recipe, **exploring new architectures**, and **applying MetaCLIP 2 to real-world applications**.

## Practical Applications
The practical applications of MetaCLIP 2 are numerous, including *image search*, *multilingual chatbots*, and *cross-lingual information retrieval*. The model's ability to effectively utilize both English and non-English data makes it a valuable tool for *global content understanding* and *multilingual AI applications*. Additionally, the approach can be applied to other *multimodal tasks*, such as *video understanding* and *audio-visual processing*, enabling more robust and accurate models for real-world applications.

---

**Authors:** Yung-Sung Chuang, Yang Li, Dong Wang, Ching-Feng Yeh, Kehan Lyu, Ramya Raghavendra, James Glass, Lifei Huang, Jason Weston, Luke Zettlemoyer, Xinlei Chen, Zhuang Liu, Saining Xie, Wen-tau Yih, Shang-Wen Li, Hu Xu
