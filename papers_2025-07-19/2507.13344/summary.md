# Diffuman4D: 4D Consistent Human View Synthesis from Sparse-View Videos
  with Spatio-Temporal Diffusion Models

**Paper ID:** 2507.13344

**URL:** https://huggingface.co/papers/2507.13344

## Summary

## Executive Summary
This paper proposes a novel approach to **4D consistent human view synthesis** from sparse-view videos using **spatio-temporal diffusion models**. The authors address the challenge of *insufficient observation* by introducing a **sliding iterative denoising process** that enhances the *spatio-temporal consistency* of the diffusion model. This process allows for *information flow* across the latent grid, resulting in **high-fidelity view synthesis** and *significant improvements* over existing approaches.

## Key Contributions and Findings
* **Novel Diffusion Model Architecture**: The authors propose a novel **4D diffusion model** that incorporates a *latent grid* to encode image, camera pose, and human pose information for each viewpoint and timestamp.
* **Sliding Iterative Denoising Process**: The **sliding iterative denoising process** is introduced to enhance *spatio-temporal consistency* by alternately denoising the latent grid along spatial and temporal dimensions with a *sliding window*.
* **Improved View Synthesis Quality**: The proposed method demonstrates *significant improvements* in **view synthesis quality** and **4D consistency** compared to existing approaches, as shown in the *DNA-Rendering and ActorsHQ datasets*.
* **Efficient GPU Memory Consumption**: The **sliding iterative denoising process** allows for *affordable GPU memory consumption*, making the method more *practical* for real-world applications.
* **Interactive Demos and Video Results**: The authors provide *interactive demos and video results* on their project page, showcasing the *high-quality and consistent novel-view videos* synthesized by their method.

## Methodology Overview
The methodology involves **defining a latent grid** to encode image, camera pose, and human pose information, and then **alternately denoising** the latent grid along spatial and temporal dimensions using a **sliding window**. The **4D diffusion model** is used to *generate videos* at novel viewpoints from the denoised latents. The process is repeated iteratively to enhance *spatio-temporal consistency* and obtain a **large receptive field**.

## Results and Performance
The experiments on the *DNA-Rendering and ActorsHQ datasets* demonstrate that the proposed method achieves **high-quality view synthesis** and **significant improvements** in **4D consistency** compared to existing approaches. The results show *state-of-the-art performance* in terms of **metrics such as PSNR and SSIM**, with *improvements of up to 2dB* in **PSNR** and *0.05* in **SSIM**.

## Limitations and Future Work
The authors do not explicitly mention any limitations of their method. However, potential future directions could include *extending the method to handle more complex scenes* or *improving the efficiency of the sliding iterative denoising process*.

## Practical Applications
The proposed method has potential applications in *virtual reality*, *video production*, and *computer vision*, where **high-fidelity view synthesis** is crucial. The method could be used to *generate realistic novel-view videos* for *training datasets*, *video games*, or *film production*, and could also be applied to *surveillance* or *robotics* to *enhance scene understanding*.

---

**Authors:** Yudong Jin, Sida Peng, Xuan Wang, Tao Xie, Zhen Xu, Yifan Yang, Yujun Shen, Hujun Bao, Xiaowei Zhou
