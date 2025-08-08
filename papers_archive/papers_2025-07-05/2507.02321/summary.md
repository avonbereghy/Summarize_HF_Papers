# Heeding the Inner Voice: Aligning ControlNet Training via Intermediate
  Features Feedback

**Paper ID:** 2507.02321

**URL:** https://huggingface.co/papers/2507.02321

## Summary

## Executive Summary
The paper introduces **InnerControl**, a novel training strategy that enhances the performance of text-to-image diffusion models by enforcing spatial consistency across all diffusion steps. By utilizing *lightweight convolutional probes* to reconstruct input control signals from intermediate *UNet features*, the method improves both control fidelity and generation quality. The proposed approach addresses the limitations of existing methods, such as **ControlNet** and **ControlNet++**, by incorporating *pseudo ground truth controls* throughout the entire diffusion process, ultimately achieving **state-of-the-art performance** across diverse conditioning methods.

## Key Contributions and Findings
* **Improved Control Fidelity**: InnerControl enhances the accuracy of generated outputs by minimizing the discrepancy between predicted and target conditions throughout the diffusion process, allowing for *precise spatial control*.
* **Efficient Signal Extraction**: The use of *lightweight convolutional probes* enables efficient extraction of control signals from *highly noisy latents*, making it possible to train the model with *pseudo ground truth controls*.
* **Enhanced Generation Quality**: By enforcing spatial consistency across all diffusion steps, InnerControl improves the overall quality of generated images, demonstrating *superior performance* compared to existing methods.
* **Flexibility and Compatibility**: The proposed approach can be combined with established techniques, such as **ControlNet++**, and is applicable to various conditioning methods, including *edges* and *depth*.

## Methodology Overview
The methodology involves **training** a text-to-image diffusion model using **InnerControl**, which consists of **lightweight convolutional probes** that reconstruct input control signals from intermediate *UNet features* at every *denoising step*. The probes are trained to minimize the discrepancy between predicted and target conditions, allowing for *pseudo ground truth controls* to be used throughout the diffusion process. The approach utilizes *cycle consistency loss* and *alignment loss* to refine the model's performance.

## Results and Performance
The results demonstrate that **InnerControl** achieves **state-of-the-art performance** across diverse conditioning methods, with **improved metrics** such as *peak signal-to-noise ratio (PSNR)* and *structural similarity index (SSIM)*. The approach shows *superior performance* compared to existing methods, including **ControlNet** and **ControlNet++**, and is applicable to various *conditioning methods*, such as *edges* and *depth*.

## Limitations and Future Work
The paper does not explicitly mention limitations, but potential future directions include:
* Exploring the application of **InnerControl** to other types of generative models
* Investigating the use of *different architectures* for the convolutional probes
* Evaluating the performance of **InnerControl** on more complex and diverse datasets

## Practical Applications
The proposed approach has potential real-world applications in areas such as:
* **Image editing** and **manipulation**, where precise spatial control is crucial
* **Computer vision** tasks, such as object detection and segmentation, where accurate generation of images is essential
* **Artistic creation**, where the ability to generate high-quality images with precise control can be beneficial for artists and designers.

---

**Authors:** Nina Konovalova, Maxim Nikolaev, Andrey Kuznetsov, Aibek Alanov
