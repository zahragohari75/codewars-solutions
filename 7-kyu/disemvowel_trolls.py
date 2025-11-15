# 7 kyu - Disemvowel Trolls
# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string_):
    vowels= 'aeoiuAEOIU'
    result = ''
    
    for char in string_:
        if char not in vowels :
            result += char
    return result
