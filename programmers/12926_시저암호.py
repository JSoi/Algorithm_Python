def solution(s, n):
    letter = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        if s[i] != ' ':
            original = s[i]
            if original.isupper():
                s[i] = letter[(letter.index(s[i].lower()) + n) % len(letter)].upper()
            else:
                s[i] = letter[(letter.index(s[i].lower()) + n) % len(letter)]
    return s
