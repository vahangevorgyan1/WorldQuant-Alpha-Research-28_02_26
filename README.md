# WorldQuant-Alpha-Research-28_02_26
Quantitative research and automated simulation of alpha signals for the WorldQuant BRAIN platform.
# Quantitative Research: Intraday Price Exhaustion Alpha

This repository documents the research, development, and validation of a long-term mean-reversion signal based on intraday price action. The core research explores the statistical significance of the divergence between a daily midpoint equilibrium and the final settlement price.

## 📐 The Mathematical Model

The alpha is defined by the following expression:

$$Alpha = \text{ts\_rank}\left(\frac{High + Low}{2} - Close, 700\right)$$

### 🔬 Core Components:
1. **Intraday Equilibrium Proxy**: $\frac{High + Low}{2}$ represents the "fair price" or the center of gravity for the day's trading range.
2. **Settlement Bias**: Subtracting the $Close$ price identifies assets that have significantly overshot or undershot this equilibrium by the end of the session.
3. **Normalization (Long-term Stasis)**: The `ts_rank` operator with a **700-day window** (~2.8 trading years) transforms the raw price distance into a stationary percentile. This ensures the model only bets on "extreme" exhaustion events relative to historical volatility.

---

## 🎯 Thematic Focus: Power Pool EUR D1

The research is strictly aligned with the **WorldQuant Power Pool Thematic Competition**. The model is optimized for the following scope to maximize capital efficiency and thematic fit:

* **Region:** Europe (EUR)
* **Universe:** `TOPCS1600` (Top 1600 liquid European equities)
* **Delay:** 1 (D1) – targeting short-term next-day alpha.
* **Active Theme:** EUR TOPCS1600 Power Pool (Multiplier: 2x)

### Adaptation Strategy
To meet the **"Pure Power Pool"** criteria, the mathematical expression was refined to pass the thematic filter while maintaining its core mean-reversion logic. By focusing on the **EUR** region with a **D1 delay**, the alpha captures liquidity-driven price corrections specific to European market hours.

---

## 🛠 Strategic Logic

### 1. Mean Reversion Hypothesis
The signal operates on the premise that extreme deviations from the daily mean are unsustainable. A high positive value suggests the close was much lower than the day's average, signaling a potential oversold condition and a subsequent upward correction.

### 2. Implementation & Neutralization
* **Neutralization:** Statistical (to isolate idiosyncratic alpha from market beta and latent factor risks).
* **Decay:** 1 (Optimized for D1 delay to capture immediate mean reversion).

---

## 📊 Performance & Constraints Analysis

To qualify as a **Power Pool Alpha**, this model is optimized under the following strict mathematical constraints:

| Criterion | Value / Limit | Status |
| :--- | :--- | :--- |
| **Operator Complexity** | 2 unique operators | ✅ Pass |
| **Data Field Count** | 3 (High, Low, Close) | ✅ Pass |
| **Information Decay** | 700-day lookback | ✅ Robust |
| **Sharpe Ratio** | $\ge 1.0$ | ✅ Target |
| **Self-Correlation** | $< 0.5$ | ✅ Pass |

---

## 🛠 Project Structure
* `alpha_generator.py` — Python script interfacing with WorldQuant Brain API for automated simulation.
* `ace_lib.py` — Core library for session management and multi-threaded simulation.
* `analysis/` — Notebooks evaluating signal decay and performance metrics.

---

## ⚠️ Disclaimer
This repository is for educational and research purposes only. Actual alpha expressions and credentials are kept confidential and protected by environment variables.
