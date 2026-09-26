def Interpret_Similarity(score, metric_name):
    if score == 0.000:
        print("\n",metric_name, "similarity: The compared paragraphs are not similar.")
    elif score == 1.000:
        print("\n",metric_name, "similarity: The two texts are identical.")
    elif score >= 0.750:
        print("\n",metric_name, "similarity: The compared paragraphs are highly similar.")
    elif score >= 0.500:
        print("\n",metric_name, "similarity: The compared paragraphs are moderately similar.")
    elif score >= 0.250:
        print("\n",metric_name, "similarity: The compared paragraphs are slightly similar.")
    else:
        print("\n",metric_name, "similarity: The compared paragraphs are almost not similar.")