import re
import secrets

def dice_ware(number_of_words, source_file):
    
    with open(source_file,'r') as wordList:
        words = re.findall(r"(\d{5})\t(\w+|.+)", wordList.read())
    [print(f'{word[1]}', end = ' ') for word in [secrets.choice(words) for _ in range(number_of_words)]]

dice_ware(10,'diceware.wordlist.txt')
