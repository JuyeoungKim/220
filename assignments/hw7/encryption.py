def encode_better(s,k):
    acc = " "
    for i in range(len(s)):
        c = s[i]
        key = k[i % len(k)]
        key = ord(key) - 97
        y = ord(c) + key
        z = chr(y)
        acc += z
    return acc

def encode(s,k):
    acc = ""
    for c in s:
        i = ord(c)
        key = k + i
        c = chr(key)
        acc += c
    return acc