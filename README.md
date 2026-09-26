# Text_Similarity_Detector
Text Similarity Detector is a Python console application that compares multiple text documents pairwise and quantifies their similarity using three distinct metrics: **Jaccard Similarity**, **Cosine Similarity**, and **Bigram Jaccard Similarity**. 
It is designed as a lightweight, transparent tool for academic use — helping students self-check assignment originality or enabling instructors to perform a quick first-pass similarity screen across multiple submissions.
The project is built entirely in core Python, without relying on external NLP libraries, so every similarity calculation is implemented from first principles using native data structures (lists, sets, dictionaries, tuples).

## Features

- **Multi-document comparison** — accepts any number of documents and compares every unique pair automatically.
- **Three similarity metrics per pair:**
  - *Jaccard Similarity* — measures word-set overlap between two documents.
  - *Cosine Similarity* — measures similarity based on word-frequency vectors, accounting for repetition and emphasis.
  - *Bigram Jaccard Similarity* — measures overlap of consecutive word-pairs, capturing phrase order and structure that word-level metrics miss.
- **Top-match identification** — automatically identifies and reports the most similar document pair, ranked by Cosine similarity, with a plain-language interpretation of the score.
- **Tabular results summary** — displays all pairwise comparison results in a clean, aligned table.
- **Input validation** — rejects and re-prompts for empty documents and non-numeric document counts, preventing crashes on invalid input.

