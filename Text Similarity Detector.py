# Text Similarity Detector
import Jaccard_Similarity as js
import Cosine_Similarity as cs
import Interpret_Similarity as ins
import bigram as bigram
import processing as proc

best_score = -1
best_pair = None
results = []
document = proc.process()

# Compare each document with every other document
for i in range(len(document)):
    for j in range(i + 1, len(document)):
        text1 = document[i]
        text2 = document[j]
        similarity_score = js.Jaccard_Similarity(text1, text2)
        cosine = cs.Cosine_Similarity(text1, text2)
        bigramA = bigram.bigram(text1)
        bigramB = bigram.bigram(text2)
        jaccard_bigram_similarity = js.Jaccard_Similarity(bigramA, bigramB)

        results.append((i+1, j+1, similarity_score, cosine, jaccard_bigram_similarity))

        if cosine > best_score:
            best_score = cosine
            best_pair = (i+1, j+1)

print("\nTOP MATCH (ranked by Cosine Similarity)")
if best_pair:
    print(f"Most similar pair: Document {best_pair[0]} & Document {best_pair[1]}")
    print(f"Cosine Similarity: {best_score*100:.2f}%")
    ins.Interpret_Similarity(best_score, "Cosine")
else:
    print("No pairs to compare.")

# FULL COMPARISON TABLE
print("\nFULL COMPARISON TABLE")
print(f"{'Pair':<20}{'Jaccard %':>12}{'Cosine %':>12}{'Bigram %':>12}")
print("-" * 56)
for doc_i, doc_j, jac, cos, big in results:
    pair_label = f"Doc {doc_i} vs Doc {doc_j}"
    print(f"{pair_label:<20}{jac*100:>11.2f}%{cos*100:>11.2f}%{big*100:>11.2f}%")