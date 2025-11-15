# 7 kyu - Vowel Count
# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    
    vowels = "aeiou"
    count = 0
    
    for char in sentence:
        if char in vowels:
            count += 1
    
    return count
