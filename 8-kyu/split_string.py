# 8 kyu - Split String
# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def solution(s):
    result=[]
    i=0
    if (len(s)%2==1): s+='_'
    while(i<len(s)):
        result.append(s[i:i+2])
        i+=2
    return result

