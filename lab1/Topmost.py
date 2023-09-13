import wordfreq, sys, urllib.request

def fileToLineList(link):
    #open the file and read the contents line by line
    file = open(link, encoding="utf-8")
    data = file.read()
    lines = data.split("\n")
    file.close()
    return lines

def main():

    # if too few arguments were specified just exit the function
    if(sys.argv.__len__() <= 1): 
        return

    ignored_words_id = 1
    path_id = 2
    top_n_id = 3

    # get ignored words from 1st argument
    ignored_words = file_to_line_list("lab1/" + sys.argv[ignored_words_id])

    # get text from 2nd argument
    # if we have a web link read it
    if(sys.argv[path_id].startswith("https://") or sys.argv[path_id].startswith("http://")):
        response = urllib.request.urlopen(sys.argv[path_id])
        lines = response.read().decode("utf8").splitlines()
    else: # if it's not from the web it's a local file
        lines = file_to_line_list("lab1/" + sys.argv[path_id]) 
    
    # get number of words from 3rd argument
    top_n = int(sys.argv[top_n_id])

    # tokenize, countWords and printTopMost  
    words = wordfreq.tokenize(lines)
    word_count = wordfreq.countWords(words, ignored_words)
    wordfreq.printTopMost(word_count, top_n)
main()

# call from the terminal:
# py lab1/Topmost.py <ignored words> <url or path to file> <nr of words to print>