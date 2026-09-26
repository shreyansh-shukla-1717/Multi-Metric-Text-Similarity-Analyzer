# Problem Statement

The manual verification of textual overlap across multiple submissions is a time-consuming, subjective, and error-prone process, particularly as the number and length of documents under review increases. In academic settings, both students and instructors frequently lack access to convenient, transparent tools for assessing how closely a piece of written work resembles other submissions — whether to verify originality prior to submission, or to conduct a preliminary screen for potential overlap across a batch of assignments. Existing commercial plagiarism-detection solutions are often opaque in their methodology, dependent on proprietary databases, and inaccessible for lightweight, individual, or classroom-level use.

This project addresses this gap by presenting the design and implementation of a **Text Similarity Detector**, developed entirely in core Python, that performs pairwise comparison across multiple text documents and quantifies their similarity through three complementary, mathematically distinct metrics: **word-level Jaccard Similarity**, **Cosine Similarity**, and **Bigram Jaccard Similarity**. Each metric captures a different dimension of textual resemblance — vocabulary overlap, proportional word emphasis, and preservation of word order and phrasing, respectively — allowing the system to distinguish between documents that merely share a topic and documents that exhibit genuine textual borrowing. The system is implemented without reliance on external natural language processing libraries, ensuring that every similarity computation is transparent, derived from first principles, and fully explainable at the level of its underlying logic.

# Scope of the Project

The scope of this project is deliberately limited to a **console-based application** that accepts plain text input provided directly by the user during runtime. The system does not interface with external databases, persistent file storage, cloud services, or third-party plagiarism-detection repositories; all processing occurs locally, in-memory, for the duration of a single program execution.

The system supports comparison of an arbitrary number of documents, computing similarity across every unique pairwise combination without redundant or self-comparisons. Input validation is incorporated to handle common user errors, including empty submissions and non-numeric entry of the document count.

Certain advanced natural language processing techniques have been deliberately excluded from the current implementation, in keeping with the project's academic scope and its foundation in core programming constructs rather than specialized libraries. These excluded techniques include:
- **TF-IDF (Term Frequency–Inverse Document Frequency) weighting**, which would require a broader corpus of reference documents to compute meaningful term-rarity statistics.
- **Stop-word filtering**, which would refine similarity scores by excluding high-frequency grammatical words.
- **Edit-distance (Levenshtein) computation**, which would enable detection of near-identical words affected by typographical variation.


These are identified as prospective future enhancements rather than current limitations of oversight, reflecting a deliberate decision to prioritize a transparent, defensible implementation within the bounds of the current curriculum.

# Target Users

- **Students**, who require a preliminary, self-directed means of assessing the originality of their own written work — such as assignments, reports, or essays — prior to formal submission, without needing access to institutional or commercial plagiarism-detection software.
- **Instructors and Faculty Members**, who require a lightweight, transparent, first-pass mechanism for screening similarity across a limited set of student submissions, particularly in contexts where formal institutional plagiarism-detection infrastructure may be unavailable, inaccessible, or unnecessary for the scale of the task at hand.
