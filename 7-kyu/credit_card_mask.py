# 7 kyu - Credit Card Mask
# https://www.codewars.com/kata/5412509bd436bd3392000d90

def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        return "#" * (len(cc) - 4) + cc[-4:]

# --- تست ---
if name == "__main__":
    # کپی شده از Codewars
    print(maskify("4556364607935616"))  # "############5616"
    print(maskify("1"))                  # "1"
    print(maskify("11111"))              # "#1111"
