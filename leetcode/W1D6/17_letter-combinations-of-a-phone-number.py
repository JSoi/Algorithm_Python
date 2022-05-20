from typing import List


class Solution:

    def letterCombinations_mine(self, digits: str) -> List[str]:
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

    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)
        if not digits:
            return []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        return result


sol = Solution()
print(sol.letterCombinations("23"))
