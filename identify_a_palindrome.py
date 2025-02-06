import re


def find_a_palindrome(input: str = 'Race caR123'):

    new_text = ''
    for i in input:
        if re.findall(r'[A-Za-z]', i):
            new_text += i.lower()
        else:
            input.strip(i)
    return new_text == new_text[::-1]


find_a_palindrome()


def find_a_palindrome_second(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


find_a_palindrome_second('racecar')
