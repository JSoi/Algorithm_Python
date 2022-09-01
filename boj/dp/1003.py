import sys

casecount = int(sys.stdin.readline().rstrip())
fibolist = list()

for _ in range(casecount):
    fibolist.append(int(sys.stdin.readline().rstrip()))
max_input = max(fibolist)
if max_input != 0:
    dp_zero = [0] * (max_input + 1)
    dp_one = [0] * (max_input + 1)
    dp_zero[1] = dp_one[0] = 0
    dp_zero[0] = dp_one[1] = 1

    for i in range(2, max_input + 1):
        dp_zero[i] = dp_zero[i - 1] + dp_zero[i - 2]
        dp_one[i] = dp_one[i - 1] + dp_one[i - 2]

    for fi in fibolist:
        print(dp_zero[fi], dp_one[fi])
else:
    print(1, 0)