def tokenize(lines):
    words = []
    for line in lines:
        start = 0 #position in array
        end  = 0 #end
        while start < (len(line)):
            while start < (len(line)) and line[start].isspace():
                start = start + 1

            if start < len(line):

                end = start
                if line[start].isalpha():
                    while end<(len(line)) and line[end].isalpha():
                        end = end + 1

                elif line[start].isdigit() == True:
                    while end<(len(line)) and line[end].isdigit():
                        end = end + 1
  
                else:
                    while end<(len(line)) and not (line[end].isdigit() or line[end].isalpha() or line[end].isspace()):
                        end = end + 1

                words.append(line[start:end].lower())
                start = end - 1

            start = start + 1
    return words

def countWords(word_list, ignore_words):
    relevant_words = [w for w in word_list if w not in ignore_words]
    word_count = dict((word, 0) for word in set(relevant_words)) 
    for word in relevant_words:
        word_count[word] += 1
    print(word_count)
    return word_count 