from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                  ['p', 'q', 'r', 's'],
                  ['t', 'u', 'v'],
                  ['w', 'x', 'y', 'z'],
                  []
                  ]
        answer = []

        def go(k, string):
            if len(string) == len(digits) and string not in answer:
                answer.append(string)
                return
            if k >= len(digits):
                return
            for n in keypad[int(digits[k])]:
                go(k + 1, string + n)

        if len(digits) == 1:
            return keypad[int(digits[0])]
        for i in range(len(digits)):
            go(int(i), "")

        print(answer)
        return answer


sol = Solution()
print(sol.letterCombinations("23"))
