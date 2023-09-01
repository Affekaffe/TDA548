
def tokenize(text):
    word_count = dict()
    words = text.split()
    unique_words = set(words)
    for w in unique_words:
        if word_count[w].isalpha():
            
        word_count[w] = words.count(w)
    return(word_count)

#print(tokenize(input('yo enter epic string: ')))

