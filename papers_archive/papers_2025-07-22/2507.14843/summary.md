# The Invisible Leash: Why RLVR May Not Escape Its Origin

**Paper ID:** 2507.14843

**URL:** https://huggingface.co/papers/2507.14843

## Summary

## Executive Summary
The paper **The Invisible Leash: Why RLVR May Not Escape Its Origin** presents a theoretical and empirical investigation into the potential limits of **Reinforcement Learning with Verifiable Rewards (RLVR)**, a promising method for enhancing AI's capabilities in solving complex logical tasks. The study reveals that RLVR is *constrained by the base model's support*, operating as a *conservative reweighting mechanism* that may restrict the discovery of entirely original solutions. The authors identify an *entropy-reward tradeoff*, where RLVR reliably enhances *precision*, but may progressively narrow *exploration* and potentially overlook correct yet *underrepresented solutions*.

## Key Contributions and Findings
* **Theoretical Perspective**: The authors offer a new theoretical perspective that RLVR is *constrained by the base model's support*, unable to sample solutions with zero initial probability, and operates as a *conservative reweighting mechanism*.
* **Entropy-Reward Tradeoff**: The study identifies an *entropy-reward tradeoff*, where RLVR reliably enhances *precision*, but may progressively narrow *exploration* and potentially overlook correct yet *underrepresented solutions*.
* **Empirical Validation**: Extensive empirical experiments validate that while RLVR consistently improves **pass@1**, the *shrinkage of empirical support* generally outweighs the expansion of empirical support under larger sampling budgets.
* **Limitations of RLVR**: The findings reveal potential limits of RLVR in extending *reasoning horizons*, suggesting that breaking this *invisible leash* may require future algorithmic innovations such as *explicit exploration mechanisms* or *hybrid strategies*.

## Methodology Overview
The methodology involves **theoretical analysis** and **empirical experiments** using *large reasoning models* and *Reinforcement Learning with Verifiable Rewards (RLVR)*. The authors employ **sampling techniques** and *entropy calculations* to investigate the potential limits of RLVR.

## Results and Performance
The key results show that RLVR consistently improves **pass@1**, but the *shrinkage of empirical support* generally outweighs the expansion of empirical support under larger sampling budgets. The study also finds that while RLVR sometimes increases *token-level entropy*, resulting in greater *uncertainty* at each generation step, **answer-level entropy** declines, indicating that these seemingly more uncertain paths ultimately converge onto a smaller set of distinct answers.

## Limitations and Future Work
The limitations mentioned include the potential for RLVR to overlook correct yet *underrepresented solutions* and the need for future algorithmic innovations to break the *invisible leash*. Potential future directions include exploring *explicit exploration mechanisms* or *hybrid strategies* to seed probability mass into *underrepresented solution regions*.

## Practical Applications
The study has potential implications for **AI reasoning capabilities** and **complex logical task solving**. The findings suggest that RLVR may not be sufficient to extend *reasoning horizons* and that future innovations are needed to improve AI's capabilities in these areas. Potential real-world applications include **natural language processing**, **decision-making systems**, and **expert systems**, where the ability to solve complex logical tasks is crucial.

---

**Authors:** Fang Wu, Weihao Xuan, Ximing Lu, Zaid Harchaoui, Yejin Choi
