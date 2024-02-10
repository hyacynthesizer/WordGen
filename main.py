import random


# OBJECTIVE: use weighted random selections to generate arbitrary words according to a set syllable structure


class CVC:
    def __init__(self):
        self.next = None
        self.next_weights = None
        self.chars = None
        self.chweights_list = None  # store the list of lists of character weights
        self.chweights_dict = dict(zip([""],[[1]]))  # dictionary of each char and array of weights by syllable number
        # standard length is up to 10 syllables


    def makedict(self):  # initialize the weights dictionary at the end of the subclass init
        self.chweights_dict = dict(zip(self.chars,self.chweights_list))
        # pass


    # can pass in previous character to check validity, and the syllable count

    def select_next(self, syll=0):
        return random.choices(self.next, weights=self.next_weights, k=1)

    def select_char(self, syll=0):
        w = []
        for c in self.chars:
            res = self.chweights_dict.get(c)
            if syll >= len(res): syll = -1
            w.append(res[syll])
        return random.choices(self.chars, weights=w, k=1)
        # return random.choices(self.chars, weights=self.char_weights, k=1)


class Init(CVC):
    def __init__(self):
        super().__init__()
        self.next = ["Vowel", "Onset", "Cluster", "Affricate"]
        self.next_weights = [1.2, 1.7, 1, 1]
        
        self.chars = [""]
        self.chweights_list = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        super().makedict()
        

class Vowel(CVC):
    def __init__(self):
        super().__init__()
        self.next = ["Coda", "Onset", "Affricate", "Geminate", "Cluster", "End"]
        self.next_weights = [1.6, 2, 1.3, 1, 0.8, 2.5]
        
        self.chars = ["a", "i", "e", "ea", "u", "o", "oa"]
        self.chweights_list = [
            [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
            [1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2],
            [1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2],
            [1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]
        super().makedict()


class Onset(CVC):
    def __init__(self):
        super().__init__()
        self.next = ["Vowel"]
        self.next_weights = [1]
        
        self.chars = ["P", "B", "M", "T", "D", "N", "KY", "GY", "NY", "K", "G", "Q", "F", "V", "S", "Z",
                      "SH", "ZH", "H", "HW", "W", "Y", "L", "LY", "R", "RR"]
        self.chweights_list = [
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]
        super().makedict()


class Affricate(CVC):
    def __init__(self):
        super().__init__()
        self.next = ["Vowel"]
        self.next_weights = [1]
        
        self.chars = ["PF", "BV", "C", "J", "CY", "JY", "CH", "JH"]
        self.chweights_list = [
            [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
            [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
            [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]]
        super().makedict()


class Coda(CVC):
    def __init__(self):
        super().__init__()
        self.next = ["Onset", "Affricate", "End"]
        self.next_weights = [2, 1.2, 2.5]
        
        self.chars = ["p", "b", "t", "d", "ky", "gy", "k", "g", "q", "m", "n", "ny", "l", "ly", "r", "rr"]
        self.chweights_list = [
            [0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
            [0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
            [0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
            [0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
            [0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
            [0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
            [0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]]
        # the way the syllable count increases, it's impossible for a coda to ever be in the "zero"th syllable
        super().makedict()


class Cluster(CVC):
    def __init__(self):
        super().__init__()
        self.next = ["Vowel"]
        self.next_weights = [1]
        
        self.chars = ["P", "B", "M", "T", "D", "N", "KY", "GY", "NY", "K", "G", "Q", "F", "V", "S", "Z", "SH", "ZH"]
        self.char_weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.second = ["W", "L", "LY", "R", "RR"]
        self.second_weights = [1, 1, 1, 1, 1]
        self.adjust_weights = None
        # super().makedict()

    def select_char(self, syll=0):  # might be harder to do positional weights for this in a way that makes sense...
        self.adjust_weights = self.second_weights  # clone of base second weights for validity
        part1 = random.choices(self.chars, weights=self.char_weights, k=1)
        if part1[0] == "N":
            self.adjust_weights = [1, 1, 1, 0, 0]
        elif part1[0] == "S" or part1[0] == "Z" or part1[0] == "SH" or part1[0] == "ZH":
            self.adjust_weights = [1, 1, 1, 1, 0]
        part2 = random.choices(self.second, weights=self.adjust_weights, k=1)

        return part1 + part2  # need to check for invalid options?


class Geminate(CVC):
    def __init__(self):
        super().__init__()
        self.next = ["Vowel"]
        self.next_weights = [1]
        
        self.chars = ["PP", "BB", "MM", "TT", "DD", "NN", "KKY", "GGY", "NNY", "KK", "GG", "QQ", "FF", "VV", "SS", "ZZ",
                      "SSH", "ZZH", "WW", "YY", "LL", "LLY", "RR"]
        self.chweights_list = [
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]
        super().makedict()


def add_to_list(target, part):
    match part:
        case "Vowel":
            target.append(Vowel())
        case "Onset":
            target.append(Onset())
        case "Affricate":
            target.append(Affricate())
        case "Geminate":
            target.append(Geminate())
        case "Cluster":
            target.append(Cluster())
        case "Coda":
            target.append(Coda())
        case "End":
            pass
    return part != "End"


parts = [Init()]
chars = [""]
# for whatever reason, random.choices returns a single-item list
next_part = parts[-1].select_next()[0]  
syllables = 0


while add_to_list(parts, next_part):
    s = syllables
    if next_part == "Vowel":
        s += 1
    chars.extend(parts[-1].select_char(syll=syllables))
    next_part = parts[-1].select_next()[0]  # because it returns as a 1d list for whatever reason
    syllables = s  # allows vowels to still be in the "zero"th syllable, but will then force the first coda to never be 0th

print(chars)
word = "".join(chars)
print(word)
