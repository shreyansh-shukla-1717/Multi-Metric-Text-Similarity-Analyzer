def Jaccard_Similarity(text1, text2):
    h = text1
    h1 = text2
    h = set(h)
    h1 = set(h1)
    intersection = h.intersection(h1)
    union=h.union(h1)
    if not union:
        return 0.0
    similarity_score=round(len(intersection)/len(union), 3)
    return similarity_score