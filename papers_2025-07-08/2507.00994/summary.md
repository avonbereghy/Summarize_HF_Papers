# Should We Still Pretrain Encoders with Masked Language Modeling?

**Paper ID:** 2507.00994

**URL:** https://huggingface.co/papers/2507.00994

## Summary

## Executive Summary
The paper **Should We Still Pretrain Encoders with Masked Language Modeling?** explores the effectiveness of *pretraining* encoders using **Masked Language Modeling (MLM)** versus **Causal Language Modeling (CLM)**. The authors investigate whether the gains of CLM-trained models are due to the *objective* itself or *confounding factors* such as model and data scale. Through a series of large-scale experiments, they find that while **MLM** generally yields better performance, **CLM**-trained models are more *data-efficient* and demonstrate improved *fine-tuning stability*. The authors propose a **biphasic training strategy** that combines the benefits of both approaches.

## Key Contributions and Findings
* **Pretraining Objectives**: The authors compare the effectiveness of **MLM** and **CLM** as pretraining objectives for encoders, finding that **MLM** generally yields better performance across *text representation tasks*.
* **Data Efficiency**: **CLM**-trained models are shown to be more *data-efficient*, requiring less data to achieve similar performance to **MLM**-trained models.
* **Fine-Tuning Stability**: The authors demonstrate that **CLM**-trained models exhibit improved *fine-tuning stability*, making them more reliable for downstream tasks.
* **Biphasic Training Strategy**: The proposed **biphasic training strategy** sequentially applies **CLM** and then **MLM**, achieving optimal performance under a fixed *computational training budget*.
* **Practical Implications**: The authors highlight the potential benefits of initializing from readily available *pretrained CLM models*, reducing the computational burden needed to train best-in-class encoder models.

## Methodology Overview
The authors employ a **large-scale experimental setup**, training a total of 30 models ranging from 210 million to 1 billion parameters. They use **pretraining ablations** and conduct over 15,000 *fine-tuning and evaluation runs* to compare the performance of **MLM** and **CLM**-trained models. The methodology involves **carefully controlled experiments** to isolate the effects of the pretraining objective and *model scale*.

## Results and Performance
The authors report that **MLM**-trained models generally achieve better performance across *text representation tasks*, with **MLM** outperforming **CLM** on most benchmarks. However, **CLM**-trained models demonstrate improved *data efficiency* and *fine-tuning stability*. The proposed **biphasic training strategy** achieves optimal performance under a fixed *computational training budget*, with **MLM** and **CLM** combined outperforming either approach alone.

## Limitations and Future Work
The authors acknowledge the *computational cost* of their experiments and the potential for *overfitting* in some models. Future work could investigate the application of the proposed **biphasic training strategy** to other *NLP tasks* and explore the use of *transfer learning* to adapt pretrained models to new domains.

## Practical Applications
The findings of this paper have significant implications for the development of *NLP systems*, particularly in applications where *data efficiency* and *fine-tuning stability* are crucial. The proposed **biphasic training strategy** could be used to improve the performance of *language models* and *text classification systems*, leading to more accurate and reliable *NLP models* in real-world applications.

---

**Authors:** Hippolyte Gisserot-Boukhlef, Nicolas Boizard, Manuel Faysse, Duarte M. Alves, Emmanuel Malherbe, André F. T. Martins, Céline Hudelot, Pierre Colombo
