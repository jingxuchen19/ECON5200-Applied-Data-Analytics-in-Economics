# Unsupervised Learning — Clustering & Dimensionality Reduction

## Objective
Diagnose, fix, and extend a K-Means clustering pipeline to classify world economies and customer segments using standardized features, PCA, and UMAP.

## Methodology
- Identified and corrected 4 errors in a broken K-Means pipeline: missing standardization, wrong parameter name (`k` vs `n_clusters`), PCA applied before scaling, and missing `random_state`
- Built a corrected pipeline: StandardScaler → K-Means (K=4) → PCA visualization
- Applied K-Means to synthetic customer segmentation data (2,000 customers, 6 behavioral features)
- Compared PCA vs UMAP for 2D projection of cluster structure
- Compared K-Means with Agglomerative (Ward linkage) hierarchical clustering
- Built a reusable `clustering_utils.py` module with `run_kmeans_pipeline()`, `evaluate_k_range()`, and `plot_pca_clusters()`

## Key Findings
- Without standardization, K-Means clusters almost entirely on GDP per capita — the other 9 features contribute almost nothing to distance calculations
- PCA on raw data: PC1 explains 90%+ variance (just a proxy for GDP). After standardization, PC1 drops to ~63%, meaning multiple features now contribute
- Silhouette score for K=4 on WDI data: 0.2590, indicating reasonable but overlapping clusters typical of real-world country data
- UMAP provides much tighter visual separation than PCA for customer segments, preserving local neighborhood structure that PCA's linear projection misses
- K-Means and Agglomerative clustering largely agree on assignments, with both methods producing similar silhouette scores

## Tools
Python, scikit-learn, UMAP, matplotlib, pandas
