class Solution:
    def longestPalindrome2(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                temp = s[i:j]
                temps = s[i:j];
                if (temps == temps[::-1]):
                    answer = temp if len(answer) < len(temp) else answer
        return answer

    ##복잡도가 n^2이 되기 때문에 Time-out!

    def longestPalindrome(sel, s: str) -> str:
        result = ""
        if len(s) == 1:
            return s

        def fromCenter(start: int, end: int) -> str:
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1:end]
            # 조건을 만족하지 못하고 끝날 시에는 start, end를 포함하지 않고 리턴해야 한다

        # 이 경우를 위해 짝수 홀수 나누는듯
        for i in range(len(s) - 1):
            result = max(result, fromCenter(i, i + 1), fromCenter(i, i + 2), key=len)
        return result