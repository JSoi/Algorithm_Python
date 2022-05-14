
# https://leetcode.com/problems/3sum/
# 3 sum

num = [-1, 0, 1, 2, -1, -4]
answer = []
for i in range(len(num)-2):
    for j in range(i + 1, len(num)-1):
        for k in range(j + 1, len(num)):
            if num[i] + num[j] + num[k] == 0:
                answer.append([num[i], num[j], num[k]])

print(answer)
