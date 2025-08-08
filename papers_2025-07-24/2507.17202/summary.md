# DesignLab: Designing Slides Through Iterative Detection and Correction

**Paper ID:** 2507.17202

**URL:** https://huggingface.co/papers/2507.17202

## Summary

## Executive Summary
The proposed system, **DesignLab**, aims to improve the quality of presentation slides by separating the design process into two roles: the **design reviewer** and the **design contributor**. This decomposition enables an iterative loop where the reviewer continuously detects *design-related issues* and the contributor corrects them, allowing a draft to be further polished with each iteration. By fine-tuning *large language models* for these roles, **DesignLab** can produce polished, professional slides that outperform existing *design-generation methods*.

## Key Contributions and Findings
* **Design Process Decomposition**: Separating the design process into two roles enables an iterative loop that refines the design quality through continuous *detection and correction* of issues.
* **Role-Specific Model Fine-Tuning**: Fine-tuning *large language models* for the **design reviewer** and **design contributor** roles allows the system to learn *design errors* and *correction strategies*.
* **Simulation of Intermediate Drafts**: Introducing controlled *perturbations* to simulate intermediate drafts enables the system to learn from *iterative refinement* and improve the overall design quality.
* **Comparison to Existing Methods**: **DesignLab** outperforms existing *design-generation methods*, including a commercial tool, by embracing the *iterative nature* of designing.
* **Polished and Professional Output**: The system can produce *high-quality* presentation slides that meet professional standards.

## Methodology Overview
The methodology involves **fine-tuning** *large language models* for the **design reviewer** and **design contributor** roles. The system uses **controlled perturbations** to simulate *intermediate drafts* and enable the models to learn from *iterative refinement*. The **design reviewer** model is trained to detect *design-related issues*, while the **design contributor** model is trained to correct them.

## Results and Performance
The key results show that **DesignLab** outperforms existing *design-generation methods* in terms of **quality** and **professionalism**. The system achieves **high accuracy** in detecting *design errors* and **effectiveness** in correcting them. In comparison to a commercial tool, **DesignLab** produces *more polished* and *professional-looking* slides, with **significant improvements** in *layout* and *color scheme*.

## Limitations and Future Work
The limitations of the study include the need for further *evaluation* and *testing* of the system. Potential future directions include *expanding the system* to support more *design elements* and *integrating with other tools* to enhance the overall design workflow.

## Practical Applications
The practical applications of **DesignLab** include *automating the design process* for non-experts, *improving the quality* of presentation slides, and *enhancing the productivity* of designers. The system can be used in various *real-world scenarios*, such as *business presentations*, *academic conferences*, and *marketing campaigns*. By providing a *user-friendly* and *intuitive* interface, **DesignLab** can make *high-quality design* accessible to a wider range of users.

---

**Authors:** Jooyeol Yun, Heng Wang, Yotaro Shimose, Jaegul Choo, Shingo Takamatsu
