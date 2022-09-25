import sys

N = int(sys.stdin.readline().rstrip())
inputlist = []
for _ in range(N):
    inputlist.append(int(sys.stdin.readline().rstrip()))
inputlist.sort(reverse=True)
print(inputlist)

'''
3
15
27
12
'''
