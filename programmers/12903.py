def solution(s):
    return s[len(s) // 2 + (-1 if len(s) % 2 == 0 else 0): len(s) // 2 + 1]
