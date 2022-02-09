import json

score_dict = {'E':26, 'S':25, 'A':24, 'O':23, 'R':22, 'I':21, 'L':20, 'T':19, 
                'N':18, 'U':17, 'D':16, 'M':15, 'Y':14, 'C':13, 'P':12, 'H':11,
                'G':10, 'B':9, 'K':8, 'F':7, 'W':6, 'V':5, 'Z':4, 'X':3,
                'J':2, 'Q':1}



with open('Resources/scored_wordlist.txt') as f:
    data = f.read()

unaltered_word_dictionary = json.loads(data)

#tell user what word to put down
#get yellow and green letters
#store eventual model with green letters
#remove words with yellow letters
#repeat

print("Please enter Wordle output as a combination of N,G, and Y. N is for a Grey letter, G is for a Green letter, and Y is for a Yellow letter")

updated_word_list = list(unaltered_word_dictionary.keys())

next_word = updated_word_list[0]

yellow_letters = []
grey_letters = []
green_letters = []
word_model = ['?', '?', '?', '?', '?']

while(next_word != "no next word"):
    print("Try " + next_word)

    reponse = str(input('What was the wordle output?'))
    

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
                print(updated_word_list)
                print(len(updated_word_list))
            elif(reponse[i] == 'Y'):
                yellow_letters.append(next_word[i])
            elif(reponse[i] == 'G'):
                green_letters.append(next_word[i])
                word_model[i] = next_word[i]
                if('?' not in word_model):
                    print("The wordle word for today is " + ''.join(word_model))
                    break
            else:
                print("Invalid response, exiting")
                break
        print("one rotation complete, word model at the moment is " + ''.join(word_model))
        if(len(updated_word_list) == 0):
            next_word = "no next word"
            print("There are no more valid words")
        else:
            next_word = updated_word_list[0]