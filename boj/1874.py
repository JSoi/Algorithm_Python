cnt = int(input())
arr = [0] * int(cnt)
stk = []
answer = ""
for i in range(cnt):
    arr[cnt - i - 1] = int(input())

for j in range(1, cnt + 1):
    # print(j)
    stk.append(j)
    answer += "+\n"
    while stk and stk[-1] == arr[-1]:
        arr.pop()
        stk.pop()
        answer += "-\n"
if len(stk) == 0 and len(arr) == 0:
    print(answer)
else:
    print("NO")
