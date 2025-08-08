# LongAnimation: Long Animation Generation with Dynamic Global-Local
  Memory

**Paper ID:** 2507.01945

**URL:** https://huggingface.co/papers/2507.01945

## Summary

## Executive Summary
The paper introduces **LongAnimation**, a novel framework for automated long animation colorization, addressing the limitations of existing studies that focus on *short-term* colorization. By proposing a dynamic **global-local paradigm**, the authors aim to achieve ideal *long-term color consistency* through the use of a **SketchDiT**, a **Dynamic Global-Local Memory (DGLM)**, and a **Color Consistency Reward**. This approach enables the *effective* generation of long animations with consistent colorization, reducing the high *labor costs* associated with manual colorization in the real animation industry.

## Key Contributions and Findings
* **Novel Framework**: The authors propose **LongAnimation**, a framework that combines a **SketchDiT**, a **DGLM**, and a **Color Consistency Reward** to achieve *long-term color consistency* in animation colorization.
* **Dynamic Global-Local Paradigm**: The paper introduces a dynamic **global-local paradigm** that *dynamically extracts global color-consistent features* relevant to the current generation, allowing for *smooth transitions* between local segments.
* **Color Consistency Reward**: The authors introduce a **Color Consistency Reward** to refine the *color consistency* of the generated animations, ensuring *coherent* and *visually appealing* results.
* **Extensive Experiments**: The paper presents *extensive experiments* on both *short-term* and *long-term* animations, demonstrating the effectiveness of **LongAnimation** in maintaining *short-term* and *long-term color consistency*.

## Methodology Overview
The methodology involves the use of **bold** components, including a **SketchDiT** that captures *hybrid reference features*, a **DGLM** that *dynamically compresses global historical features* and *adaptively fuses* them with the current generation features, and a **Color Consistency Reward** that refines the *color consistency*. The authors employ *specific techniques*, such as *long video understanding models*, to support the **DGLM** module.

## Results and Performance
The key results show that **LongAnimation** achieves **high color consistency** and **smooth transitions** between video segments, outperforming existing methods in terms of **color consistency metrics**. The authors report *significant improvements* in *long-term color consistency*, with **average metrics** demonstrating the effectiveness of the proposed framework. The results are compared to *state-of-the-art methods*, highlighting the *advantages* of **LongAnimation**.

## Limitations and Future Work
The paper does not explicitly mention limitations, but potential future directions include:
* Exploring the application of **LongAnimation** to other domains, such as *video generation* or *image colorization*
* Investigating the use of *alternative techniques*, such as *generative adversarial networks* or *transformers*, to improve the performance of **LongAnimation**
* Developing more *efficient* and *scalable* methods for *long-term color consistency* in animation colorization

## Practical Applications
The proposed **LongAnimation** framework has potential practical applications in the *real animation industry*, including:
* Automated animation colorization, reducing *labor costs* and increasing *productivity*
* *Consistent* and *high-quality* animation colorization for *film*, *television*, and *video game* production
* *Improved* colorization tools for *animation studios* and *content creators*, enabling the *efficient* generation of *high-quality* animations.

---

**Authors:** Nan Chen, Mengqi Huang, Yihao Meng, Zhendong Mao
