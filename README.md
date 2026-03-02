# Quantitative Research: Hierarchical Price Exhaustion Alpha

This repository documents the systematic research, development, and optimization of a statistical arbitrage signal for the WorldQuant BRAIN platform. The project focuses on identifying intraday price anomalies through multi-level group normalization and long-term stationarity filters.

## 📐 The Mathematical Model

The final alpha expression utilizes a multi-stage pipeline to process price-action bias:

$$Alpha = ts\_rank(group\_rank(group\_zscore(\frac{\frac{High + Low}{2} - Close}{Close}, group), group), T)$$

### Logical Architecture:
1. **Normalized Settlement Bias**: Measuring the distance between the daily midpoint $(High + Low) / 2$ and $Close$, scaled by price to ensure cross-sectional comparability.
2. **Hierarchical Normalization**:
   - `group_zscore(group)`: First-stage risk cleaning. Evaluates asset deviation relative to its specific group volatility (e.g., country-level).
   - `group_rank(group)`: Second-stage refinement. Identifies relative "winners" and "losers" within peer groups (e.g., industry-level), making the signal robust against sector-wide shocks.
3. **Temporal Stationarity**: A 700-day `ts_rank` window ensures the signal captures historically significant exhaustion events rather than high-frequency noise.
---

## 🔬 Research & Optimization (Grid Search)

The model parameters were selected via an exhaustive **Grid Search** across a 4-dimensional parameter space $\Omega$:
* **Groups**: `[country, industry, subindustry, sector]`
* **Lookback (T)**: `[20:1000]` with a step of 50.
* **Decay**: `[10:110]` with a step of 10.
* **Neutralization**: `[market, industry, sector, statistical, crowding]`.
---

## 🎯 Thematic Focus: EUR D1 Power Pool

The research is strictly aligned with the **WorldQuant Power Pool Thematic Competition (EUR/D1/PV)**:
* **Region**: Europe (EUR)
* **Universe**: `TOPCS1600` (Highly liquid European equities)
* **Delay**: 1 (D1)
---

## 📊 Performance Metrics

The submitted alpha achieved the following verified results:

| Metric | Value | Cutoff | Result |
| :--- | :--- | :--- | :--- |
| **Sharpe Ratio** | **2.24** | 1.58 | ✅ Pass |
| **2-Year Sharpe** | **1.70** | 1.58 | ✅ Pass |
| **Fitness** | **1.00** | 1.00 | ✅ Pass |
| **Turnover** | **32.22%** | 1% - 70% | ✅ Pass |
| **Robust Universe Sharpe** | **1.28** | 0.70 | ✅ Pass |

---

## 🛠 Project Structure
* `research_grid_search.py`: Core optimization engine and batch simulation script.
* `ace_lib.py`: Session management and multi-threaded API integration.
* `helpful_functions.py`: Data normalization and result formatting utilities.
* `results/`: CSV exports of the parameter search space.

---
