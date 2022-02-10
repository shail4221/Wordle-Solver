import json
import operator
from queue import Empty
import re
from turtle import update

score_dict = {'E':26, 'S':25, 'A':24, 'O':23, 'R':22, 'I':21, 'L':20, 'T':19, 
                'N':18, 'U':17, 'D':16, 'M':15, 'Y':14, 'C':13, 'P':12, 'H':11,
                'G':10, 'B':9, 'K':8, 'F':7, 'W':6, 'V':5, 'Z':4, 'X':3,
                'J':2, 'Q':1}

yellow_score_dict = score_dict

iteration_wordlists = []

def score_words(wordlist, scores):
    scored_words = {}

    for word in wordlist:
        adjusted_word = ''.join(sorted(set(word), key=word.index))
        word_score = 0
        for letter in adjusted_word:
            word_score += scores[letter]
        scored_words[word] = word_score

    sorted_scored_words = dict(sorted(scored_words.items(), key=operator.itemgetter(1),reverse=True))
    return list(sorted_scored_words.keys())
    

with open('Resources/scored_wordlist.txt') as f:
    data = f.read()

unaltered_word_dictionary = json.loads(data)

#tell user what word to put down
#get yellow and green letters
#store eventual model with green letters
#remove words with yellow letters
#repeat

print("Please enter Wordle output as a combination of N,G, and Y. N is for a Grey letter, G is for a Green letter, and Y is for a Yellow letter")

unaltered_word_list = list(unaltered_word_dictionary.keys())
updated_word_list = list(unaltered_word_dictionary.keys())
iteration_wordlists.append(updated_word_list)

next_word = updated_word_list[0]

yellow_letters = []
grey_letters = []
green_letters = []
word_model = ['[A-Z]', '[A-Z]', '[A-Z]', '[A-Z]', '[A-Z]']

iteration = 0

while(next_word != "no next word"):
    iteration += 1



    if(iteration == 6):
        regex_expression = re.compile(''.join(word_model))
        print(regex_expression)
        new_list = [x for x in unaltered_word_list if regex_expression.match(x)]
        print(new_list)
        if(new_list is not Empty):
            #filter out all words with grey letters
            for letter in grey_letters:
                print("removing character " + letter)
                new_list = [x for x in new_list if letter not in x]
                print(new_list)
            if(new_list is not Empty):
                print("Final word: " + new_list[0])
            else:
                print("The program was not able to find a suitable word (sry)")
        else:
            print("The program was not able to find a suitable word (sry)")
        break

    print("Try " + next_word)

    reponse = str(input('What was the wordle output?')).upper()
    
    if(reponse == "exit pls"):
        break

    elif(len(reponse) != 5):
        print("Invalid response, exiting")
        break
    
    else:
        for i in range(0, 5):
            if(reponse[i] == 'N'):
                grey_letters.append(next_word[i])
                updated_word_list = [x for x in updated_word_list if next_word[i] not in x]
            elif(reponse[i] == 'Y'):
                yellow_letters.append(next_word[i])
                yellow_score_dict[next_word[i]] = 0
            elif(reponse[i] == 'G'):
                green_letters.append(next_word[i])
                word_model[i] = "[" + next_word[i] + "]"
                if('[A-Z]' not in word_model):
                    print("The wordle word for today is " + ''.join(word_model))
                    exit()
            else:
                print("Invalid response, exiting")
                break
            updated_word_list = score_words(updated_word_list, yellow_score_dict)
            print(updated_word_list)
            print(len(updated_word_list))
            iteration_wordlists.append(updated_word_list)
        print("one rotation complete, word model at the moment is " + ''.join(word_model))

        if(len(updated_word_list) == 0):
            next_word = "no next word"
            print("There are no more valid words")
        else:
            next_word = updated_word_list[0]