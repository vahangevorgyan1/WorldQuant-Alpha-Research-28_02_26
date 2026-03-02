## 📐 The Mathematical Model

The final alpha expression utilizes a multi-stage pipeline to process price-action bias:

$$Alpha = ts\_rank(group\_rank(group\_zscore(\frac{\frac{High + Low}{2} - Close}{Close}, group), group), T)$$

### Logical Architecture:
1. **Normalized Settlement Bias**: Measuring the distance between the daily midpoint $(High + Low) / 2$ and $Close$, scaled by price to ensure cross-sectional comparability.
2. **Hierarchical Normalization**:
   - `group_zscore(group)`: First-stage risk cleaning. Evaluates asset deviation relative to its specific group volatility (e.g., country-level).
   - `group_rank(group)`: Second-stage refinement. Identifies relative "winners" and "losers" within peer groups (e.g., industry-level), making the signal robust against sector-wide shocks.
3. **Temporal Stationarity**: A 700-day `ts_rank` window ensures the signal captures historically significant exhaustion events rather than high-frequency noise.
