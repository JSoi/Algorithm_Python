import heapq
import sys

cnt = int(input())
mylist = list()
ans = ''
for _ in range(cnt):
    line = int(sys.stdin.readline())
    if line == 0:
        if len(mylist) == 0:
            ans += '0\n'
        else:
            ans += str(-heapq.heappop(mylist)) + '\n'
    else:
        heapq.heappush(mylist, -line)
print(ans)