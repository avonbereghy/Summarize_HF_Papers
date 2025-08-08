# Energy-Based Transformers are Scalable Learners and Thinkers

**Paper ID:** 2507.02092

**URL:** https://huggingface.co/papers/2507.02092

## Summary

## Executive Summary
The paper **Energy-Based Transformers are Scalable Learners and Thinkers** introduces a new class of models called **Energy-Based Transformers (EBTs)**, which can learn to think solely from *unsupervised learning*. By assigning an *energy value* to every input and candidate-prediction pair, EBTs enable predictions through *gradient descent-based energy minimization*. This approach allows EBTs to scale faster than existing models, achieving better performance with **System 2 Thinking** and generalizing better to downstream tasks.

## Key Contributions and Findings
* **Scalability**: EBTs scale faster than the dominant **Transformer++** approach during training, achieving an up to *35% higher scaling rate* with respect to data, batch size, parameters, FLOPs, and depth.
* **Performance Improvement**: EBTs improve performance with **System 2 Thinking** by *29% more* than the **Transformer++** on language tasks, and outperform **Diffusion Transformers** on image denoising while using fewer *forward passes*.
* **Generalizability**: EBTs achieve better results than existing models on most downstream tasks given the same or worse *pretraining performance*, suggesting that EBTs generalize better than existing approaches.
* **Energy-Based Modeling**: EBTs are a new class of **Energy-Based Models (EBMs)**, which can learn to explicitly verify the compatibility between inputs and candidate-predictions, and then re-frame prediction problems as optimization with respect to this *verifier*.

## Methodology Overview
The methodology involves training **Energy-Based Transformers (EBTs)** to assign an *energy value* to every input and candidate-prediction pair, enabling predictions through **gradient descent-based energy minimization**. The approach uses *unsupervised learning* and does not require additional supervision or training on top of *unsupervised pretraining*.

## Results and Performance
The key results show that EBTs achieve **up to 35% higher scaling rate** than **Transformer++** during training, and improve performance with **System 2 Thinking** by *29% more* than **Transformer++** on language tasks. EBTs also outperform **Diffusion Transformers** on image denoising while using fewer *forward passes*, with a **29% improvement** in performance.

## Limitations and Future Work
The paper does not mention specific limitations, but potential future directions include exploring the application of EBTs to other *modalities* and *tasks*, and investigating the use of EBTs in *multimodal learning* scenarios.

## Practical Applications
The introduction of EBTs has potential real-world applications in areas such as *natural language processing*, *computer vision*, and *multimodal learning*. EBTs can be used to improve the performance of models in tasks such as language translation, image recognition, and text summarization, and can also be applied to *real-world problems* such as image denoising and data compression.

---

**Authors:** Alexi Gladstone, Ganesh Nanduru, Md Mofijul Islam, Peixuan Han, Hyeonjeong Ha, Aman Chadha, Yilun Du, Heng Ji, Jundong Li, Tariq Iqbal
