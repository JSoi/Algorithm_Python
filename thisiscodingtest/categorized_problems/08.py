# 문자열 재정렬
import sys

string = sys.stdin.readline().strip()
alpha = []
digit_sum = 0
for i in range(len(string)):
    if string[i].isdigit():
        digit_sum += int(string[i])
    else:
        alpha.append(string[i])
alpha.sort()
print(''.join(alpha) + str(digit_sum))

'''
K1KA5CB7
'''
