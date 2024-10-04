import time
# manually generate every word of a certain length, and output to .txt file

# options for initial syllable: onset, nothing
# options for vowel: [vowels]
# options for "bridge": next onset, coda+onset, geminate, cluster, END, coda+END

# need to be able to specify to the console the syllable count of the words to generate

# implement rules for adding hyphens?

onset = ["P", "B", "M", "T", "D", "N", "Ǩ", "Ǧ", "Ň", "K", "G", "Q", "F", "V", "S", "Z",
        "Š", "Ž", "H", "Ŵ", "W", "Y", "L", "Ľ", "R", "Ř",
        "Ṕ", "B́", "C", "J", "Č", "J̌", "Ć", "J́"]
vowel = ["a", "i", "e", "ê", "u", "o", "ô"]
coda = ["p", "b", "t", "d", "ǩ", "ǧ", "k", "g", "q", "m", "n", "ň",
        "l", "ľ", "r", "ř", "n̂", "ḱ", "ǵ", "q́"]
geminate = ["PP", "BB", "MM", "TT", "DD", "NN", "ǨǨ", "ǦǦ", "ŇŇ", "KK", "GG", "QQ", "FF", "VV", "SS", "ZZ",
            "ŠŠ", "ŽŽ", "WW", "YY", "LL", "ĽĽ", "ŘŘ", "ṔṔ", "B́B́", "CC", "JJ", "ČČ", "J̌J̌", "ĆĆ", "J́J́"]
cluster1 = ["P", "B", "M", "T", "D", "N", "Ǩ", "Ǧ", "Ň", "K", "G", "Q", "F", "V", "S", "Z", "Š", "Ž"]
cluster2 = ["W", "L", "Ľ", "R", "Ř"]
extra = ["ST", "SK", "ŠT", "ŠK", "ZD", "ZG", "ŽD", "ŽG"]  # for any atypical combinations
disallowed = {"NR", "NŘ", "ŇR", "ŇŘ", "SŘ", "ZŘ", "ŠŘ", "ŽŘ"}

cluster = []
for c in cluster1:
    for d in cluster2:
        cluster.append(c + d)

cluster += extra
cluster = [el for el in cluster if el not in disallowed]
# print(cluster)


sylcount = abs(int(input("How many syllables should the words have? ")))
if sylcount == 0: sylcount = 1

def addvowel(w, n, f):
    for c in vowel:
        wnew = w + c
        num = n + 1
        addbridge(wnew, num, f)

def addbridge(w, n, f):
    if n == sylcount:
        for c in [""] + coda:
            word = w + c
            finished(word, f)
    else:
        for o in ["no", "co","g","cl"]:
            match o:
                case "no":
                    # no coda, next onset
                    for c in onset:
                        word = w + c
                        addvowel(word, n, f)
                case "co":
                    for c in coda:
                        for d in onset:
                            word = w + c + d
                            addvowel(word, n, f)
                case "g":
                    for c in geminate:
                        word = w + c
                        addvowel(word, n, f)
                case "cl":
                    for c in cluster:
                        word = w + c
                        addvowel(word, n, f)
                case _:
                    print("Something has gone wrong here.")
                    pass


def finished(word, f):
    # print(word, file=f)
    print(word)
    time.sleep(0.2)
    

filename = "dict-" + str(sylcount) + ".txt"
with open(filename, "w", encoding="utf-8") as f:
    
    # looping here

    for c in [""] + onset:
        word = "" + c
        addvowel(word, 0, f)