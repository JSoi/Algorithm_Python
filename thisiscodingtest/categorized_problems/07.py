# 럭키 스트레이트
# https://www.acmicpc.net/problem/18406
N = input().strip()
length = len(N)
left = right = 0
for i in range(length // 2):
    left += int(N[i])
    right += int(N[length - i - 1])
print("LUCKY" if left == right else "READY")
# 123402
# 7755
