# The Cost of Living Crisis: A Data-Driven Analysis
# ECON 5200 — Assignment 1 | Student Price Index (SPI)

## Overview
Official CPI is designed to reflect the spending patterns of the average U.S. consumer. However, students face a very different cost structure—dominated by tuition and rent. This project builds a student-focused inflation measure and compares it to the national CPI to test whether “average inflation” hides real pressure on students.

## The Problem
The national CPI is a weighted index representing a broad population. For students, tuition and housing take up a disproportionately large share of spending, meaning the official CPI may understate real student inflation.

This project asks: Does the official CPI reflect the lived inflation experience of students in Boston?

## Methodology
1. **Student basket benchmark:** Constructed a simplified student consumption basket (tuition, rent, food, Spotify) and tracked inflation from 2016 to 2024.  
2. **Official data pipeline:** Pulled CPI time series from the FRED API (`fredapi`) using student-relevant category proxies (tuition, rent, streaming, food away from home).  
3. **Normalization (Re-indexing):** Since CPI sub-series use different base years, all series were normalized to a common baseline (**Jan 2016 = 100**) using:  
   `Value_Index = (Value_Current / Value_at_Start_Date) * 100`  
4. **Student SPI construction (Laspeyres weighting):** Built a weighted student inflation index (**Student SPI**) using student-relevant weights (tuition/rent dominate).  
5. **Reality check (Boston vs USA vs Student):** Extended analysis by pulling the Boston-Cambridge-Newton CPI series and plotting three normalized indices on one chart.

## Visual Results

### 1) Normalized CPI Components (2016=100)
Tracks sector-specific inflation trends relevant to students (tuition, rent, streaming, food away from home) compared to the official CPI benchmark.

### 2) Student SPI vs Official CPI (“Inflation Gap”)
A weighted Student SPI was compared against the official CPI, and the gap between them was shaded using `plt.fill_between` to highlight divergence over time.

### 3) The Scale Fallacy (“Bad Chart”)
A raw chart without normalization (tuition vs streaming) illustrates why comparing series with different base years is misleading—tuition appears “huge” simply due to scale differences.

### 4) Boston vs USA vs You
Boston CPI was fetched from FRED, re-indexed to 2016=100, and compared with national CPI and the Student SPI to evaluate whether local inflation differs from national averages.

## Key Findings

- Students experience inflation differently because tuition and housing dominate budgets.
- Once CPI series are properly normalized, rent and food trends rise more sharply, changing the story compared to the national CPI.
- The Student SPI diverges from official CPI, revealing that average CPI may understate student cost pressure.
- The Boston CPI comparison shows how regional inflation can further amplify the gap between national indicators and lived experiences.

My analysis reveals a meaningful divergence between student-facing inflation and the official CPI benchmark, suggesting national averages can hide local and demographic-specific inflation burdens.

## Tools & Libraries

- Python (`pandas`, `numpy`, `matplotlib`)
- FRED API via `fredapi`
- Index normalization + weighted index construction (Laspeyres-style approach)

## Files

- `Assignment_1.ipynb` — full code and charts  
- `README.md` — project narrative for portfolio presentation
