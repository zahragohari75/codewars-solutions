# 8 kyu - Filter out the geese
# https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):

    return [b for b in birds if b not in geese]
