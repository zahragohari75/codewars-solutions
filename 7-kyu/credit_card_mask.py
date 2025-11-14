def maskify(cc):

    if len(cc) <= 4:
        return cc
    else:
        return "#" * (len(cc)-4) + cc[-4:]# 7 kyu - Credit Card Mask
# https://www.codewars.com/kata/...

