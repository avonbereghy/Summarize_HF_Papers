# EarthCrafter: Scalable 3D Earth Generation via Dual-Sparse Latent
  Diffusion

**Paper ID:** 2507.16535

**URL:** https://huggingface.co/papers/2507.16535

## Summary

## Executive Summary
The **EarthCrafter** framework is a novel approach to scalable 3D Earth generation, addressing the challenge of modeling large geographic areas. By introducing the **Aerial-Earth3D** dataset, the largest 3D aerial dataset to date, and proposing a *dual-sparse latent diffusion* model, the authors enable efficient and high-quality generation of 3D Earth surfaces. The framework separates *structural and textural generation*, using **dual sparse 3D-VAEs** and *condition-aware flow matching models* to preserve critical information while reducing computational costs. This approach supports versatile applications, including *semantic-guided urban layout generation* and *unconditional terrain synthesis*, while maintaining *geographic plausibility*.

## Key Contributions and Findings
* **Large-Scale Dataset Introduction**: The authors introduce the **Aerial-Earth3D** dataset, consisting of *50k curated scenes* and *45M multi-view Google Earth frames*, providing a foundation for large-scale 3D Earth generation.
* **Dual-Sparse Latent Diffusion Model**: The proposed **EarthCrafter** framework uses *dual sparse 3D-VAEs* to compress high-resolution geometric voxels and textural 2D Gaussian Splats (2DGS) into compact latent spaces, alleviating costly computations.
* **Condition-Aware Flow Matching Models**: The authors propose *condition-aware flow matching models* trained on mixed inputs to flexibly model latent geometry and texture features independently, enabling versatile applications.
* **Geographic Plausibility**: The framework maintains *geographic plausibility* through rich data priors from **Aerial-Earth3D**, ensuring generated 3D Earth surfaces are realistic and diverse.
* **Scalability and Efficiency**: The **EarthCrafter** framework demonstrates substantial improvements in *extremely large-scale generation*, supporting efficient and high-quality generation of 3D Earth surfaces.

## Methodology Overview
The methodology involves **two major components**: the **Aerial-Earth3D** dataset and the **EarthCrafter** framework. The **Aerial-Earth3D** dataset provides a foundation for large-scale 3D Earth generation, while the **EarthCrafter** framework uses *dual-sparse latent diffusion* to separate *structural and textural generation*. The framework employs **dual sparse 3D-VAEs** and *condition-aware flow matching models* to preserve critical information and reduce computational costs.

## Results and Performance
The **EarthCrafter** framework demonstrates substantial improvements in **generation quality** and **efficiency**, outperforming existing methods in *extremely large-scale generation*. The framework achieves **state-of-the-art results** in terms of *visual quality* and *geographic plausibility*, with *significant reductions* in computational costs. The authors report **impressive metrics**, including *high-resolution geometric voxel reconstruction* and *textural 2D Gaussian Splat (2DGS) synthesis*, showcasing the framework's capabilities.

## Limitations and Future Work
The authors mention potential **limitations**, including:
* The need for *large-scale datasets* to support training and evaluation
* The challenge of *balancing structural and textural generation* for optimal results
* The potential for *mode collapse* or *lack of diversity* in generated 3D Earth surfaces
Future work may involve exploring *new architectures* or *techniques* to address these limitations and further improve the **EarthCrafter** framework.

## Practical Applications
The **EarthCrafter** framework has significant implications for various fields, including:
* **Urban planning** and *urban design*, where *semantic-guided urban layout generation* can support the creation of realistic and functional city layouts
* **Geographic information systems (GIS)**, where *unconditional terrain synthesis* can enable the generation of realistic 3D terrain models
* **Computer-aided design (CAD)** and *architecture*, where *high-quality 3D Earth surface generation* can support the creation of realistic and detailed models
* **Environmental modeling** and *simulation*, where *geographic plausibility* and *realism* are crucial for accurate predictions and decision-making.

---

**Authors:** Shang Liu, Chenjie Cao, Chaohui Yu, Wen Qian, Jing Wang, Fan Wang
