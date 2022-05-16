class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {} # 책에서는 collections.Counter(s)
        # counter는 출연빈도를 key-value 형으로 dictionary에 넣어줍니다
        stack = []
        visited = set() # 방문했는지 여부를 알려주는 set(중복 X, 순서 X)

        for i in range(len(s)): # 문자의 마지막 장소를 저장해 둔다.
            last_occ[s[i]] = i # ex : cabb -> {'c':0, 'b':3, 'a':1}

        for i in range(len(s)): # 문자열 char 하나하나 탐색
            if s[i] not in visited: # 방문 Set에 들어있지 않은 상태라면 다음을 수행한다
                # 3가지의 조건을 만족할 동안 while문을 실행합니다
                # 스택이 비어있지 않고
                # 스택의 마지막원소(peek)한 값이 문자열 하나보다 큰 값이며(
                # 스택의 peek 한 위치가 마지막이 아닐 경우 stack에서 지우고 visited에서도 제거해준다
                # (방문하지 않았다고 표기 & 답에서도 제거) - 그렇게 되면 for문을 돌 때 해당 인덱스를 다시 체크하고 넣어주게 된다
                while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
                    visited.remove(stack.pop())
                    # stack 안에 있는 방문 set에서 제거해준다
                stack.append(s[i]) # stack에 해당 인덱스를 더해준다
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
print(sol.removeDuplicateLetters("cba"))
