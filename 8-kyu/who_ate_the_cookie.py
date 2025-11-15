# 8 kyu - Who ate the cookie?
# https://www.codewars.com/kata/55a996e0e8520afab9000055

def cookie(x):
    if isinstance(x, str):
        return "Who ate the last cookie? It was Zach!"
    elif isinstance(x, (float, int)) and not isinstance(x, bool):
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"
