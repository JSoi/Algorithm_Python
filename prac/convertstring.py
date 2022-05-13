

from typing import List

def reverseString(s: List[str]) -> None:
    start, end = 0, len(s) - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


def reverseString2(s: List[str]) -> None:
    s.reverse()


list = ["h", "e", "l", "l", "o"]
reverseString(list)
