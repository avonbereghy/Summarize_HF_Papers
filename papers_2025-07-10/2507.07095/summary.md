# Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data

**Paper ID:** 2507.07095

**URL:** https://huggingface.co/papers/2507.07095

## Summary

## Executive Summary
The paper **Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data** presents a significant advancement in the field of *text-to-motion* generation, aiming to achieve **zero-shot generalization** capabilities. By introducing the largest human motion dataset, **MotionMillion**, featuring over 2 million high-quality motion sequences, and a comprehensive evaluation framework, **MotionMillion-Eval**, the authors demonstrate strong *generalization* to out-of-domain and complex compositional motions. Leveraging a **scalable architecture**, the model is scaled to 7B parameters, marking a significant step toward **zero-shot human motion generation** with *improved performance*.

## Key Contributions and Findings
* **Large-Scale Dataset**: The authors introduce **MotionMillion**, the largest human motion dataset to date, featuring over 2 million high-quality motion sequences, which provides a *comprehensive* foundation for training and evaluating *text-to-motion* models.
* **Comprehensive Evaluation Framework**: The paper proposes **MotionMillion-Eval**, a *rigorous* benchmark for evaluating *zero-shot motion generation*, allowing for *accurate* assessment of model performance and identification of directions for improvement.
* **Scalable Architecture**: The authors develop a **scalable architecture** that can be scaled to 7B parameters, enabling *efficient* training and *effective* generation of human motion sequences.
* **Zero-Shot Generalization**: The model demonstrates strong *generalization* to out-of-domain and complex compositional motions, marking a significant step toward **zero-shot human motion generation**.
* **Code Availability**: The code is made available at https://github.com/VankouF/MotionMillion-Codes, facilitating *reproducibility* and *future research*.

## Methodology Overview
The methodology involves **data collection** and **annotation** using an efficient pipeline, followed by **model training** using a **scalable architecture**. The authors employ *transfer learning* and *fine-tuning* techniques to adapt the model to the **MotionMillion** dataset. The **MotionMillion-Eval** framework is used to evaluate the model's performance on *zero-shot motion generation* tasks.

## Results and Performance
The results demonstrate strong **generalization** to out-of-domain and complex compositional motions, with *improved performance* compared to previous models. The authors report **state-of-the-art** results on the **MotionMillion-Eval** benchmark, with *significant improvements* in *accuracy* and *diversity* metrics. The model's performance is evaluated using **metrics** such as *BLEU score* and *Frechet inception distance*, showing *competitive* results.

## Limitations and Future Work
The authors mention limitations in terms of *dataset bias* and *limited domain coverage*. Potential future directions include *expanding the dataset* to cover more domains and *improving the model's robustness* to out-of-domain inputs. Additionally, the authors suggest exploring *multi-modal* approaches that incorporate *visual* and *audio* inputs to generate more *realistic* human motion sequences.

## Practical Applications
The paper has significant implications for *real-world applications* such as **computer vision**, **graphics**, and **robotics**. The ability to generate *natural* and *diverse* human motion sequences can be used in *animation*, *gaming*, and *simulations*. Additionally, the technology can be applied to *rehabilitation* and *therapy* by generating *personalized* motion sequences for patients. The *zero-shot generalization* capability can also be used in *human-robot interaction* and *autonomous systems* to generate *adaptive* and *responsive* motion sequences.

---

**Authors:** Ke Fan, Shunlin Lu, Minyue Dai, Runyi Yu, Lixing Xiao, Zhiyang Dou, Junting Dong, Lizhuang Ma, Jingbo Wang
