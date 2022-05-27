import sys

cnt = int(sys.stdin.readline())
mylist = list()
for _ in range(cnt):
    mylist.append(int(sys.stdin.readline()))
mylist.sort()
answer=''
for l in mylist:
    print(l)