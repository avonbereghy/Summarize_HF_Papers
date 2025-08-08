# Seq vs Seq: An Open Suite of Paired Encoders and Decoders

**Paper ID:** 2507.11412

**URL:** https://huggingface.co/papers/2507.11412

## Summary

## Executive Summary
The paper introduces the **Seq vs Seq** suite, a comprehensive collection of paired *encoder-only* and *decoder-only* models, ranging from 17 million to 1 billion parameters, trained on up to 2 trillion tokens. The authors demonstrate that using the same **training recipe** for both *encoder-only* and *decoder-only* models produces state-of-the-art (**SOTA**) results in both categories, outperforming notable models like *ModernBERT* and *Llama 3.2*. The study highlights the strengths of each architecture, with *encoder-only* models exceling at *classification* and *retrieval tasks*, while *decoder-only* models excel at *generative tasks*.

## Key Contributions and Findings
* **Model Architecture Comparison**: The authors compare the performance of *encoder-only* and *decoder-only* models on various tasks, showing that each architecture has its strengths and weaknesses, with *encoder-only* models performing well on *classification* tasks and *decoder-only* models performing well on *generative tasks*.
* **Training Recipe**: The study demonstrates that using the same **training recipe** for both *encoder-only* and *decoder-only* models can produce **SOTA** results in both categories, highlighting the importance of *training techniques* and *dataset* selection.
* **Adaptation and Fine-Tuning**: The authors show that adapting a *decoder* model to *encoder* tasks (and vice versa) through continued training is subpar compared to using only the reverse *objective*, emphasizing the need for *task-specific* models.
* **Open-Source Release**: The authors open-source all artifacts of the study, including *training data*, *training order segmented by checkpoint*, and over 200 checkpoints, allowing future work to analyze or extend all aspects of *training*.

## Methodology Overview
The methodology involves **training** paired *encoder-only* and *decoder-only* models using the same **recipe**, which includes *dataset* selection, *training techniques*, and *hyperparameter tuning*. The authors utilize **large-scale datasets** and *distributed training* to train models of varying sizes, from 17 million to 1 billion parameters.

## Results and Performance
The key results show that the **Seq vs Seq** suite achieves **SOTA** performance on various tasks, with *encoder-only* models outperforming *ModernBERT* on *classification tasks* and *decoder-only* models outperforming *Llama 3.2* and *SmolLM2* on *generative tasks*. The authors report **state-of-the-art** results on tasks like *MNLI*, with a 400M *encoder* outperforming a 1B *decoder*, and vice versa for *generative tasks*.

## Limitations and Future Work
The study mentions limitations in terms of *computational resources* and *dataset* selection, highlighting the need for further research on *efficient training methods* and *dataset curation*. Potential future directions include exploring *multi-task learning*, *transfer learning*, and *few-shot learning* with the **Seq vs Seq** suite.

## Practical Applications
The **Seq vs Seq** suite has potential real-world applications in *natural language processing* tasks, such as *text classification*, *information retrieval*, and *text generation*. The study's findings can inform the development of more efficient and effective *language models* for tasks like *chatbots*, *language translation*, and *content generation*, highlighting the importance of *task-specific* models and *training recipes*.

---

**Authors:** Orion Weller, Kathryn Ricci, Marc Marone, Antoine Chaffin, Dawn Lawrie, Benjamin Van Durme
