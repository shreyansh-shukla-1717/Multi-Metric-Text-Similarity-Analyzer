def bigram(text):
    bi = []
    for i in range(len(text)-1):
        bi.append(text[i] + " " + text[i+1])
    return bi