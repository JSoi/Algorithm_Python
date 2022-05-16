class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {}
        stack = []
        visited = set()

        for i in range(len(s)):
            last_occ[s[i]] = i

        for i in range(len(s)):
            if s[i] not in visited:
                while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        return ''.join(stack)


def isAlphabetic(s1: list, index: int) -> bool:
    s = []
    s.extend(s1)
    # contains는 수행한 상태
    if len(s) < 1:  # 비어 있을 경우
        return True
    now = None
    while len(s) > 0:
        if not now:  # 이전 값이 없을 때(초기시행)
            now = s.pop(0)
            if now == index:
                if len(s) < 1:  # 다음 값이 없을 때
                    return True
                elif ord(now) > ord(s[0]):  # 다음 원소가 존재하며, 알파벳 순서가 아닌 경우
                    return False
        else:
            next = s.pop(0)
            if next == index and ord(now) > ord(next):
                return False
            now = next
    return True


# 정렬해서 stack에 넣고, peek했을 때
#  print(' '.join(l for l in sorted(s)))


sol = Solution()
sol.removeDuplicateLetters("cbacdcbc")
