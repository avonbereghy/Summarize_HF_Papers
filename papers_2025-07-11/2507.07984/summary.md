# OST-Bench: Evaluating the Capabilities of MLLMs in Online
  Spatio-temporal Scene Understanding

**Paper ID:** 2507.07984

**URL:** https://huggingface.co/papers/2507.07984

## Summary

## Executive Summary
The paper introduces **OST-Bench**, a benchmark designed to evaluate the capabilities of *multimodal large language models (MLLMs)* in online spatio-temporal scene understanding. The benchmark emphasizes the need for models to process and reason over *incrementally acquired observations* in an **online** setting, integrating current visual inputs with *historical memory* to support **dynamic spatial reasoning**. The authors evaluate several leading MLLMs on OST-Bench and observe that they *fall short* on tasks requiring **complex spatio-temporal reasoning**, highlighting the challenges of *real-world embodied perception*.

## Key Contributions and Findings
* **Benchmark Introduction**: The authors introduce OST-Bench, a benchmark consisting of *1.4k scenes* and *10k question-answer pairs* collected from *ScanNet*, *Matterport3D*, and *ARKitScenes*.
* **Model Evaluation**: The authors evaluate several leading MLLMs on OST-Bench and observe that they *struggle* with tasks requiring **complex clue-based spatial reasoning** and *long-term memory retrieval*.
* **Error Pattern Analysis**: The authors identify *common error patterns* across models and find that both **complex spatial reasoning demands** and *long-term memory retrieval requirements* significantly *drop model performance*.
* **Dataset and Code Availability**: The authors make their *codes*, *dataset*, and *benchmark* available to *foster further research and development* in the field.
* **Project Page**: The authors provide a *project page* with more information about OST-Bench and their research.

## Methodology Overview
The methodology involves **data collection** using an *efficient data collection pipeline*, **benchmark design** with a focus on **online spatio-temporal understanding**, and **model evaluation** using several leading MLLMs. The authors employ *specific techniques* such as **incremental observation processing** and *historical memory integration* to support **dynamic spatial reasoning**.

## Results and Performance
The key results show that the evaluated MLLMs achieve **low accuracy** on tasks requiring **complex spatio-temporal reasoning**, with *accuracy declining* as the **exploration horizon extends** and the **memory grows**. The authors report **significant drops in model performance** along two separate axes: **complex spatial reasoning demands** and *long-term memory retrieval requirements*.

## Limitations and Future Work
The authors mention the following limitations and potential future directions:
* **Limited model capacity**: The evaluated MLLMs may not have the capacity to handle **complex spatio-temporal reasoning** tasks.
* **Insufficient training data**: The models may not have been trained on sufficient *diverse and representative data* to handle **online spatio-temporal understanding** tasks.
* **Future research directions**: The authors suggest exploring *new model architectures* and *training methods* to improve **online embodied reasoning** capabilities.

## Practical Applications
The research has potential real-world applications in areas such as:
* **Robotics**: **Online spatio-temporal understanding** is crucial for robots to navigate and interact with their environment.
* **Autonomous vehicles**: **Dynamic spatial reasoning** is essential for autonomous vehicles to safely navigate through complex scenes.
* **Virtual reality**: **Embodied perception** is critical for creating immersive and interactive virtual reality experiences.
* **Healthcare**: **Online spatio-temporal understanding** can be applied to *medical diagnosis* and *treatment* by analyzing *medical images* and *patient data* over time.

---

**Authors:** JingLi Lin, Chenming Zhu, Runsen Xu, Xiaohan Mao, Xihui Liu, Tai Wang, Jiangmiao Pang
