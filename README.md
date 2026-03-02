# Quantitative Research: Hierarchical Price Exhaustion Alpha

This repository documents the systematic research, development, and optimization of a statistical arbitrage signal for the WorldQuant BRAIN platform. The project focuses on identifying intraday price anomalies through multi-level group normalization and long-term stationarity filters.

## 📐 The Mathematical Model

The final alpha expression utilizes a multi-stage pipeline to process price-action bias:

$$Alpha = \text{ts\_rank}(\text{group\_rank}(\text{group\_zscore}(\frac{\frac{High + Low}{2} - Close}{Close}, \text{group}), \text{group}), T)$$

### Logical Architecture:
1. **Normalized Settlement Bias**: Measuring the distance between the daily midpoint $(High+Low)/2$ and $Close$, scaled by price to ensure cross-sectional comparability.
2. **Hierarchical Normalization**:
   - `group\_zscore(group)`: First-stage risk cleaning. Evaluates asset deviation relative to its specific group volatility.
   - `group\_rank(group)`: Second-stage refinement. Identifies relative "winners" and "losers" within peer groups.
3. **Temporal Stationarity**: A 700-day `ts\_rank` window ensures the signal captures historically significant exhaustion events.

---

## 🔬 Research & Optimization (Grid Search)

The model parameters were selected via an exhaustive **Grid Search** across a 4-dimensional parameter space $\Omega$:
- **Groups**: `[country, industry, subindustry, sector]`
- **Lookback (T)**: `[20:1000]` with step 50.
- **Decay**: `[10:110]` with step 10.
- **Neutralization**: `[market, industry, sector, statistical, crowding]`.

### Key Findings:
- **Optimal Decay (110)**: Increasing decay significantly reduced Turnover to the 32% range while maintaining a high Sharpe Ratio.
- **Group Synergy**: The combination of `industry` ranking and `statistical` neutralization provided the cleanest idiosyncratic alpha.

---

## 🎯 Thematic Focus: EUR D1 Power Pool

The research is optimized for the **WorldQuant Power Pool Thematic Competition (EUR/D1/PV)**:
- **Region**: Europe (EUR)
- **Universe**: `TOPCS1600` (Highly liquid European equities)
- **Delay**: 1 (D1)
- **Multiplier**: 1.1x

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
- `research_grid_search.py`: Core optimization engine and batch simulation script.
- `ace_lib.py`: Session management and multi-threaded API integration.
- `results/`: CSV exports of the parameter search space.

---

## ⚠️ Disclaimer
Educational and research purposes only. Actual alpha credentials and environment configurations are excluded for security.
