# FedSpeak 2.0 — NLP Pipeline for Central Bank Communications

## Objective

Diagnosed, corrected, and extended a broken NLP pipeline for analyzing FOMC meeting minutes, comparing traditional TF-IDF features against sentence-transformer embeddings for predicting Federal Reserve policy decisions.

## Methodology

- Identified three planted errors in an NLP pipeline: naive whitespace tokenizer, wrong sentiment dictionary (Harvard GI instead of Loughran-McDonald), and poorly configured TF-IDF parameters
- Fixed preprocessing with `nltk.word_tokenize()` and regex cleaning to properly handle punctuation and contractions
- Replaced the general-purpose Harvard GI dictionary with the Loughran-McDonald financial sentiment dictionary, reducing false positive rate from 51% to 0%
- Corrected TF-IDF vectorizer with `min_df=5`, `max_df=0.85`, and bigram support to filter noise and capture meaningful phrases like "interest rate" and "target range"
- Encoded 240 FOMC documents using `all-MiniLM-L6-v2` sentence-transformer into 384-dimensional dense embeddings
- Clustered documents using K-Means (K=3) on both TF-IDF (after SVD reduction to 50 dims) and embeddings, compared using silhouette scores
- Evaluated predictive power with logistic regression and TimeSeriesSplit (5-fold) cross-validation on a binary tightening/easing target

## Key Findings

- Embeddings produced slightly better clusters (silhouette: 0.197 vs 0.167 for TF-IDF)
- TF-IDF outperformed embeddings in predicting Fed tightening periods (AUC: 0.81 ± 0.24 vs 0.72 ± 0.21), likely because specific policy keywords and bigrams are more directly predictive than general semantic representations
- Built a reusable `fomc_sentiment.py` module with `preprocess_fomc()`, `compute_lm_sentiment()`, and `build_tfidf_matrix()`

## Tools

Python, NLTK, scikit-learn, sentence-transformers, Hugging Face Datasets
