
def backtracking(n):
    answer = []

    def back(track, mysum):
        if mysum > n:
            return
        if mysum == n:
            answer.append(track)
            return
        back(track + [1], mysum + 1)
        back(track + [2], mysum + 2)
        back(track + [3], mysum + 3)

    back(list(), 0)
    return str(len(answer))


cnt = int(input())
out = ""
for _ in range(cnt):
    eachi = int(input())
    out += (backtracking(eachi) + '\n')
print(out)
