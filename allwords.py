# manually generate every word of a certain length, and output to .txt file

# options for initial syllable: onset, nothing
# options for vowel: [vowels]
# options for "bridge": next onset, coda+onset, geminate, cluster, END, coda+END

onset = ["P", "B", "M", "T", "D", "N", "KY", "GY", "NY", "K", "G", "Q", "F", "V", "S", "Z",
        "SH", "ZH", "H", "HW", "W", "Y", "L", "LY", "R", "RR",
        "PF", "BV", "C", "J", "CY", "JY", "CH", "JH"]
vowel = ["a", "i", "e", "ea", "u", "o", "oa"]
coda = ["p", "b", "t", "d", "ky", "gy", "k", "g", "q", "m", "n", "ny",
        "l", "ly", "r", "rr", "ng", "kh", "gh", "qh"]
geminate = ["PP", "BB", "MM", "TT", "DD", "NN", "KKY", "GGY", "NNY", "KK", "GG", "QQ", "FF", "VV", "SS", "ZZ",
            "SSH", "ZZH", "WW", "YY", "LL", "LLY", "RR"]
cluster1 = ["P", "B", "M", "T", "D", "N", "KY", "GY", "NY", "K", "G", "Q", "F", "V", "S", "Z", "SH", "ZH"]
cluster2 = ["W", "L", "LY", "R", "RR"]
extra = ["ST", "SK", "SHT", "SHK", "ZD", "ZG", "ZHD", "ZHG"]  # for any atypical combinations
disallowed = {"NR", "NRR", "SRR", "ZRR", "SHRR", "ZHRR"}

cluster = []
for c in cluster1:
    for d in cluster2:
        cluster.append(c + d)

cluster += extra
cluster = [el for el in cluster if el not in disallowed]