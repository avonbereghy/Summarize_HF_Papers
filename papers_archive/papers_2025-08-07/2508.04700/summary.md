# SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from
  Experience

**Paper ID:** 2508.04700

**URL:** https://huggingface.co/papers/2508.04700

## Summary

## Executive Summary
The proposed **SEAgent** framework enables computer-use agents to autonomously evolve through interactions with unfamiliar software, leveraging *experiential learning* to master novel software environments. By utilizing a **World State Model** and a **Curriculum Generator**, the agent can explore new software, learn through iterative trial-and-error, and progressively tackle auto-generated tasks. This approach allows the agent to develop a stronger *generalist* capability, ultimately achieving performance surpassing ensembles of individual **specialist agents**. The **SEAgent** framework has the potential to revolutionize the field of computer-use agents by enabling them to adapt to new software environments without requiring *human-labeled data*.

## Key Contributions and Findings
* **Autonomous Learning**: The **SEAgent** framework enables computer-use agents to autonomously learn from experience, allowing them to adapt to new software environments without requiring *human annotations*.
* **Experiential Learning**: The agent's policy is updated through *experiential learning*, which includes *adversarial imitation* of failure actions and **Group Relative Policy Optimization (GRPO)** on successful ones.
* **Specialist-to-Generalist Training**: The introduction of a *specialist-to-generalist* training strategy facilitates the development of a stronger **generalist** CUA, capable of continuous autonomous evolution.
* **Performance Improvement**: The **SEAgent** framework achieves a significant improvement of *23.2%* in success rate, from *11.3%* to *34.5%*, over a competitive open-source CUA, **UI-TARS**.
* **Scalability**: The framework is validated across *five novel software environments* within **OS-World**, demonstrating its scalability and potential for real-world applications.

## Methodology Overview
The **SEAgent** framework consists of several major components, including a **World State Model** for step-wise trajectory assessment, a **Curriculum Generator** for generating increasingly diverse and challenging tasks, and an *experiential learning* mechanism for updating the agent's policy. The framework utilizes *adversarial imitation* and **GRPO** to learn from failure and success, respectively. The *specialist-to-generalist* training strategy is also employed to integrate individual experiential insights from **specialist agents**.

## Results and Performance
The **SEAgent** framework achieves a significant improvement in **success rate**, with a *23.2%* increase from *11.3%* to *34.5%*, compared to **UI-TARS**. The framework also demonstrates its ability to adapt to new software environments, with a *significant improvement* in performance across *five novel software environments* within **OS-World**. The results are compared to *state-of-the-art* methods, highlighting the **SEAgent** framework's potential for real-world applications.

## Limitations and Future Work
The paper does not explicitly mention any limitations of the **SEAgent** framework. However, potential future directions may include:
* Exploring the application of the **SEAgent** framework to other domains, such as *robotics* or *natural language processing*.
* Investigating the use of *transfer learning* to adapt the **SEAgent** framework to new software environments.
* Developing more advanced *experiential learning* mechanisms to improve the agent's ability to learn from experience.

## Practical Applications
The **SEAgent** framework has several potential real-world applications, including:
* **Automated software testing**: The framework can be used to automate the testing of new software environments, reducing the need for *human annotations* and improving the efficiency of the testing process.
* **Intelligent tutoring systems**: The **SEAgent** framework can be used to develop intelligent tutoring systems that can adapt to individual users' needs and provide personalized feedback.
* **Human-computer interaction**: The framework can be used to improve human-computer interaction by enabling computers to learn from experience and adapt to new software environments.

---

**Authors:** Zeyi Sun, Ziyu Liu, Yuhang Zang, Yuhang Cao, Xiaoyi Dong, Tong Wu, Dahua Lin, Jiaqi Wang
