sugar = int(input())
# 봉지는 3kg, 5kg가 있다
# sugar = 3a + 5b
answer = -1
for i in range(sugar // 5, -1, -1):
    # 5kg 봉지로 나올 수 있는 최대
    leftover = sugar - 5 * i
    if leftover % 3 == 0:
        answer = (leftover // 3) + i
        break
print(answer)