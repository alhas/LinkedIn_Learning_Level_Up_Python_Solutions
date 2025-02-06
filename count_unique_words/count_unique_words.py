from collections import Counter
import re


def count_words(text):

    with open(text, 'r') as file:
        content = re.findall(r"[0-9a-zA-Z-']+", file.read().casefold())
  
    print(f'Total Words: {len(content)}\nTop 20 Words')
    for key, value in list(sorted(Counter(content).items(), key=lambda item: item[1], reverse=True))[:20]:
        print(f"{key.upper()}\t{value}")

count_words('pg100.txt')
