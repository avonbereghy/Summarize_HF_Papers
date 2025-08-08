# SpeakerVid-5M: A Large-Scale High-Quality Dataset for Audio-Visual
  Dyadic Interactive Human Generation

**Paper ID:** 2507.09862

**URL:** https://huggingface.co/papers/2507.09862

## Summary

## Executive Summary
The paper introduces **SpeakerVid-5M**, a large-scale, high-quality dataset designed for *audio-visual dyadic interactive virtual human generation*. This dataset contains over 5.2 million video clips of human portraits, covering diverse scales and interaction types, including *monadic talking*, *listening*, and *dyadic conversations*. The dataset is structured along two key dimensions: **interaction type** and **data quality**, making it suitable for a wide array of *2D virtual human tasks*. The authors also provide an *autoregressive (AR)-based video chat baseline* trained on this data, accompanied by a dedicated set of *metrics and test data* to serve as a benchmark **VidChatBench** for future work.

## Key Contributions and Findings
* **Dataset Creation**: The authors created a large-scale dataset, **SpeakerVid-5M**, which contains over 5.2 million video clips of human portraits, covering *diverse scales and interaction types*.
* **Dual Structure**: The dataset is structured along two key dimensions: **interaction type** and **data quality**, allowing for *flexible and efficient* use in various *virtual human tasks*.
* **Baseline Model**: The authors provide an *autoregressive (AR)-based video chat baseline* trained on this data, which serves as a starting point for future research and development.
* **Benchmarking**: The authors introduce **VidChatBench**, a dedicated set of *metrics and test data*, to evaluate and compare the performance of different models and approaches.
* **Public Release**: The dataset and corresponding *data processing code* will be publicly released, facilitating *collaboration and innovation* in the field.

## Methodology Overview
The methodology involves **data collection** and **processing**, where the authors gathered and annotated a large-scale dataset of video clips. They employed *specific techniques*, such as *video encoding* and *quality control*, to ensure the dataset's **quality and consistency**. The dataset is then structured into a **large-scale pre-training subset** and a **curated, high-quality subset** for *Supervised Fine-Tuning (SFT)*.

## Results and Performance
The authors report **impressive results** with their *autoregressive (AR)-based video chat baseline* model, which achieves **high-quality video generation** and *realistic audio-visual synchronization*. The model's performance is evaluated using **metrics**, such as *peak signal-to-noise ratio (PSNR)* and *structural similarity index (SSIM)*, and compared to *state-of-the-art models*.

## Limitations and Future Work
The authors mention **limitations** in terms of *dataset size and diversity*, and suggest potential future directions, such as *collecting more data* and *exploring new interaction types*. They also encourage *future research* to focus on **improving the model's performance** and *developing new applications* for the **SpeakerVid-5M** dataset.

## Practical Applications
The **SpeakerVid-5M** dataset has potential *real-world applications* in areas such as **virtual reality**, **video conferencing**, and **human-computer interaction*. The dataset can be used to develop more *realistic and engaging* virtual humans, and to improve the overall *user experience* in various *interactive applications*. The authors' work can also contribute to the development of *more sophisticated* *virtual assistants* and *chatbots*, which can *simulate human-like conversations* and *interactions*.

---

**Authors:** Youliang Zhang, Zhaoyang Li, Duomin Wang, Jiahe Zhang, Deyu Zhou, Zixin Yin, Xili Dai, Gang Yu, Xiu Li
