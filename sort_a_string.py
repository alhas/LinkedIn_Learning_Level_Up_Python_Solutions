

def sort_a_string(input: str = 'alhas bahtiyar ali'):

    result = ' '.join(sorted(input.split(), key=str.casefold))
    print(result)

sort_a_string()
