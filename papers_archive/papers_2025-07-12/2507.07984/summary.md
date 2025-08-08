# OST-Bench: Evaluating the Capabilities of MLLMs in Online
  Spatio-temporal Scene Understanding

**Paper ID:** 2507.07984

**URL:** https://huggingface.co/papers/2507.07984

## Summary

## Executive Summary
The paper introduces **OST-Bench**, a benchmark designed to evaluate the capabilities of *multimodal large language models (MLLMs)* in online spatio-temporal scene understanding. This benchmark focuses on the **online** aspect, which requires processing and reasoning over incrementally acquired observations, and the **spatio-temporal** component, which demands integrating current visual inputs with *historical memory* to support dynamic spatial reasoning. The authors evaluate several leading MLLMs on OST-Bench and observe that they struggle with tasks requiring complex *spatio-temporal reasoning*, highlighting the need for improvement in **embodied perception**.

## Key Contributions and Findings
* **Benchmark Introduction**: The authors introduce OST-Bench, a benchmark consisting of *1.4k scenes* and *10k question-answer pairs* collected from *ScanNet*, *Matterport3D*, and *ARKitScenes*, which better reflects the challenges of real-world *embodied perception*.
* **Model Evaluation**: The authors evaluate several leading MLLMs on OST-Bench and observe that they fall short on tasks requiring complex *spatio-temporal reasoning*, with their accuracy declining as the *exploration horizon* extends and the *memory* grows.
* **Error Pattern Analysis**: Through further experimental analysis, the authors identify common *error patterns* across models and find that both complex *clue-based spatial reasoning demands* and *long-term memory retrieval requirements* significantly drop model performance along two separate axes.
* **Dataset and Code Availability**: The authors make their *codes*, *dataset*, and *benchmark* available to foster further research and development in the field.
* **Project Page**: The project page is available at *https://rbler1234.github.io/OSTBench.github.io/*, providing access to the benchmark, dataset, and codes.

## Methodology Overview
The methodology involves **data collection** using an efficient pipeline, which gathers *1.4k scenes* and *10k question-answer pairs* from *ScanNet*, *Matterport3D*, and *ARKitScenes*. The authors then use **benchmark design** to create OST-Bench, which evaluates MLLMs in an **online setting** with *incremental observations* and *historical memory*. The evaluation is performed using *specific techniques*, such as *question-answer pairs* and *accuracy metrics*.

## Results and Performance
The key results show that the evaluated MLLMs achieve **low accuracy** on tasks requiring complex *spatio-temporal reasoning*, with their performance declining as the *exploration horizon* extends and the *memory* grows. The results are summarized using **metrics**, such as *accuracy* and *error rates*, and are compared to *baseline models* using *statistical analysis*. The authors observe that the models struggle with *long-term memory retrieval* and *complex clue-based spatial reasoning*, highlighting the need for improvement in these areas.

## Limitations and Future Work
The limitations of the study include the **limited size of the dataset** and the **restricted scope of the benchmark**, which may not cover all aspects of *embodied perception*. Potential future directions include **expanding the dataset**, **improving the benchmark**, and **developing new models** that can better handle *spatio-temporal reasoning* and *long-term memory retrieval*.

## Practical Applications
The study has potential real-world applications in areas such as **robotics**, **autonomous vehicles**, and **smart homes**, where *embodied perception* and *spatio-temporal reasoning* are crucial for **navigation**, **object recognition**, and **human-robot interaction*. The development of more accurate and efficient MLLMs for online spatio-temporal scene understanding can lead to significant improvements in these areas, enabling more **intelligent** and **autonomous systems*.

---

**Authors:** JingLi Lin, Chenming Zhu, Runsen Xu, Xiaohan Mao, Xihui Liu, Tai Wang, Jiangmiao Pang
