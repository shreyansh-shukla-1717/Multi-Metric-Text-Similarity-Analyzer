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

## Technologies / Tools Used

- **Python 3** (no external libraries or packages required)
- **VS Code** — used as the development environment
- Core Python constructs used: lists, sets, dictionaries, tuples, functions, loops, conditional statements, string manipulation

## Project Structure

```
text-similarity-detector/
├── main.py                    # Entry point — orchestrates the full comparison workflow
├── processing.py              # Document count validation, input collection, cleaning, tokenization
├── bigram.py                  # Generates consecutive word-pair (bigram) tuples
├── Jaccard_Similarity.py      # Jaccard similarity calculation (word-level and bigram-level)
├── Cosine_Similarity.py       # Cosine similarity calculation using word-frequency vectors
├── Interpret_Similarity.py    # Converts a numeric similarity score into a plain-language verdict
├── README.md
└── statement.md
```

## Installation & Setup

1. Ensure Python 3 is installed on your system. You can check by opening a terminal and running: python --version
2. Clone this repository, or download it as a ZIP and extract it: git clone https://github.com/<your-username>/text-similarity-detector.git
3. Open the project folder in VS Code (or any code editor of your choice).
4. No additional packages need to be installed — the project uses only Python's standard library.
