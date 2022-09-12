def solution(s, n):
    letter = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for i in range(len(s)):
        add = ''
        if s[i] != ' ':
            original = s[i]
            if original.isupper():
                add = letter[(letter.index(s[i].lower()) + n) % len(letter)].upper()
            else:
                add = letter[(letter.index(s[i].lower()) + n) % len(letter)]
        else:
            add = ' '
        answer += add
    return answer
