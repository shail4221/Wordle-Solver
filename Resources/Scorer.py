import operator
import json

words = []

with open('wordlist.txt','r+') as f:
    for line in f:
        words.append(line.split())

score_dict = {'E':26, 'S':25, 'A':24, 'O':23, 'R':22, 'I':21, 'L':20, 'T':19, 
                'N':18, 'U':17, 'D':16, 'M':15, 'Y':14, 'C':13, 'P':12, 'H':11,
                'G':10, 'B':9, 'K':8, 'F':7, 'W':6, 'V':5, 'Z':4, 'X':3,
                'J':2, 'Q':1}

scored_words = {}


for word in (words[0]):
    adjusted_word = ''.join(sorted(set(word), key=word.index))
    word_score = 0
    for letter in adjusted_word:
        word_score += score_dict[letter]
    scored_words[word] = word_score

sorted_scored_words = dict(sorted(scored_words.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_scored_words)

with open('scored_wordlist.txt', 'w') as convert_file:
     convert_file.write(json.dumps(sorted_scored_words))