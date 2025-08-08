# BANG: Dividing 3D Assets via Generative Exploded Dynamics

**Paper ID:** 2507.21493

**URL:** https://huggingface.co/papers/2507.21493

## Summary

## Executive Summary
The paper introduces **BANG**, a novel generative approach that bridges 3D generation and reasoning, allowing for intuitive and flexible part-level decomposition of 3D objects. At its core, BANG utilizes *Generative Exploded Dynamics*, which creates a smooth sequence of exploded states for an input geometry, progressively separating parts while preserving their geometric and semantic coherence. This approach enables **precise control** over the decomposition process, and can be extended with *multimodal models* for more intuitive and creative workflows. By leveraging **large-scale latent diffusion models** and *temporal attention modules*, BANG enhances control with *spatial prompts*, enabling users to specify which parts to decompose and how.

## Key Contributions and Findings
* **Generative Approach**: BANG introduces a novel generative approach that combines 3D generation and reasoning, allowing for intuitive and flexible part-level decomposition of 3D objects, with a focus on *geometric and semantic coherence*.
* **Exploded Dynamics**: The paper proposes *Generative Exploded Dynamics*, which creates a smooth sequence of exploded states for an input geometry, progressively separating parts while preserving their *geometric and semantic properties*.
* **Control and Interaction**: BANG enables **precise control** over the decomposition process, and can be extended with *multimodal models* for more intuitive and creative workflows, including *2D-to-3D manipulations*.
* **Applications and Implications**: The capabilities of BANG extend to generating detailed part-level geometry, associating parts with *functional descriptions*, and facilitating *component-aware 3D creation and manufacturing workflows*.
* **Future Directions**: The paper highlights the potential for BANG to be used in various applications, including *3D printing*, where separable parts are generated for easy printing and reassembly, and *multimodal interactions*, enabling more intuitive and creative workflows.

## Methodology Overview
The methodology of BANG involves **large-scale latent diffusion models**, which are fine-tuned for *exploded dynamics* with a *lightweight exploded view adapter*. The approach also incorporates a **temporal attention module** to ensure smooth transitions and consistency across time. Additionally, BANG utilizes *spatial prompts*, such as *bounding boxes* and *surface regions*, to enable users to specify which parts to decompose and how.

## Results and Performance
The key results of BANG demonstrate its ability to generate high-quality, detailed part-level geometry, with **high accuracy** and **efficiency**. The approach is also shown to be **flexible** and **intuitive**, allowing users to control the decomposition process with *spatial prompts* and *multimodal interactions*. In comparison to other methods, BANG achieves *state-of-the-art results* in terms of **quality** and **efficiency**, making it a promising approach for various applications.

## Limitations and Future Work
The paper mentions several limitations, including the need for **large-scale training data** and the potential for *mode collapse* in the generative model. Future directions include exploring the use of BANG in various applications, such as *3D printing* and *computer-aided design*, and improving the **efficiency** and **accuracy** of the approach.

## Practical Applications
The practical applications of BANG are numerous, including *3D printing*, where separable parts are generated for easy printing and reassembly, and *computer-aided design*, where BANG can be used to generate detailed part-level geometry and facilitate *component-aware 3D creation and manufacturing workflows*. Additionally, BANG has the potential to be used in various other fields, such as *architecture*, *product design*, and *video game development*, where intuitive and flexible part-level decomposition of 3D objects is essential.

---

**Authors:** Longwen Zhang, Qixuan Zhang, Haoran Jiang, Yinuo Bai, Wei Yang, Lan Xu, Jingyi Yu
