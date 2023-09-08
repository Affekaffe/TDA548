import wordfreq

def fileToLineList(link):
    #open the file and read the contents line by line
    file = open(link)
    lines = file.readlines()
    file.close()
    return lines

lines2 = fileToLineList("lab1/examples/article1.txt")
words2 = wordfreq.tokenize(lines2)

print(words2)