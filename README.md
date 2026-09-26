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

- **Text Similarity Detector.py** — Entry point; orchestrates the full comparison workflow
- **processing.py** — Document count validation, input collection, cleaning, and tokenization
- **bigram.py** — Generates consecutive word-pair (bigram) tuples
- **Jaccard_Similarity.py** — Jaccard similarity calculation (word-level and bigram-level)
- **Cosine_Similarity.py** — Cosine similarity calculation using word-frequency vectors
- **Interpret_Similarity.py** — Converts a numeric similarity score into a plain-language verdict
- **README.md** — Project documentation (this file)
- **statement.md** — Problem statement, scope, and target users


## Installation & Setup

1. Ensure Python 3 is installed on your system. You can check by opening a terminal and running: python --version
2. Clone this repository, or download it as a ZIP and extract it: git clone https://github.com/shreyansh_shukla_1717/text-similarity-detector.git
3. Open the project folder in VS Code (or any code editor of your choice).
4. No additional packages need to be installed — the project uses only Python's standard library.


## How to Run

1. Open a terminal in VS Code (Terminal → New Terminal), or navigate to the project folder in your system terminal.
2. Run the main script: python "Text Similarity Detector.py"
3. Follow the on-screen prompts:
   - Enter the number of documents you wish to compare.
   - Enter the text of each document, one at a time.
4. The program will display the most similar document pair, followed by a full comparison table for all document pairs.


## Testing Instructions

To verify the program works as expected, try the following test cases:

1. **Identical documents** — enter the same text twice; all three similarity scores should report 100%, and the top match should identify this pair.
2. **Completely unrelated documents** — enter two documents with no shared vocabulary; all scores should report 0%.
3. **Same words, different order** — enter two documents using identical vocabulary but in a different sequence (e.g., "not bad very good" vs. "very bad not good"); word-level Jaccard should remain high while Bigram Jaccard should drop significantly, demonstrating that phrase-order is being captured.
4. **Invalid input handling** — enter a non-numeric value (e.g., "five") when prompted for the number of documents, and confirm the program re-prompts rather than crashing. Similarly, try submitting an empty document to confirm it is rejected.
5. **Multiple documents (3 or more)** — confirm the program correctly generates and displays all unique pairwise comparisons without repeating a pair or comparing a document to itself.

## Author
SHREYANSH SHUKLA - 26BAI10862
