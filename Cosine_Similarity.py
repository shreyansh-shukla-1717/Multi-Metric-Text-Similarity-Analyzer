def Cosine_Similarity(text1, text2):
    frequency1 = {}
    for word in text1:
        if word in frequency1:
             frequency1[word] += 1
        else:
            frequency1[word] = 1
    frequency2 = {}
    for word in text2:
        if word in frequency2:
            frequency2[word] += 1
        else:
            frequency2[word] = 1
    dot = 0
    for word in frequency1:
        if word in frequency2:
            dot += (frequency1[word] * frequency2[word])
    count = 0
    for word in frequency1:
        count = count + (frequency1[word] ** 2)
    count2 =0
    for word in frequency2:
        count2 = count2 + (frequency2[word] ** 2)
    count**=0.5
    count2**=0.5
    if count * count2 == 0:
        return 0.0
    cosine=round(dot/(count*count2), 3)
    return cosine