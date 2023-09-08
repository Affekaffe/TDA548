import wordfreq, sys, urllib.request

def fileToLineList(link):
    #open the file and read the contents line by line
    file = open(link)
    data = file.read()
    lines = data.split("\n")
    file.close()
    return lines

def main():
    #the lab is talking about som stopwords that should not be included and they have those on index 1
    index = 1
    lines = []

    #if no arguments were specified just exit the function
    if(sys.argv.__len__() <= 1): return

    #if we have a wev link read it
    if(sys.argv[index].startswith("https://")or sys.argv[index].startswith("http://")):
        respons = urllib.request.urlopen(sys.argv[index])
        lines = respons.read().decode("utf8").splitlines()
        
    #if it's not from the web it's a local file
    else:
        lines = fileToLineList("lab1/" + sys.argv[index])
    words = wordfreq.tokenize(lines)
    print(words)

main()
#lines2 = fileToLineList("lab1/examples/article1.txt")
#words2 = wordfreq.tokenize(lines2)
#
#print(words2)
