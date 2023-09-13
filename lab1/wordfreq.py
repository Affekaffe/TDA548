def tokenize(lines):
    words = []
    for line in lines:
        start = 0 
        end  = 0 
        while start < (len(line)):
            while start < (len(line)) and line[start].isspace():
                start = start + 1

            if start < len(line):

                end = start
                if line[start].isalpha():
                    while end<(len(line)) and line[end].isalpha():
                        end = end + 1

                elif line[start].isdigit():
                    while end<(len(line)) and line[end].isdigit():
                        end = end + 1
  
                elif end<(len(line)) and not (line[end].isdigit() or line[end].isalpha() or line[end].isspace()):
                    end = end + 1

                words.append(line[start:end].lower())
                start = end - 1

            start = start + 1
    return words

def countWords(word_list, ignored_words):
    relevant_words = [w for w in word_list if w not in ignored_words]
    word_count = dict((word, 0) for word in set(relevant_words)) 
    for word in relevant_words:
        word_count[word] += 1
    return word_count 

def printTopMost(word_count, top_n):
    word_count_sorted = sorted(word_count.items(), key = lambda x: x[1], reverse = True) # obs: dict becomes list of tuples
    
    # loop over top n words, print word and count
    for word, count in word_count_sorted[:top_n]: 
        print(str(word).ljust(20) + str(count).rjust(5))