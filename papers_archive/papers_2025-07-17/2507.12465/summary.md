# PhysX: Physical-Grounded 3D Asset Generation

**Paper ID:** 2507.12465

**URL:** https://huggingface.co/papers/2507.12465

## Summary

## Executive Summary
The paper introduces **PhysX**, a novel paradigm for *physical-grounded* 3D asset generation, aiming to bridge the gap between virtual and physical modeling. By proposing **PhysXNet**, a *physics-annotated* 3D dataset, and **PhysXGen**, a *feed-forward* framework for image-to-3D asset generation, the authors enable the creation of 3D assets with *plausible physical predictions* while preserving native geometry quality. This work has significant implications for *real-world applications* in simulation and *embodied AI*, and the release of code, data, and models will facilitate future research in *generative physical AI*.

## Key Contributions and Findings
* **Physics-Grounded Dataset**: The authors present **PhysXNet**, the first *physics-grounded* 3D dataset, which is systematically annotated across five foundational dimensions: *absolute scale*, *material*, *affordance*, *kinematics*, and *function description*.
* **Efficient Annotation Pipeline**: A scalable *human-in-the-loop* annotation pipeline is devised, leveraging *vision-language models* to efficiently create *physics-first* assets from raw 3D assets.
* **Physics-Grounded Generation Framework**: **PhysXGen** is proposed, a *feed-forward* framework that injects *physical knowledge* into the pre-trained 3D structural space, producing 3D assets with *plausible physical predictions*.
* **Dual-Branch Architecture**: The framework employs a *dual-branch architecture* to explicitly model the *latent correlations* between 3D structures and physical properties.
* **Generalization Capability**: Extensive experiments validate the superior performance and promising *generalization capability* of the framework.

## Methodology Overview
The methodology involves **PhysXNet** dataset creation, which includes a scalable *human-in-the-loop* annotation pipeline using *vision-language models*. The **PhysXGen** framework is then proposed, which consists of a *dual-branch architecture* that models the *latent correlations* between 3D structures and physical properties. The framework is trained using a *feed-forward* approach, enabling the generation of 3D assets with *plausible physical predictions*.

## Results and Performance
The key results show that **PhysXGen** achieves superior performance in terms of **accuracy** and **quality** of generated 3D assets, with *significant improvements* over baseline methods. The framework also demonstrates a promising *generalization capability*, with **high precision** and **recall** rates. The results are compared to *state-of-the-art* methods, highlighting the *advantages* of the proposed approach.

## Limitations and Future Work
The authors mention that the current implementation has limitations in terms of *scalability* and *diversity* of the generated 3D assets. Potential future directions include *expanding the dataset* to include more diverse and complex scenes, and *improving the efficiency* of the annotation pipeline. Additionally, the authors suggest exploring *new applications* of the framework, such as *robotics* and *computer-aided design*.

## Practical Applications
The proposed **PhysX** paradigm has significant implications for *real-world applications* in simulation, *embodied AI*, and *robotics*. The ability to generate 3D assets with *plausible physical predictions* enables more accurate and realistic simulations, which can be used in a variety of fields, such as *architecture*, *product design*, and *video games*. The release of code, data, and models will facilitate future research in *generative physical AI*, enabling the development of more sophisticated and realistic 3D models.

---

**Authors:** Ziang Cao, Zhaoxi Chen, Linag Pan, Ziwei Liu
