import wordfreq
#test = wordfreq.tokenize("abc, Abbbb det finns ett ord")
#print(test)
test = wordfreq.tokenize(input("Enter String: "))
print(test)
file = open("examples/article1.txt", encoding="utf-8")

#detta är ett test