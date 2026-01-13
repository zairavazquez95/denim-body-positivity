# denim-body-positivity

# Style Signals: Algorithmic Analysis of the "Thin" Resurgence

> **"Can we predict the silhouette of next season's denim by analyzing the search volume of pharmaceutical weight loss?"**

## OUTCOME: The Data Visualization
<img width="1158" height="643" alt="bodypostivity - denim" src="https://github.com/user-attachments/assets/08446167-d30c-4392-85d1-382639ec11a6" />
*Figure 1: Normalized search interest (2020–2026) showing the inverse correlation between societal acceptance (Body Positivity) and medicalized thinness (Ozempic).*

## Project Overview
This project uses Python to quantify a major cultural shift in the fashion and wellness industries. By analyzing Google Search Trends data over a 6-year period, I tested the hypothesis that the rise of GLP-1 agonists (Ozempic) is statistically correlated with a shift in aesthetic preferences—specifically, the return of "thin-centric" fashion trends like Low Rise Jeans and the decline of inclusivity movements like Body Positivity.

## Key Insights & Analysis
The data reveals a stark "Cultural Crossing" event in late 2023:

1.  **The "Great Replacement" (r = -0.82):**
    There is a massive inverse correlation between **Body Positivity** (Red line) and **Ozempic** (Green line). As interest in medical weight loss surged, cultural interest in body acceptance plummeted to near-zero levels by 2025.

2.  **The Aesthetic Lag:**
    **Pilates Aesthetic** (Purple) and **Calorie Deficit** (Orange) track tightly with the rise of Ozempic. This suggests a return to "discipline-based" aesthetics.

3.  **The Denim Forecast:**
    While **Baggy Jeans** dominated the "Body Positivity" era (2020–2023), they have plateaued. Meanwhile, **Low Rise Jeans** (Yellow) are steadily climbing, mirroring the "thin" signals. Most notably, **Skinny Jeans** (Light Grey), which crashed during the pandemic, show early signs of a "micro-trend" recovery in late 2025.

## Technical Methodology
This was built using a custom Python script designed to handle unstable API endpoints and normalize disparate data sets.

* **Data Source:** Google Trends API (via `pytrends`).
* **Smoothing:** Applied a 12-week rolling average to eliminate weekly volatility and reveal macro-trends.
* **Normalization:** All datasets were scaled (0-100) to allow for relative comparison between high-volume terms (like "Jeans") and niche cultural terms (like "Pilates Aesthetic").
* **Statistical Validation:** Used `scipy.stats.pearsonr` to calculate correlation coefficients and p-values to distinguish between coincidence and correlation.

