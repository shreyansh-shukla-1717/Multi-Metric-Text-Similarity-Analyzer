def process():
    num_input = input("\nEnter the number of documents to be evaluated: ")
    while not num_input.isdigit():
        print("Please enter a valid whole number.")
        num_input = input("\nEnter the number of documents to be evaluated: ")
    num = int(num_input)
    document = []
    for i in range(num):
        text = input("\nEnter the texts for similarity comparison: ")
        while not text.strip():
            print("The input cannot be empty. Please enter a valid text.")
            text = input("\nEnter the texts for similarity comparison: ")
        punctuation = ".,!?;:\"'()[]{}"
        for char in punctuation:
            text = text.replace(char, "")
        raw_text = text.lower().split()
        document.append(raw_text)
    return document