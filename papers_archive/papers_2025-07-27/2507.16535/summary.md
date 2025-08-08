# EarthCrafter: Scalable 3D Earth Generation via Dual-Sparse Latent
  Diffusion

**Paper ID:** 2507.16535

**URL:** https://huggingface.co/papers/2507.16535

## Summary

## Executive Summary
The paper introduces **EarthCrafter**, a novel framework for scalable 3D Earth generation, addressing the challenge of modeling large geographic areas. By leveraging a **dual-sparse latent diffusion** approach, the authors propose a tailored architecture that separates *structural* and *textural* generation, enabling efficient and high-quality 3D Earth generation. The framework is built on top of **Aerial-Earth3D**, the largest 3D aerial dataset to date, consisting of *50k curated scenes* with *multi-view images*, *depth maps*, and other relevant data. This innovation enables **large-scale 3D Earth generation** with *geographic plausibility* and supports various applications, including *semantic-guided urban layout generation*.

## Key Contributions and Findings
* **Dual-Sparse Latent Diffusion**: The authors propose a novel approach that combines *dual sparse 3D-VAEs* to compress high-resolution geometric voxels and textural 2D Gaussian Splats (2DGS) into compact latent spaces, alleviating *costly computation* and preserving critical information.
* **Condition-Aware Flow Matching Models**: The paper introduces condition-aware flow matching models trained on *mixed inputs* (semantics, images, or neither) to flexibly model latent geometry and texture features independently, enabling *versatile applications*.
* **Aerial-Earth3D Dataset**: The authors present **Aerial-Earth3D**, the largest 3D aerial dataset to date, consisting of *50k curated scenes* with *multi-view images*, *depth maps*, and other relevant data, providing a rich foundation for *geographic plausibility*.
* **Scalable 3D Earth Generation**: The framework demonstrates **substantial improvements** in extremely large-scale generation, supporting applications such as *unconditional terrain synthesis* and *semantic-guided urban layout generation*.

## Methodology Overview
The methodology involves **two major components**: (1) **Dual-Sparse 3D-VAEs**, which compress high-resolution geometric voxels and textural 2DGS into compact latent spaces using *sparse decoupling*, and (2) **Condition-Aware Flow Matching Models**, which flexibly model latent geometry and texture features independently using *mixed inputs*. The framework also leverages **Aerial-Earth3D** as a foundation for *geographic plausibility*.

## Results and Performance
The paper reports **substantial improvements** in extremely large-scale generation, with **better performance** in terms of *visual quality* and *geographic plausibility*. The framework demonstrates **state-of-the-art results** in *unconditional terrain synthesis* and *semantic-guided urban layout generation*, outperforming existing methods in *quality* and *efficiency*.

## Limitations and Future Work
The paper mentions potential limitations, including:
* The need for **large-scale datasets** to support *geographic plausibility*
* The challenge of **balancing efficiency and quality** in large-scale generation
Future directions may include:
* **Extending the framework** to support *multi-modal inputs* and *more complex scenarios*
* **Improving the efficiency** of the framework using *advanced techniques* such as *parallel processing* or *distributed computing*

## Practical Applications
The **EarthCrafter** framework has potential real-world applications in:
* **Urban planning** and *architecture*, where *semantic-guided urban layout generation* can support the design of *sustainable cities*
* **Environmental monitoring** and *conservation*, where *unconditional terrain synthesis* can help simulate *natural environments* and predict *climate change* impacts
* **Geospatial analysis** and *mapping*, where the framework can support the creation of *high-quality 3D models* for *geographic information systems* (GIS) and *remote sensing* applications.

---

**Authors:** Shang Liu, Chenjie Cao, Chaohui Yu, Wen Qian, Jing Wang, Fan Wang
