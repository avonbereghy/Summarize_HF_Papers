# Scaling Laws for Optimal Data Mixtures

**Paper ID:** 2507.09404

**URL:** https://huggingface.co/papers/2507.09404

## Summary

## Executive Summary
The paper **Scaling Laws for Optimal Data Mixtures** proposes a systematic method to determine the optimal *data mixture* for training large foundation models, which is critical for achieving good model performance. The authors introduce **scaling laws** that can accurately predict the *loss* of a model trained with a specific *domain weight vector*. This approach provides a principled alternative to costly *trial-and-error* methods, allowing for the estimation of optimal *domain weights* for any target domain under a given training budget. The *scaling laws* are validated in three distinct settings: *large language models*, *native multimodal models*, and *large vision models*.

## Key Contributions and Findings
* **Optimal Data Mixture Determination**: The authors propose a method to determine the optimal *data mixture* using *scaling laws*, which can accurately predict the *loss* of a model trained with a specific *domain weight vector*.
* **Universality of Scaling Laws**: The *scaling laws* are shown to be universal, demonstrating predictive power in three distinct and large-scale settings: *large language models*, *native multimodal models*, and *large vision models*.
* **Extrapolation to New Data Mixtures**: The *scaling laws* can extrapolate to new *data mixtures* and across scales, allowing for the estimation of optimal *domain weights* using a few small-scale training runs.
* **Principled Alternative to Trial-and-Error**: The approach provides a principled alternative to costly *trial-and-error* methods, enabling the estimation of optimal *domain weights* for any target domain under a given training budget.
* **Accurate Estimation of Performance**: The *scaling laws* can accurately estimate the *performance* of a model at larger scales and unseen *domain weights*.

## Methodology Overview
The methodology involves **scaling laws** that model the relationship between the *loss* of a model and its size, the number of training tokens, and the *domain weight vector*. The authors use **regression analysis** to estimate the parameters of the *scaling laws* from a few small-scale training runs. The **scaling laws** are then used to estimate the optimal *domain weights* for any target domain under a given training budget, utilizing *optimization techniques* to find the best *data mixture*.

## Results and Performance
The key results show that the **scaling laws** can accurately predict the **loss** of a model trained with a specific *domain weight vector*, with *high correlation* between predicted and actual values. The authors also demonstrate that the **scaling laws** can extrapolate to new *data mixtures* and across scales, achieving **state-of-the-art performance** in three distinct settings: *large language models*, *native multimodal models*, and *large vision models*. The results are compared to *baseline methods*, showing *significant improvements* in terms of **accuracy** and **efficiency**.

## Limitations and Future Work
The limitations of the study include the assumption of a *linear relationship* between the *loss* and the *domain weight vector*, which may not hold in all cases. Future work could involve exploring *non-linear relationships* and applying the **scaling laws** to other *machine learning tasks*. Additionally, the authors mention the need for further research on the *interpretability* of the **scaling laws** and their potential applications in *real-world scenarios*.

## Practical Applications
The **scaling laws** have potential practical applications in *large-scale pretraining* of foundation models, enabling the efficient estimation of optimal *domain weights* for any target domain. This could lead to *improved performance* and *reduced training costs* in a variety of *real-world applications*, such as *natural language processing*, *computer vision*, and *multimodal learning*. The approach could also be used to *optimize data mixtures* for specific *tasks* or *domains*, leading to more *efficient* and *effective* training procedures.

---

**Authors:** Mustafa Shukor, Louis Bethune, Dan Busbridge, David Grangier, Enrico Fini, Alaaeldin El-Nouby, Pierre Ablin
