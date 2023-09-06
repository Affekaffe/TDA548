def tokenize(lines):
    words = []
    for line in lines:
        start = 0 #position in array
        end  = 0
        while start < (len(line)):
            while start < (len(line)) and line[start].isspace() == True:
                start = start + 1


            if start < (len(line)) and line[start].isalpha() == True:
                end = start
                while end<(len(line)) and line[end].isalpha() == True:
                    end = end + 1
                words.append(line[start:end].lower())
                start = end - 1


            elif start < (len(line)) and line[start].isdigit() == True:
                end = start
                while end<(len(line)) and line[end].isdigit() == True:
                    end = end + 1
                words.append((line[start:end].lower()))
                start = end - 1

                
            else:
                end = start
                while end<(len(line)):
                    end = end + 1
                words.append(line[start:end].lower())
                start = end - 1
            start = start+1
    return words
