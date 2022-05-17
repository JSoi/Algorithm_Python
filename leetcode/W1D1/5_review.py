class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        if len(s) < 2:
            return s
        for i in range(len(s) - 1):  # +1, +2 를 해주기 때문에 마지막에서 2번째 원소까지만 돈다
            str1 = go(i, i + 1, s);  # 0,1 | 1,2 | 2,3
            str2 = go(i, i + 2, s);  # 0,2 | 1,3 | 2,4
            # 형식으로
            answer = max(answer, str1, str2, key=len)
        return answer


def go(start, end, s):
    while 0 <= start and end < len(s) and s[start] == s[end]:
        start -= 1
        end += 1
    return s[start + 1:end]
