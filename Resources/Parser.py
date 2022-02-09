lines = []

with open("wordlist.txt", 'r') as f:
    lines = f.readlines()

letter_dict = {}

for sentence in lines:
    for letter in sentence:
        if(letter in letter_dict):
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 0

print(letter_dict)
