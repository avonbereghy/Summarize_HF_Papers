# Step-3 is Large yet Affordable: Model-system Co-design for
  Cost-effective Decoding

**Paper ID:** 2507.19427

**URL:** https://huggingface.co/papers/2507.19427

## Summary

## Executive Summary
The paper introduces **Step-3**, a 321B-parameter *Very Large Model* (VLM) that achieves unprecedented **cost efficiency** through **hardware-aware model-system co-design**. By innovating in two key dimensions, **Multi-Matrix Factorization Attention (MFA)** and **Attention-FFN Disaggregation (AFD)**, Step-3 significantly reduces *theoretical decoding costs* while maintaining high *attention expressiveness*. This co-design enables Step-3 to activate *38B parameters per token*, outperforming models like **DeepSeek-V3** and **Qwen3 MoE 235B** in terms of *decoding throughput* and *cost-effectiveness*.

## Key Contributions and Findings
* **Novel Attention Mechanism**: Step-3 introduces a novel **Multi-Matrix Factorization Attention (MFA)** mechanism that reduces *KV cache size* and *computation* while maintaining high *attention expressiveness*.
* **Distributed Inference System**: The paper proposes **Attention-FFN Disaggregation (AFD)**, a distributed inference system that decouples *attention* and *Feed-Forward Network (FFN)* layers into specialized subsystems, achieving *unprecedented cost efficiency*.
* **Hardware-Aligned Design**: Step-3's design is optimized for *hardware efficiency*, leveraging *MoE sparsity* and *AFD* to minimize *decoding costs*.
* **State-of-the-Art Performance**: Step-3 achieves a *decoding throughput* of up to **4,039 tokens per second per GPU**, outperforming **DeepSeek-V3** and setting a new *Pareto frontier* for *LLM decoding*.
* **Scalability**: Step-3 demonstrates *scalability* and *cost-effectiveness* even at *longer context lengths*, making it a promising solution for *real-world applications*.

## Methodology Overview
The methodology involves **co-designing** the **Step-3 model** with **hardware-aware optimizations**, including **Multi-Matrix Factorization Attention (MFA)** and **Attention-FFN Disaggregation (AFD)**. The authors use *specific techniques* such as *model parallelism* and *data parallelism* to implement the **AFD** system, and *evaluate* the performance of Step-3 using *benchmarking* and *comparison* with other models.

## Results and Performance
The results show that Step-3 achieves **low decoding costs** while activating *38B parameters per token*, outperforming models like **DeepSeek-V3** and **Qwen3 MoE 235B**. The paper reports a **decoding throughput** of up to **4,039 tokens per second per GPU**, which is *higher* than **DeepSeek-V3**'s *2,324 tokens per second per GPU* in the same setup. Step-3 also demonstrates *better scalability* and *cost-effectiveness* at *longer context lengths*.

## Limitations and Future Work
The paper does not explicitly mention any limitations, but potential future directions include:
* Exploring *further optimizations* to improve **Step-3**'s performance and *cost-effectiveness*
* Investigating the *applicability* of **Step-3** to other *natural language processing tasks*
* Developing *new techniques* to improve the *scalability* and *efficiency* of **Step-3**

## Practical Applications
The **Step-3 model** has potential *real-world applications* in areas such as:
* **Natural Language Processing**: Step-3 can be used for *language translation*, *text summarization*, and *question answering* tasks.
* **Conversational AI**: Step-3 can be integrated into *chatbots* and *virtual assistants* to improve their *language understanding* and *response generation* capabilities.
* **Content Generation**: Step-3 can be used for *content generation* tasks such as *text generation* and *image captioning*.

---

**Authors:** StepFun, Bin Wang, Bojun Wang, Changyi Wan, Guanzhe Huang, Hanpeng Hu, Haonan Jia, Hao Nie, Mingliang Li, Nuo Chen, Siyu Chen, Song Yuan, Wuxun Xie, Xiaoniu Song, Xing Chen, Xingping Yang, Xuelin Zhang, Yanbo Yu, Yaoyu Wang, Yibo Zhu, Yimin Jiang, Yu Zhou, Yuanwei Lu, Houyi Li, Jingcheng Hu, Ka Man Lo, Ailin Huang, Binxing Jiao, Bo Li, Boyu Chen, Changxin Miao, Chang Lou, Chen Hu, Chen Xu, Chenfeng Yu, Chengyuan Yao, Daokuan Lv, Dapeng Shi, Deshan Sun, Ding Huang, Dingyuan Hu, Dongqing Pang, Enle Liu, Fajie Zhang, Fanqi Wan, Gulin Yan, Han Zhang, Han Zhou, Hanghao Wu, Hangyu Guo, Hanqi Chen, Hanshan Zhang, Hao Wu, Haocheng Zhang, Haolong Yan, Haoran Lv, Haoran Wei, Hebin Zhou, Heng Wang, Heng Wang, Hongxin Li, Hongyu Zhou, Hongyuan Wang, Huiyong Guo, Jia Wang, Jiahao Gong, Jialing Xie, Jian Zhou, Jianjian Sun, Jiaoren Wu, Jiaran Zhang, Jiayu Liu, Jie Cheng, Jie Luo, Jie Yan, Jie Yang, Jieyi Hou, Jinguang Zhang, Jinlan Cao, Jisheng Yin, Junfeng Liu, Junhao Huang, Junzhe Lin, Kaijun Tan, Kaixiang Li, Kang An, Kangheng Lin, Kenkun Liu, Lei Yang, Liang Zhao, Liangyu Chen, Lieyu Shi, Liguo Tan, Lin Lin, Lin Zhang, Lina Chen, Liwen Huang, Liying Shi, Longlong Gu, Mei Chen, Mengqiang Ren, Ming Li, Mingzhe Chen, Na Wang, Nan Wu, Qi Han, Qian Zhao, Qiang Zhang, Qianni Liu, Qiaohui Chen, Qiling Wu, Qinglin He, Qinyuan Tan, Qiufeng Wang, Qiuping Wu, Qiuyan Liang, Quan Sun, Rui Li, Ruihang Miao, Ruosi Wan, Ruyan Guo, Shangwu Zhong, Shaoliang Pang, Shengjie Fan, Shijie Shang, Shilei Jiang, Shiliang Yang, Shiming Hao, Shuli Gao, Siming Huang, Siqi Liu, Tiancheng Cao, Tianhao Cheng, Tianhao Peng, Wang You, Wei Ji, Wen Sun, Wenjin Deng, Wenqing He, Wenzhen Zheng, Xi Chen, Xiangwen Kong, Xianzhen Luo, Xiaobo Yang, Xiaojia Liu, Xiaoxiao Ren, Xin Han, Xin Li, Xin Wu, Xu Zhao, Yanan Wei, Yang Li, Yangguang Li, Yangshijie Xu, Yanming Xu, Yaqiang Shi, Yeqing Shen, Yi Yang, Yifei Yang, Yifeng Gong, Yihan Chen, Yijing Yang, Yinmin Zhang, Yizhuang Zhou, Yuanhao Ding, Yuantao Fan, Yuanzhen Yang, Yuchu Luo, Yue Peng, Yufan Lu, Yuhang Deng, Yuhe Yin, Yujie Liu, Yukun Chen, Yuling Zhao, Yun Mou, Yunlong Li, Yunzhou Ju, Yusheng Li, Yuxiang Yang, Yuxiang Zhang, Yuyang Chen, Zejia Weng, Zhe Xie, Zheng Ge, Zheng Gong, Zhenyi Lu, Zhewei Huang, Zhichao Chang, Zhiguo Huang, Zhirui Wang, Zidong Yang, Zili Wang, Ziqi Wang, Zixin Zhang, Binxing Jiao, Daxin Jiang, Heung-Yeung Shum, Xiangyu Zhang
