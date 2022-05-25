import heapq
import sys

cnt = int(sys.stdin.readline())
mylist = list()
ans = ''
for _ in range(cnt):
    line = int(sys.stdin.readline())
    if line == 0:
        if mylist:
            ans += str(heapq.heappop(mylist)) + '\n'
        else:
            ans += '0\n'
    else:
        heapq.heappush(mylist, line)
print(ans)