import collections
import re
from typing import Deque


class Solution:
    def pel(self, s: str) -> bool:
        s = s.lower()
        strs = []
        for i in s:
            if i.isalnum():
                strs.append(i.lower())
        # print(strs)
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

    def pel2(self, s: str) -> bool:
        s = s.lower()
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.pop() != strs.popleft():
                return False
        return True

    def pel3(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]

    def longPel(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                temp = s[i:j]
                if self.pel3(s[i:j]):
                    answer = temp if len(answer) < len(temp) else answer
        return answer



# A man, a plan, a canal : panama

# print(pel(line))
# print(pel2(line))
# print(pel3(line))

if __name__ == '__main__':
    sol = Solution()
    print(sol.pel3('A man, a plan, a canal : panama'))
