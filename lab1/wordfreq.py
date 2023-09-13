def tokenize(lines):
    words = []
    for line in lines: # loop over file
        start = 0 # start of each word
        end  = 0 # end of each word, to be determined by while loops below

        while start < (len(line)): 
            while start < (len(line)) and line[start].isspace(): # skip if space
                start = start + 1

            if start < len(line):

                # while loops increases end until word is complete
                
                end = start # set start of new word
                if line[start].isalpha(): # check if letters
                    while end<(len(line)) and line[end].isalpha():
                        end = end + 1

                elif line[start].isdigit(): # check if digits
                    while end<(len(line)) and line[end].isdigit():
                        end = end + 1
                
                # check if symbol, no while loop as symbols dont concatenate
                elif end<(len(line)) and not (line[end].isdigit() or line[end].isalpha() or line[end].isspace()):
                    end = end + 1

                words.append(line[start:end].lower()) # add word to list
                start = end - 1

            start = start + 1
    return words

def countWords(word_list, ignored_words):
    relevant_words = [w for w in word_list if w not in ignored_words] # new list without ignored_words
    word_count = dict((word, 0) for word in set(relevant_words)) # init dict
    
    for word in relevant_words: # increase count in dict for each occurence
        word_count[word] += 1
    return word_count 

def printTopMost(word_count, top_n):
    word_count_sorted = sorted(word_count.items(), key = lambda x: x[1], reverse = True) # obs: dict becomes list of tuples
    
    # loop over top n words, print word and count
    for word, count in word_count_sorted[:top_n]: 
        print(str(word).ljust(20) + str(count).rjust(5))