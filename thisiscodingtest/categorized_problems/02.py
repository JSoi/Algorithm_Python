# 곱하기 또는 더하기
import sys

S = sys.stdin.readline().strip()
numlist = [int(S[i]) for i in range(len(S))]
# print(numlist)
val = numlist[0]
for i in range(1,len(numlist)):
    val = max(val + numlist[i], val * numlist[i])
print(val)
# 02984
# 567
