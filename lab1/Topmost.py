import wordfreq
#test = wordfreq.tokenize("abc, Abbb det finns ett ord")
#print(test)
test = wordfreq.tokenize(input("Enter String: "))
print(test)
file = open("examples/article1.txt", encoding="utf-8")
